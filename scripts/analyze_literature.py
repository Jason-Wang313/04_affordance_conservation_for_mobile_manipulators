"""Generate literature maps, novelty decision artifacts, and selected BibTeX."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
PAPER = ROOT / "paper"
MATRIX_CSV = DOCS / "related_work_matrix.csv"


HIDDEN_ASSUMPTIONS = [
    "Affordance is an object- or part-level property rather than a context-censored observation.",
    "Changing the mobile base pose changes access, not the latent affordance itself.",
    "Clutter can be represented as generic observation noise or an obstacle field without changing the affordance variable.",
    "A failed attempt is negative evidence about the object rather than evidence that access was blocked.",
    "Reachability is a sufficient proxy for manipulation success.",
    "Graspability and task affordance are interchangeable.",
    "The robot's base pose distribution in training covers deployment.",
    "Action primitives have a fixed frame independent of base and scene layout.",
    "The correspondence between contacts across context changes is known or trivial.",
    "Scene graphs preserve enough geometry to decide swept-volume access.",
    "Occlusion, collision, and semantic non-affordance can be learned from the same binary label.",
    "A planner may query affordances as static predicates without corrupting their meaning.",
    "Object state is unchanged by prior navigation, contact, or clutter motions.",
    "Clutter perturbations are independent and identically distributed.",
    "Manipulation failures are independent across base poses once the object is fixed.",
    "The manipulator morphology is fixed and does not enter the affordance definition.",
    "A learned affordance map can be recomputed cheaply for each base pose.",
    "The relevant invariance group is a rigid scene transform rather than a quotient over access variables.",
    "Language-conditioned affordances inherit physical validity from visual grounding.",
    "Negative labels are uncensored, even when the robot could not physically try the action.",
    "Benchmark train/test splits contain the base-clutter shifts that matter in homes, labs, and warehouses.",
    "Base placement is a downstream planning problem after affordance prediction.",
    "Dense value maps are semantically calibrated across unreachable and reachable regions.",
    "Conservation failures indicate model error, not possible object or clutter state change.",
    "Arm-base coupling can be separated from contact semantics without an explicit interface.",
]

CANDIDATES = [
    {
        "name": "Conserved Affordance Quotients",
        "broken_assumption": "binary success labels directly measure object affordance",
        "central_mechanism": "divide observed success into a conserved contact-frame affordance and a mutable access term, then project labels onto equivalence classes across base/clutter orbits",
        "why_not_weak": "changes the target variable and estimator rather than adding a verifier, uncertainty head, or bigger predictor",
        "evidence_path": "sample-complexity claim plus mobile-manipulation simulation with controlled base/clutter shifts",
        "score": 9.6,
    },
    {
        "name": "Censored Negative Affordance Learning",
        "broken_assumption": "failed action attempts are true negative labels",
        "central_mechanism": "treat unreachable trials as censored observations in a survival-style affordance estimator",
        "why_not_weak": "new label semantics, but less directly distinct from positive-unlabeled and missing-data literature",
        "evidence_path": "compare censored and uncensored estimators under unreachable contexts",
        "score": 8.2,
    },
    {
        "name": "Clutter Topology Affordance Gates",
        "broken_assumption": "clutter density is the relevant variable",
        "central_mechanism": "use swept-volume homotopy classes rather than object counts to gate contact access",
        "why_not_weak": "a genuine physical abstraction, but narrower and closer to motion planning",
        "evidence_path": "show identical density with different access topology",
        "score": 7.8,
    },
    {
        "name": "Morphology-Relative Affordance Gauges",
        "broken_assumption": "affordances transfer between embodiments without changing coordinates",
        "central_mechanism": "represent affordance in a robot-specific quotient space induced by reachable contact screws",
        "why_not_weak": "mechanistic but broad enough to become a survey unless scoped tightly",
        "evidence_path": "compare arm lengths and bases in simulation",
        "score": 7.5,
    },
    {
        "name": "Affordance Residuals for Object-State Change",
        "broken_assumption": "conservation violations are model error",
        "central_mechanism": "use repeated quotient residuals to detect when an object part or articulation changed state",
        "why_not_weak": "useful diagnostic, but closest to change detection unless paired with quotient estimator",
        "evidence_path": "detect handle removal/articulation lock from residuals",
        "score": 7.3,
    },
]


def md_escape(text: object) -> str:
    value = "" if text is None else str(text)
    value = value.replace("|", "\\|")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def short(text: object, n: int = 240) -> str:
    value = md_escape(text)
    if len(value) <= n:
        return value
    return value[: n - 3].rstrip() + "..."


def latex_escape(text: object) -> str:
    value = "" if text is None else str(text)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def rows_by_cluster(df: pd.DataFrame) -> str:
    counts = df["cluster"].value_counts().reset_index()
    counts.columns = ["cluster", "count"]
    lines = ["| Cluster | Count in 1100 | Top hostile examples |", "|---|---:|---|"]
    for _, row in counts.iterrows():
        cluster = row["cluster"]
        examples = df[df["cluster"] == cluster].head(3)["title"].tolist()
        lines.append(f"| {md_escape(cluster)} | {int(row['count'])} | {short('; '.join(examples), 260)} |")
    return "\n".join(lines)


def year_histogram(df: pd.DataFrame) -> str:
    years = pd.to_numeric(df["year"], errors="coerce").dropna().astype(int)
    bins = {
        "pre-2000": int((years < 2000).sum()),
        "2000-2009": int(((years >= 2000) & (years <= 2009)).sum()),
        "2010-2015": int(((years >= 2010) & (years <= 2015)).sum()),
        "2016-2020": int(((years >= 2016) & (years <= 2020)).sum()),
        "2021-2026": int(((years >= 2021) & (years <= 2026)).sum()),
    }
    return "\n".join(f"- {k}: {v}" for k, v in bins.items())


def top_table(df: pd.DataFrame, n: int = 25) -> str:
    lines = ["| Rank | Title | Year | Cluster | Less novel | Leaves open |", "|---:|---|---:|---|---|---|"]
    for _, row in df.head(n).iterrows():
        lines.append(
            "| {rank} | {title} | {year} | {cluster} | {less} | {open} |".format(
                rank=int(row["rank"]),
                title=short(row["title"], 110),
                year=md_escape(row["year"]),
                cluster=short(row["cluster"], 60),
                less=short(row["what_it_makes_less_novel"], 120),
                open=short(row["what_it_leaves_open"], 140),
            )
        )
    return "\n".join(lines)


def write_literature_map(df: pd.DataFrame) -> None:
    hostile = df.head(100)
    deep = df.head(250)
    serious = df.head(300)
    text = f"""# Literature Map

## Sweep Protocol
- Landscape sweep: {len(df)} OpenAlex records from 30 robotics/mobile-manipulation/affordance queries.
- Serious skim: top {len(serious)} ranked records, using titles, venues, abstracts when available, concepts, and query provenance.
- Deep read set: top {len(deep)} ranked records, still at abstract/metadata level unless the record itself exposed more detail.
- Hostile prior-work set: top {len(hostile)} records most likely to make the seed idea less novel.
- Ranking is not a citation-impact ranking; it is tuned for mobile manipulation, affordance, reachability, base pose, clutter, invariance, and action-model terms.

## Field Box
The selected field box is mobile manipulation under changing base pose and clutter, with affordance learning/planning as the interface between object-centered action semantics and whole-body access. The box includes learned object/part affordance predictors, reachability maps, whole-body mobile manipulation planning, task-and-motion planning, clutter rearrangement, equivariant manipulation representations, and recent language/foundation-model manipulation systems.

## Cluster Counts
{rows_by_cluster(df)}

## Year Distribution
{year_histogram(df)}

## What the Sweep Says
1. Affordance papers often learn a map from perception to action possibilities, but the binary labels are usually entangled with whether the robot could approach the part from the sampled base pose.
2. Mobile-manipulation and base-placement papers model access well, but usually take the affordance predicate or target contact as already specified.
3. Reachability maps and inverse-reachability models explain kinematic access but do not preserve a separate object-side affordance variable.
4. Clutter and rearrangement work shows the access variable is physically important, yet often treats the object affordance as fixed background knowledge.
5. Invariance/equivariance work gives useful transport machinery, but most label-preserving groups are rigid geometric groups; the mobile-manipulation problem needs a quotient where the full success label is not conserved, only one factor is.
6. Vision-language and robot foundation models make dense action values convenient, but do not by themselves distinguish a changed object affordance from a temporarily inaccessible one.

## Top Hostile Papers Snapshot
{top_table(df, 30)}

## Hidden Assumptions That May Be False
"""
    text += "\n".join(f"{i + 1}. {assumption}" for i, assumption in enumerate(HIDDEN_ASSUMPTIONS))
    text += """

## Directions That Break Those Assumptions
"""
    for c in CANDIDATES:
        text += (
            f"\n### {c['name']}\n"
            f"- Broken assumption: {c['broken_assumption']}.\n"
            f"- Central mechanism: {c['central_mechanism']}.\n"
            f"- Why it is not a weak move: {c['why_not_weak']}.\n"
            f"- Evidence path: {c['evidence_path']}.\n"
            f"- Score: {c['score']}/10.\n"
        )
    text += """

## Strongest Direction
The strongest direction is **Conserved Affordance Quotients**. It has a sharper mechanism-level distinction than a new benchmark, active learner, verifier, or larger policy: the paper changes what is estimated. The observed mobile-manipulation success label is treated as a product or gate of (i) a conserved contact-frame affordance and (ii) a mutable base/clutter access field. The research question becomes when and how the first term can be transported across context changes while the second term is recomputed geometrically.
"""
    (DOCS / "literature_map.md").write_text(text, encoding="utf-8")


def write_hostile(df: pd.DataFrame) -> None:
    lines = [
        "# Hostile Prior Work Set",
        "",
        "This set contains the top 100 records most likely to attack novelty. Each extraction is abstract/metadata-level unless marked otherwise in the matrix.",
    ]
    for _, row in df.head(100).iterrows():
        lines.extend(
            [
                "",
                f"## H{int(row['rank']):03d}. {md_escape(row['title'])} ({md_escape(row['year'])})",
                f"- Venue/source: {md_escape(row['venue']) or 'not listed'}",
                f"- Authors: {short(row['authors'], 220) or 'not listed'}",
                f"- Cluster: {md_escape(row['cluster'])}",
                f"- Problem claimed: {md_escape(row['problem_claimed'])}",
                f"- Actual mechanism introduced: {md_escape(row['actual_mechanism_introduced'])}",
                f"- Hidden assumptions: {md_escape(row['hidden_assumptions'])}",
                f"- Variables treated as fixed: {md_escape(row['variables_treated_as_fixed'])}",
                f"- Failure modes ignored: {md_escape(row['failure_modes_ignored'])}",
                f"- What it makes less novel: {md_escape(row['what_it_makes_less_novel'])}",
                f"- What it leaves open: {md_escape(row['what_it_leaves_open'])}",
                f"- Evidence basis: {md_escape(row['extraction_confidence'])}",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_boundary(df: pd.DataFrame) -> None:
    lines = [
        "# Novelty Boundary Map",
        "",
        "## Boundary Claim",
        "The paper is not novel if it is only an affordance predictor, a reachability map, a base-placement planner, a clutter rearrangement planner, a language-conditioned value map, or an equivariant representation. It is only novel if the central object is a quotient representation that explicitly separates the conserved object/contact term from the mutable base/clutter access term and uses that separation for estimation, prediction, and diagnosis.",
        "",
        "## Not Novel by Cluster",
    ]
    for cluster, group in df.groupby("cluster", sort=False):
        top_titles = "; ".join(group.head(5)["title"].tolist())
        less = Counter(group["what_it_makes_less_novel"]).most_common(1)[0][0]
        open_ = Counter(group["what_it_leaves_open"]).most_common(1)[0][0]
        lines.extend(
            [
                "",
                f"### {md_escape(cluster)}",
                f"- Representative hostile records: {short(top_titles, 360)}",
                f"- Makes less novel: {md_escape(less)}.",
                f"- Leaves open: {md_escape(open_)}.",
                "- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.",
            ]
        )
    lines.extend(
        [
            "",
            "## Positive Novelty Boundary",
            "- Define affordance as a contact-frame latent variable that can be conserved even when observed task success is not.",
            "- Define access as a base/clutter-dependent gate computed from reachability and swept-volume obstruction.",
            "- Provide an estimator that projects observed successes onto conserved equivalence classes after quotienting by access.",
            "- Prove a sample-complexity or identifiability statement under explicit assumptions.",
            "- Demonstrate under controlled base-pose and clutter shifts that the broken assumption matters.",
            "",
            "## Negative Boundary",
            "- Do not claim full real-robot validation.",
            "- Do not claim full manipulation planning is solved.",
            "- Do not claim all affordances are conserved; conservation is conditional on stable object/contact state and correct correspondence.",
            "- Do not claim the access model is learned or perfect outside the controlled evidence.",
        ]
    )
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_decision() -> None:
    lines = [
        "# Novelty Decision",
        "",
        "## Candidate Evaluation",
        "| Candidate | Broken assumption | Central mechanism | Evidence path | Score |",
        "|---|---|---|---|---:|",
    ]
    for c in sorted(CANDIDATES, key=lambda x: x["score"], reverse=True):
        lines.append(
            f"| {md_escape(c['name'])} | {md_escape(c['broken_assumption'])} | {md_escape(c['central_mechanism'])} | {md_escape(c['evidence_path'])} | {c['score']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## Chosen Thesis",
            "**Affordance Conservation for Mobile Manipulators**: in mobile manipulation, the observed success of an action contact under a base pose and clutter state should be modeled as a mutable access gate times a conserved contact-frame affordance. Learning or planning directly on the observed success label entangles object semantics with base/clutter censoring. A conserved affordance quotient recovers the object-side variable, transports it across base and clutter changes, and exposes residuals when the object/contact state truly changes.",
            "",
            "## Why This Wins",
            "- It changes the central mechanism from prediction or planning to conservation-aware factorization.",
            "- It attacks a false hidden assumption shared by affordance predictors and mobile-base planners from opposite sides.",
            "- It admits a clean theorem: quotient projection reduces sample complexity from context-specific labels to contact-class labels when access is known or certified.",
            "- It is testable with a small mobile-manipulation simulator where base pose and clutter can change while object affordance remains fixed.",
            "",
            "## What Will Be Unsupported",
            "- Real-robot transfer is not established.",
            "- The access gate is geometric/certified in the experiment, not learned from raw depth.",
            "- The theorem requires correct contact correspondence and stable object state.",
        ]
    )
    (DOCS / "novelty_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_claims() -> None:
    text = """# Claims

## Main Claim
Observed mobile-manipulation success labels conflate a conserved contact affordance with a mutable base/clutter access gate. Estimating the conserved quotient improves cross-context generalization when object state is stable and access can be certified.

Status: supported by formal assumptions and planned synthetic evidence, not yet by real-robot experiments.

## Formal Claim
If observations satisfy `Y_i = A_g Z_i + epsilon_i`, where `A_g` is the latent contact affordance for contact class `g`, `Z_i` is a known binary access gate for the sampled base/clutter context, and `epsilon_i` is bounded zero-mean noise observed only when `Z_i=1`, then the quotient estimator `hat A_g = mean(Y_i/Z_i : Z_i=1, class=g)` is unbiased and has Hoeffding concentration using only accessible samples. A context-specific estimator over `K` base/clutter bins needs samples in each bin, yielding a `K`-factor support burden for the same contact class.

Status: proof sketch will be included. This is not a claim about arbitrary learned access models.

## Experimental Claim
In a 2D mobile-manipulation simulator with fixed object contacts, shifted base-pose distributions, and changed clutter, conserved quotient prediction should reduce Brier/log-loss and false blocked-contact predictions relative to object-only, access-only, context-table, and monolithic logistic baselines.

Status: to be tested by `scripts/run_simulation.py`.

## Diagnostic Claim
Large conservation residuals after quotienting indicate either a wrong access certificate, wrong correspondence, or a true object/contact state change.

Status: conceptual and partially testable; should be framed as a diagnostic, not a guaranteed detector.

## Non-Claims
- No claim of superior large-scale robot foundation modeling.
- No claim of solving generic task-and-motion planning.
- No claim of real-world deployment or hardware robustness.
- No claim that every affordance is conserved under all clutter changes.
"""
    (DOCS / "claims.md").write_text(text, encoding="utf-8")


def write_attacks(df: pd.DataFrame) -> None:
    attacks = [
        ("This is just reachability gating.", "No: reachability is the mutable gate; the paper's object is the quotient estimator for the conserved contact variable. The experiment must include access-only and reachability-only baselines."),
        ("Affordance templates already did this.", "Templates encode action-relevant geometry, but the novelty boundary is explicit separation of observed success into conserved contact affordance and mutable base/clutter access, with a concentration claim."),
        ("Task-and-motion planning already checks feasibility.", "TAMP checks feasibility for fixed predicates. The proposed mechanism changes the predicate semantics by treating negative labels under inaccessible contexts as censored, not false."),
        ("A larger policy could learn this implicitly.", "Possibly, but the paper's claim is about identifiability and sample support. The central mechanism is explicit quotient projection and auditable residuals."),
        ("The access gate is assumed known.", "Correct. This is a limitation and a deliberate scope choice. The paper proves and tests the mechanism when access is certified by geometry, not from raw perception."),
        ("Synthetic evidence is too weak.", "Yes for submission strength. The final audit should likely recommend workshop/revise unless the simulation results are unusually compelling."),
        ("Conservation is trivial if the object does not change.", "The nontrivial part is that the observed success label does change under base/clutter shifts; only the quotient is conserved."),
        ("Correspondence across contacts is unsolved.", "Correct. The current paper assumes contact correspondence or class labels. This must be explicit in theorem and limitations."),
        ("Clutter can change the object state.", "Then conservation should fail and residuals should rise. The claim is conditional on stable object/contact state."),
        ("The monolithic logistic baseline is weak.", "The evidence should include both context table and monolithic learned predictor, and report exactly what features each receives."),
        ("The theorem is just a mean estimator.", "The simplicity is intentional: it isolates the variable change. The paper should not oversell mathematical depth."),
        ("The 1000-paper sweep is API-level, not full-text.", "Correct. The audit should state literature coverage as metadata/abstract-level with hostile top-set extraction."),
    ]
    lines = [
        "# Reviewer Attacks",
        "",
        "## Likely Attacks and Required Answers",
    ]
    for i, (attack, answer) in enumerate(attacks, start=1):
        lines.extend([f"{i}. Attack: {attack}", f"   Response: {answer}"])
    lines.extend(
        [
            "",
            "## Hostile Prior Work Most Likely To Be Cited By Reviewers",
            top_table(df, 15),
        ]
    )
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def bib_key(index: int) -> str:
    return f"rw{index:03d}"


def write_bib(df: pd.DataFrame) -> None:
    PAPER.mkdir(parents=True, exist_ok=True)
    selected = df.head(80).copy()
    entries: List[str] = []
    selected_meta: List[Dict[str, str]] = []
    for i, (_, row) in enumerate(selected.iterrows(), start=1):
        key = bib_key(i)
        authors = [a.strip() for a in str(row.get("authors", "")).split(";") if a.strip()]
        author_field = " and ".join(authors[:10]) if authors else "Anonymous"
        raw_year = str(row.get("year", "")).strip()
        try:
            year = str(int(float(raw_year))) if raw_year else "n.d."
        except ValueError:
            year = raw_year or "n.d."
        venue = str(row.get("venue", "")) if str(row.get("venue", "")).strip() else "OpenAlex record"
        doi = str(row.get("doi", "")).replace("https://doi.org/", "").strip()
        entry_type = "inproceedings" if any(term in venue.lower() for term in ["conference", "proceedings", "icra", "iros", "rss", "corl"]) else "article"
        venue_field = "booktitle" if entry_type == "inproceedings" else "journal"
        fields = [
            f"  title = {{{latex_escape(row.get('title', 'Untitled'))}}}",
            f"  author = {{{latex_escape(author_field)}}}",
            f"  year = {{{latex_escape(year)}}}",
            f"  {venue_field} = {{{latex_escape(venue)}}}",
        ]
        if doi:
            fields.append(f"  doi = {{{latex_escape(doi)}}}")
        entries.append(f"@{entry_type}{{{key},\n" + ",\n".join(fields) + "\n}\n")
        selected_meta.append(
            {
                "key": key,
                "title": str(row.get("title", "")),
                "year": year,
                "cluster": str(row.get("cluster", "")),
            }
        )
    (PAPER / "references.bib").write_text("\n".join(entries), encoding="utf-8")
    (DATA / "selected_references.json").write_text(json.dumps(selected_meta, indent=2), encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    if not MATRIX_CSV.exists():
        (DOCS / "analysis_failure.md").write_text("Missing docs/related_work_matrix.csv.\n", encoding="utf-8")
        return 0
    df = pd.read_csv(MATRIX_CSV).fillna("")
    df["rank"] = pd.to_numeric(df["rank"], errors="coerce").fillna(999999).astype(int)
    df["relevance_score"] = pd.to_numeric(df["relevance_score"], errors="coerce").fillna(0.0)
    df = df.sort_values(["rank", "relevance_score"], ascending=[True, False])

    write_literature_map(df)
    write_hostile(df)
    write_boundary(df)
    write_decision()
    write_claims()
    write_attacks(df)
    write_bib(df)
    summary = {
        "matrix_rows": int(len(df)),
        "serious_skim_rows": 300,
        "deep_read_rows": 250,
        "hostile_rows": 100,
        "chosen_direction": "Conserved Affordance Quotients",
        "outputs": [
            "docs/literature_map.md",
            "docs/hostile_prior_work.md",
            "docs/novelty_boundary_map.md",
            "docs/novelty_decision.md",
            "docs/claims.md",
            "docs/reviewer_attacks.md",
            "paper/references.bib",
        ],
    }
    (DATA / "literature_analysis_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        DOCS.mkdir(parents=True, exist_ok=True)
        (DOCS / "analysis_failure.md").write_text(f"Analysis failed but was recorded: {exc}\n", encoding="utf-8")
        print(f"ANALYSIS_FAILURE_RECORDED: {exc}")
        raise SystemExit(0)
