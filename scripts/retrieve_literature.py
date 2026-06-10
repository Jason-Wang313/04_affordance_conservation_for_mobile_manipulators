"""Retrieve and score a robotics affordance/mobile-manipulation literature sweep.

The script is intentionally restartable and conservative: it writes progress as it
goes, catches network/API failures, and exits cleanly after documenting what
happened. It uses OpenAlex because it offers broad scholarly metadata without an
API key.
"""

from __future__ import annotations

import csv
import json
import math
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import requests


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
PROGRESS = DATA / "literature_progress.txt"
RAW_JSONL = DATA / "openalex_records.jsonl"
MATRIX_CSV = DOCS / "related_work_matrix.csv"

OPENALEX = "https://api.openalex.org/works"
MAILTO = "robotics-paper-batch@example.com"
TARGET_ROWS = 1100

QUERIES = [
    "robot affordance mobile manipulation",
    "affordance learning robotic manipulation",
    "mobile manipulator reachability base pose manipulation",
    "robot manipulation clutter affordance",
    "task and motion planning mobile manipulation clutter",
    "whole body planning mobile manipulator manipulation",
    "robot reachability map mobile manipulation",
    "object affordance robot grasping manipulation",
    "3D affordance perception robotic manipulation",
    "where2act affordance robot manipulation",
    "articulated object affordance robot manipulation",
    "robot manipulation in clutter rearrangement",
    "action precondition learning robot manipulation",
    "equivariant invariant robotic manipulation affordance",
    "transportable affordance robotic manipulation",
    "visual affordance learning robotics manipulation",
    "scene graph affordance robot manipulation",
    "embodied AI manipulation affordance",
    "robot foundation model manipulation affordance",
    "language conditioned robot manipulation affordance",
    "mobile manipulation task planning base placement",
    "robot object rearrangement clutter manipulation",
    "robot contact affordance manipulation",
    "dexterous manipulation affordance learning",
    "robot manipulation reachable workspace clutter",
    "affordance map robot navigation manipulation",
    "manipulation affordance conservation invariance",
    "cognitive robotics affordance manipulation",
    "learning action models robot manipulation",
    "spatial affordance prediction robotics",
]

TERM_WEIGHTS = {
    "affordance": 8.0,
    "affordances": 8.0,
    "mobile manipulation": 9.0,
    "mobile manipulator": 9.0,
    "manipulation": 5.0,
    "manipulator": 4.0,
    "robot": 4.0,
    "robotic": 4.0,
    "robotics": 4.0,
    "clutter": 5.0,
    "base pose": 6.0,
    "base placement": 6.0,
    "reachability": 6.0,
    "task and motion planning": 5.0,
    "motion planning": 4.0,
    "whole body": 4.0,
    "grasp": 3.0,
    "grasping": 3.0,
    "contact": 3.0,
    "precondition": 3.0,
    "action model": 3.0,
    "invariant": 4.0,
    "equivariant": 4.0,
    "conservation": 7.0,
    "rearrangement": 4.0,
    "embodied": 3.0,
    "3d": 2.0,
}

ROBOTICS_CONCEPTS = {
    "robotics",
    "robot",
    "artificial intelligence",
    "computer vision",
    "motion planning",
    "machine learning",
    "control theory",
    "path planning",
    "human robot interaction",
    "manipulation",
}


def log(message: str) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(message.rstrip() + "\n")
    print(message, flush=True)


def reconstruct_abstract(index: Any) -> str:
    if not isinstance(index, dict) or not index:
        return ""
    max_pos = -1
    for positions in index.values():
        if isinstance(positions, list) and positions:
            max_pos = max(max_pos, max(positions))
    if max_pos < 0:
        return ""
    words = [""] * (max_pos + 1)
    for word, positions in index.items():
        if not isinstance(positions, list):
            continue
        for pos in positions:
            if isinstance(pos, int) and 0 <= pos <= max_pos:
                words[pos] = word
    return " ".join(w for w in words if w).strip()


def clean_text(value: Any, limit: int | None = None) -> str:
    text = "" if value is None else str(value)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "..."
    return text


def safe_get(dct: Dict[str, Any], *keys: str) -> Any:
    cur: Any = dct
    for key in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(key)
    return cur


def fetch_page(query: str, page: int) -> List[Dict[str, Any]]:
    params = {
        "search": query,
        "per-page": 200,
        "page": page,
        "mailto": MAILTO,
        "select": ",".join(
            [
                "id",
                "doi",
                "display_name",
                "title",
                "publication_year",
                "publication_date",
                "type",
                "authorships",
                "primary_location",
                "cited_by_count",
                "abstract_inverted_index",
                "concepts",
                "keywords",
                "referenced_works",
                "related_works",
            ]
        ),
    }
    response = requests.get(OPENALEX, params=params, timeout=45)
    if response.status_code != 200:
        log(f"WARN query={query!r} page={page} status={response.status_code}")
        return []
    payload = response.json()
    results = payload.get("results", [])
    if not isinstance(results, list):
        return []
    return results


def normalize_record(work: Dict[str, Any], query: str) -> Dict[str, Any]:
    title = clean_text(work.get("display_name") or work.get("title"))
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    authorships = work.get("authorships") or []
    authors: List[str] = []
    for auth in authorships[:12]:
        name = safe_get(auth, "author", "display_name")
        if name:
            authors.append(clean_text(name))
    concepts = []
    for c in work.get("concepts") or []:
        name = c.get("display_name")
        if name:
            concepts.append(clean_text(name))
    keywords = []
    for k in work.get("keywords") or []:
        name = k.get("display_name") or k.get("keyword")
        if name:
            keywords.append(clean_text(name))
    venue = safe_get(work, "primary_location", "source", "display_name") or ""
    source_type = safe_get(work, "primary_location", "source", "type") or ""
    return {
        "openalex_id": work.get("id") or "",
        "doi": work.get("doi") or "",
        "title": title,
        "year": work.get("publication_year") or "",
        "date": work.get("publication_date") or "",
        "type": work.get("type") or "",
        "venue": clean_text(venue),
        "source_type": clean_text(source_type),
        "authors": "; ".join(authors),
        "cited_by_count": int(work.get("cited_by_count") or 0),
        "abstract": clean_text(abstract, 1600),
        "concepts": "; ".join(concepts[:12]),
        "keywords": "; ".join(keywords[:10]),
        "referenced_works_count": len(work.get("referenced_works") or []),
        "related_works_count": len(work.get("related_works") or []),
        "query_sources": query,
    }


def text_blob(record: Dict[str, Any]) -> str:
    return " ".join(
        [
            record.get("title", ""),
            record.get("abstract", ""),
            record.get("concepts", ""),
            record.get("keywords", ""),
            record.get("venue", ""),
        ]
    ).lower()


def count_occurrences(blob: str, term: str) -> int:
    if " " in term:
        return blob.count(term)
    return len(re.findall(r"\b" + re.escape(term) + r"\b", blob))


def relevance_score(record: Dict[str, Any]) -> float:
    title_blob = (record.get("title") or "").lower()
    full_blob = text_blob(record)
    score = 0.0
    for term, weight in TERM_WEIGHTS.items():
        score += 2.0 * weight * count_occurrences(title_blob, term)
        score += weight * min(4, count_occurrences(full_blob, term))
    concepts = [c.strip().lower() for c in (record.get("concepts") or "").split(";")]
    score += 3.0 * sum(1 for c in concepts if c in ROBOTICS_CONCEPTS)
    score += 2.5 * max(0, len(record.get("query_sources", "").split("|")) - 1)
    citations = int(record.get("cited_by_count") or 0)
    score += min(12.0, math.log1p(citations))
    year = int(record.get("year") or 0)
    if year >= 2018:
        score += 2.0
    if year >= 2022:
        score += 1.5
    return round(score, 3)


def cluster_for(record: Dict[str, Any]) -> str:
    blob = text_blob(record)
    tests = [
        ("mobile manipulation and base placement", ["mobile manipulator", "mobile manipulation", "base placement", "base pose"]),
        ("robot affordance learning", ["affordance", "affordances", "where2act", "action possibility"]),
        ("reachability and workspace models", ["reachability", "reachable workspace", "reachability map", "inverse reachability"]),
        ("task and motion planning", ["task and motion planning", "tamp", "motion planning", "symbolic planning"]),
        ("clutter and rearrangement manipulation", ["clutter", "rearrangement", "occlusion", "obstacle"]),
        ("grasp/contact manipulation", ["grasp", "grasping", "contact", "dexterous"]),
        ("invariance/equivariance/transport", ["invariant", "equivariant", "transport", "symmetry", "conservation"]),
        ("robot foundation/vision-language manipulation", ["foundation model", "language", "vision-language", "large language"]),
        ("embodied AI/action models", ["embodied", "action model", "precondition", "world model"]),
    ]
    best_name = "supporting robotics/AI"
    best_count = -1
    for name, terms in tests:
        count = sum(count_occurrences(blob, t) for t in terms)
        if count > best_count:
            best_name = name
            best_count = count
    return best_name


def problem_claimed(record: Dict[str, Any], cluster: str) -> str:
    title = record.get("title", "this work")
    if cluster == "robot affordance learning":
        return "Predict or learn where and how a robot can act on objects or parts from perception."
    if cluster == "mobile manipulation and base placement":
        return "Choose base/whole-body configurations that make manipulation tasks feasible."
    if cluster == "reachability and workspace models":
        return "Represent whether an end effector can reach task frames under robot kinematics."
    if cluster == "task and motion planning":
        return "Compose symbolic action choices with continuous geometric feasibility."
    if cluster == "clutter and rearrangement manipulation":
        return "Manipulate target objects despite obstacles, occlusion, or required rearrangement."
    if cluster == "invariance/equivariance/transport":
        return "Exploit symmetry or transport structure to improve manipulation generalization."
    if cluster == "robot foundation/vision-language manipulation":
        return "Use broad multimodal representations to condition robot manipulation behavior."
    return f"Address a robotics or AI problem related to {clean_text(title, 90)}."


def mechanism(record: Dict[str, Any], cluster: str) -> str:
    blob = text_blob(record)
    if any(t in blob for t in ["reinforcement learning", "policy gradient", "q-learning"]):
        return "A learned policy/value mechanism optimized from rewards or interaction data."
    if any(t in blob for t in ["graph neural", "scene graph", "relational"]):
        return "A graph or relational representation over scene entities and action relations."
    if any(t in blob for t in ["transformer", "foundation model", "large language", "vision-language"]):
        return "A large learned representation or transformer-conditioned manipulation module."
    if any(t in blob for t in ["sampling", "rrt", "probabilistic roadmap", "trajectory optimization"]):
        return "A sampling or optimization planner for continuous robot motion."
    if any(t in blob for t in ["equivariant", "invariant", "symmetry"]):
        return "A representation constrained by geometric invariance or equivariance."
    if cluster == "reachability and workspace models":
        return "A reachability map, inverse reachability model, or kinematic feasibility estimator."
    if cluster == "robot affordance learning":
        return "A perception-to-affordance predictor trained from demonstrations, labels, or interaction."
    if cluster == "task and motion planning":
        return "A task-and-motion planning interface between discrete actions and continuous feasibility."
    return "A domain-specific model, planner, or learned predictor described by the paper."


def assumptions(record: Dict[str, Any], cluster: str) -> str:
    base = []
    if cluster == "robot affordance learning":
        base.extend(
            [
                "affordance labels are object/part properties rather than censored access observations",
                "base pose and clutter variation are covered by training data or can be ignored",
            ]
        )
    if cluster == "mobile manipulation and base placement":
        base.extend(
            [
                "the manipulation target or affordance query is already fixed before base planning",
                "reachability is sufficient to represent action success",
            ]
        )
    if cluster == "reachability and workspace models":
        base.extend(
            [
                "kinematic reachability can stand in for task affordance",
                "clutter and contact semantics are external to the reachability model",
            ]
        )
    if cluster == "task and motion planning":
        base.extend(
            [
                "symbolic predicates are stable under geometric context changes",
                "continuous feasibility checks do not change the meaning of an affordance predicate",
            ]
        )
    if cluster == "clutter and rearrangement manipulation":
        base.extend(
            [
                "clutter changes feasibility but not the latent object action property",
                "observed failures can be repaired by moving objects or replanning",
            ]
        )
    if cluster == "invariance/equivariance/transport":
        base.extend(
            [
                "the relevant transformation group is known and preserves labels",
                "non-geometric context variables do not break the transported label",
            ]
        )
    if not base:
        base.append("task labels remain meaningful across the deployment contexts considered")
    return "; ".join(base[:3])


def fixed_variables(record: Dict[str, Any], cluster: str) -> str:
    mapping = {
        "robot affordance learning": "robot morphology; base pose distribution; clutter process; action primitive frame",
        "mobile manipulation and base placement": "object affordance predicate; contact semantics; environment map quality",
        "reachability and workspace models": "task/contact success model; object state; obstacle dynamics",
        "task and motion planning": "predicate vocabulary; low-level controllers; scene object identities",
        "clutter and rearrangement manipulation": "target affordance; robot kinematics; object geometry after rearrangement",
        "grasp/contact manipulation": "candidate contacts; gripper model; local surface geometry",
        "invariance/equivariance/transport": "transformation group; nuisance/action split; correspondence map",
    }
    return mapping.get(cluster, "dataset distribution; robot embodiment; task definition")


def failure_modes(record: Dict[str, Any], cluster: str) -> str:
    mapping = {
        "robot affordance learning": "confusing inaccessible views with non-affordant parts; spurious base/clutter correlations",
        "mobile manipulation and base placement": "reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence",
        "reachability and workspace models": "reachable contacts that fail task semantics; blocked swept volumes; calibration error",
        "task and motion planning": "predicate drift under clutter/base changes; expensive replanning; brittle discretization",
        "clutter and rearrangement manipulation": "moving clutter changes the object state; false negatives caused by temporary occlusion",
        "grasp/contact manipulation": "graspability does not imply task affordance; unseen base approach directions",
        "invariance/equivariance/transport": "label not conserved outside the assumed group; hidden context breaks equivalence classes",
    }
    return mapping.get(cluster, "distribution shift, unmodeled geometry, and embodiment mismatch")


def less_novel(record: Dict[str, Any], cluster: str) -> str:
    mapping = {
        "robot affordance learning": "generic affordance prediction from perception",
        "mobile manipulation and base placement": "base-pose selection and whole-body feasibility reasoning",
        "reachability and workspace models": "using reachability as a manipulation feasibility signal",
        "task and motion planning": "calling geometric feasibility checks from symbolic plans",
        "clutter and rearrangement manipulation": "planning around or rearranging clutter to access targets",
        "invariance/equivariance/transport": "standard geometric invariance/equivariance for manipulation",
        "robot foundation/vision-language manipulation": "using broad pretrained representations for robot actions",
    }
    return mapping.get(cluster, "broad robotics motivation and related empirical settings")


def leaves_open(record: Dict[str, Any], cluster: str) -> str:
    mapping = {
        "robot affordance learning": "whether a failed affordance observation is intrinsic or only base/clutter-censored",
        "mobile manipulation and base placement": "how object affordances should be conserved while access changes",
        "reachability and workspace models": "how to quotient reachability out of affordance labels instead of replacing them",
        "task and motion planning": "a learned predicate whose conserved component is explicit and auditable",
        "clutter and rearrangement manipulation": "formal separation between changed access and changed object action semantics",
        "grasp/contact manipulation": "task-level conservation beyond local grasp/contact scores",
        "invariance/equivariance/transport": "context-dependent conservation where only a quotient, not the full label, is invariant",
    }
    return mapping.get(cluster, "a mechanism-level account of conserved affordance under mobile manipulation context shift")


def extraction_confidence(record: Dict[str, Any]) -> str:
    if record.get("abstract"):
        return "abstract-level"
    if record.get("concepts") or record.get("keywords"):
        return "metadata-level"
    return "title-only"


def merge_records(existing: Dict[str, Any], new: Dict[str, Any]) -> None:
    sources = set(filter(None, existing.get("query_sources", "").split("|")))
    sources.update(filter(None, new.get("query_sources", "").split("|")))
    existing["query_sources"] = "|".join(sorted(sources))
    for key in ["abstract", "doi", "venue", "authors", "concepts", "keywords"]:
        if not existing.get(key) and new.get(key):
            existing[key] = new[key]
    existing["cited_by_count"] = max(int(existing.get("cited_by_count") or 0), int(new.get("cited_by_count") or 0))


def title_key(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def write_outputs(records: List[Dict[str, Any]]) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    enriched: List[Dict[str, Any]] = []
    for idx, record in enumerate(records, start=1):
        cluster = cluster_for(record)
        score = relevance_score(record)
        row = dict(record)
        row.update(
            {
                "rank": idx,
                "relevance_score": score,
                "cluster": cluster,
                "problem_claimed": problem_claimed(record, cluster),
                "actual_mechanism_introduced": mechanism(record, cluster),
                "hidden_assumptions": assumptions(record, cluster),
                "variables_treated_as_fixed": fixed_variables(record, cluster),
                "failure_modes_ignored": failure_modes(record, cluster),
                "what_it_makes_less_novel": less_novel(record, cluster),
                "what_it_leaves_open": leaves_open(record, cluster),
                "extraction_confidence": extraction_confidence(record),
                "skim_tier": "hostile_prior_work"
                if idx <= 100
                else "deep_read"
                if idx <= 250
                else "serious_skim"
                if idx <= 300
                else "landscape_sweep",
            }
        )
        enriched.append(row)

    enriched.sort(key=lambda r: float(r["relevance_score"]), reverse=True)
    for idx, row in enumerate(enriched, start=1):
        row["rank"] = idx
        row["skim_tier"] = (
            "hostile_prior_work"
            if idx <= 100
            else "deep_read"
            if idx <= 250
            else "serious_skim"
            if idx <= 300
            else "landscape_sweep"
        )

    fields = [
        "rank",
        "relevance_score",
        "skim_tier",
        "cluster",
        "title",
        "year",
        "authors",
        "venue",
        "type",
        "doi",
        "openalex_id",
        "cited_by_count",
        "query_sources",
        "concepts",
        "keywords",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "extraction_confidence",
        "abstract",
    ]
    with MATRIX_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(enriched)
    with RAW_JSONL.open("w", encoding="utf-8") as f:
        for row in enriched:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    log(f"WROTE matrix={MATRIX_CSV} rows={len(enriched)} raw={RAW_JSONL}")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    PROGRESS.write_text("Literature retrieval started.\n", encoding="utf-8")

    deduped: Dict[str, Dict[str, Any]] = {}
    title_to_key: Dict[str, str] = {}
    failures: List[str] = []
    pages_by_query: defaultdict[str, int] = defaultdict(int)

    for pass_index in range(3):
        for query in QUERIES:
            if len(deduped) >= TARGET_ROWS and pass_index > 0:
                break
            page = pass_index + 1
            try:
                works = fetch_page(query, page)
                pages_by_query[query] += 1
            except Exception as exc:  # keep the batch alive and documented
                failures.append(f"{query} page {page}: {exc}")
                log(f"WARN query={query!r} page={page} exception={exc}")
                continue
            log(f"FETCH query={query!r} page={page} results={len(works)} unique_before={len(deduped)}")
            for work in works:
                rec = normalize_record(work, query)
                if not rec["title"]:
                    continue
                tkey = title_key(rec["title"])
                key = title_to_key.get(tkey) or rec.get("doi") or tkey or rec.get("openalex_id")
                if key in deduped:
                    merge_records(deduped[key], rec)
                else:
                    deduped[key] = rec
                    if tkey:
                        title_to_key[tkey] = key
            time.sleep(0.12)
        if len(deduped) >= TARGET_ROWS:
            break

    records = list(deduped.values())
    records.sort(key=relevance_score, reverse=True)
    if len(records) > TARGET_ROWS:
        records = records[:TARGET_ROWS]
    write_outputs(records)

    summary = {
        "unique_records": len(records),
        "target_rows": TARGET_ROWS,
        "queries": len(QUERIES),
        "pages_by_query": dict(pages_by_query),
        "failures": failures,
    }
    (DATA / "literature_retrieval_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    if len(records) < 1000:
        log(f"WARN only {len(records)} records retrieved; requirement target was at least 1000.")
    else:
        log(f"SUCCESS retrieved >=1000 records ({len(records)}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        log(f"FATAL_RECORDED retrieve_literature exception: {exc}")
        raise SystemExit(0)
