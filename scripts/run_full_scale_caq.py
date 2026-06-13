"""Full-scale evidence suite for conserved affordance quotients.

The suite is intentionally synthetic. It expands the original mechanism test
without changing the claim into a real-robot or raw-perception claim. Outputs
are compact CSV summaries under results/full_scale rather than raw trajectories.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import run_simulation as base


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "full_scale"
FIG_OUT = OUT / "figures"
PAPER_FIG = ROOT / "paper" / "figures"
PROGRESS = OUT / "progress.txt"

CLASS_NAMES = base.CLASS_NAMES
CLASS_AFFORDANCE = base.CLASS_AFFORDANCE
N_CLASSES = len(CLASS_NAMES)
N_CONTACTS = base.N_CONTACTS
OBJECT_RADIUS = base.OBJECT_RADIUS
REACH_MIN = base.REACH_MIN
REACH_MAX = base.REACH_MAX
APPROACH_DOT_MIN = base.APPROACH_DOT_MIN
SWEEP_RADIUS = base.SWEEP_RADIUS


@dataclass(frozen=True)
class Scenario:
    name: str
    focus_mean: float
    focus_prob: float
    focus_std: float
    radius_low: float
    radius_high: float
    clutter_counts: Tuple[int, ...]
    clutter_probs: Tuple[float, ...]
    block_bias: float
    obstacle_radius_low: float = 0.045
    obstacle_radius_high: float = 0.105


SCENARIOS: Dict[str, Scenario] = {
    "left_light": Scenario(
        "left_light",
        math.pi,
        0.82,
        0.48,
        0.72,
        1.18,
        (0, 1, 2),
        (0.50, 0.34, 0.16),
        0.18,
    ),
    "left_medium": Scenario(
        "left_medium",
        math.pi,
        0.70,
        0.62,
        0.68,
        1.25,
        (0, 1, 2, 3),
        (0.30, 0.30, 0.25, 0.15),
        0.24,
    ),
    "right_mild": Scenario(
        "right_mild",
        0.0,
        0.62,
        0.74,
        0.68,
        1.25,
        (0, 1, 2, 3),
        (0.25, 0.32, 0.28, 0.15),
        0.26,
    ),
    "right_medium": Scenario(
        "right_medium",
        0.0,
        0.82,
        0.52,
        0.66,
        1.30,
        (1, 2, 3, 4, 5),
        (0.12, 0.22, 0.27, 0.24, 0.15),
        0.34,
    ),
    "right_heavy": Scenario(
        "right_heavy",
        0.0,
        0.90,
        0.42,
        0.61,
        1.35,
        (2, 3, 4, 5, 6, 7),
        (0.10, 0.18, 0.24, 0.23, 0.17, 0.08),
        0.46,
        0.055,
        0.125,
    ),
    "uniform_medium": Scenario(
        "uniform_medium",
        0.0,
        0.00,
        1.0,
        0.66,
        1.30,
        (0, 1, 2, 3, 4),
        (0.18, 0.24, 0.26, 0.20, 0.12),
        0.28,
    ),
}


SHIFT_PAIRS: Tuple[Tuple[str, str, str], ...] = (
    ("iid_left_light", "left_light", "left_light"),
    ("mild_cross", "left_light", "right_mild"),
    ("medium_cross", "left_light", "right_medium"),
    ("severe_cross", "left_light", "right_heavy"),
    ("reverse_heavy_to_light", "right_heavy", "left_light"),
)


def log(message: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(message + "\n")
    print(message, flush=True)


def ensure_dirs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FIG_OUT.mkdir(parents=True, exist_ok=True)
    PAPER_FIG.mkdir(parents=True, exist_ok=True)


def angle_wrap_scalar(theta: float) -> float:
    return float((theta + math.pi) % (2 * math.pi) - math.pi)


def sample_base_param(rng: np.random.Generator, scenario: Scenario) -> Tuple[float, float]:
    if rng.random() < scenario.focus_prob:
        theta = rng.normal(scenario.focus_mean, scenario.focus_std)
    else:
        theta = rng.uniform(-math.pi, math.pi)
    radius = rng.uniform(scenario.radius_low, scenario.radius_high)
    return angle_wrap_scalar(float(theta)), float(radius)


def line_clearance(a: np.ndarray, b: np.ndarray, center: np.ndarray, radius: float, sweep_radius: float) -> float:
    ab = b - a
    denom = float(np.dot(ab, ab))
    if denom <= 1e-12:
        return float("inf")
    t = float(np.clip(np.dot(center - a, ab) / denom, 0.0, 1.0))
    closest = a + t * ab
    return float(np.linalg.norm(closest - center) - radius - sweep_radius)


def sample_obstacles_param(
    rng: np.random.Generator,
    scenario: Scenario,
    base_xy: np.ndarray,
    contact: np.ndarray,
    clutter_multiplier: float = 1.0,
) -> List[Tuple[np.ndarray, float]]:
    count = int(rng.choice(scenario.clutter_counts, p=np.array(scenario.clutter_probs, dtype=float)))
    count = int(max(0, round(count * clutter_multiplier)))
    obstacles: List[Tuple[np.ndarray, float]] = []
    for _ in range(count):
        radius = float(rng.uniform(scenario.obstacle_radius_low, scenario.obstacle_radius_high))
        if rng.random() < scenario.block_bias:
            t = float(rng.uniform(0.18, 0.86))
            center = contact + t * (base_xy - contact)
            normal = np.array([-(base_xy - contact)[1], (base_xy - contact)[0]])
            norm = float(np.linalg.norm(normal)) + 1e-9
            center = center + normal / norm * rng.normal(0, 0.045)
        else:
            theta = float(rng.uniform(-math.pi, math.pi))
            rad = float(rng.uniform(0.15, 1.08))
            center = np.array([rad * math.cos(theta), rad * math.sin(theta)])
        obstacles.append((center, radius))
    return obstacles


def compute_access_param(
    base_xy: np.ndarray,
    contact: np.ndarray,
    normal: np.ndarray,
    obstacles: List[Tuple[np.ndarray, float]],
    reach_min: float = REACH_MIN,
    reach_max: float = REACH_MAX,
    approach_min: float = APPROACH_DOT_MIN,
    sweep_radius: float = SWEEP_RADIUS,
) -> Tuple[bool, float, float, bool, float]:
    vec = base_xy - contact
    distance = float(np.linalg.norm(vec))
    unit = vec / (distance + 1e-9)
    approach_dot = float(np.dot(unit, normal))
    clearances = [line_clearance(contact, base_xy, center, radius, sweep_radius) for center, radius in obstacles]
    clutter_margin = min(clearances) if clearances else 1.0
    blocked = bool(clutter_margin <= 0.0)
    reachable = reach_min <= distance <= reach_max
    access = reachable and approach_dot >= approach_min and not blocked
    reach_margin = min(distance - reach_min, reach_max - distance)
    approach_margin = approach_dot - approach_min
    margin = float(min(reach_margin, approach_margin, clutter_margin))
    return bool(access), distance, approach_dot, blocked, margin


def make_dataset(
    seed: int,
    n: int,
    scenario_name: str,
    class_affordance: np.ndarray | None = None,
    violation_strength: float = 0.0,
    reach_scale: float = 1.0,
    approach_min: float = APPROACH_DOT_MIN,
    clutter_multiplier: float = 1.0,
) -> base.Dataset:
    rng = np.random.default_rng(seed)
    scenario = SCENARIOS[scenario_name]
    angles, cls_by_site, contact_pts = base.contact_geometry()
    affordance = np.array(CLASS_AFFORDANCE if class_affordance is None else class_affordance, dtype=float)
    rows: Dict[str, List] = {
        "site": [],
        "cls": [],
        "site_angle": [],
        "base_theta": [],
        "base_r": [],
        "base_xy": [],
        "distance": [],
        "approach_dot": [],
        "clutter_count": [],
        "blocked": [],
        "access": [],
        "true_affordance": [],
        "success_prob": [],
        "y": [],
    }
    reach_mid = 0.5 * (REACH_MIN + REACH_MAX)
    reach_half = 0.5 * (REACH_MAX - REACH_MIN) * reach_scale
    reach_min = max(0.05, reach_mid - reach_half)
    reach_max = reach_mid + reach_half
    for _ in range(n):
        site = int(rng.integers(0, N_CONTACTS))
        cls = int(cls_by_site[site])
        contact = contact_pts[site]
        normal = contact / (np.linalg.norm(contact) + 1e-9)
        base_theta, base_r = sample_base_param(rng, scenario)
        base_xy = np.array([base_r * math.cos(base_theta), base_r * math.sin(base_theta)])
        obstacles = sample_obstacles_param(rng, scenario, base_xy, contact, clutter_multiplier=clutter_multiplier)
        access, distance, approach_dot, blocked, _margin = compute_access_param(
            base_xy,
            contact,
            normal,
            obstacles,
            reach_min=reach_min,
            reach_max=reach_max,
            approach_min=approach_min,
        )
        intrinsic = float(affordance[cls])
        if violation_strength > 0:
            # Negative-control mode: the contact is not conserved. A contact
            # keeps its normal affordance from left-side approaches but trends
            # toward the complementary affordance from right-side approaches.
            # This makes train-left/test-right transport intentionally invalid.
            side_weight = 1.0 / (1.0 + math.exp(-7.0 * float(base_xy[0])))
            nonconserved = (1.0 - side_weight) * intrinsic + side_weight * (1.0 - intrinsic)
            intrinsic = float((1.0 - violation_strength) * intrinsic + violation_strength * nonconserved)
            intrinsic = float(np.clip(intrinsic, 0.02, 0.98))
        success_prob = float((intrinsic if access else 0.0) + (0.015 if not access else 0.0))
        success_prob = float(np.clip(success_prob, 0.001, 0.999))
        y = int(rng.random() < success_prob)
        rows["site"].append(site)
        rows["cls"].append(cls)
        rows["site_angle"].append(float(angles[site]))
        rows["base_theta"].append(base_theta)
        rows["base_r"].append(base_r)
        rows["base_xy"].append(base_xy)
        rows["distance"].append(distance)
        rows["approach_dot"].append(approach_dot)
        rows["clutter_count"].append(len(obstacles))
        rows["blocked"].append(blocked)
        rows["access"].append(access)
        rows["true_affordance"].append(intrinsic)
        rows["success_prob"].append(success_prob)
        rows["y"].append(y)
    return base.Dataset(
        site=np.array(rows["site"], dtype=int),
        cls=np.array(rows["cls"], dtype=int),
        site_angle=np.array(rows["site_angle"], dtype=float),
        base_theta=np.array(rows["base_theta"], dtype=float),
        base_r=np.array(rows["base_r"], dtype=float),
        base_xy=np.vstack(rows["base_xy"]).astype(float),
        distance=np.array(rows["distance"], dtype=float),
        approach_dot=np.array(rows["approach_dot"], dtype=float),
        clutter_count=np.array(rows["clutter_count"], dtype=int),
        blocked=np.array(rows["blocked"], dtype=bool),
        access=np.array(rows["access"], dtype=bool),
        true_affordance=np.array(rows["true_affordance"], dtype=float),
        success_prob=np.array(rows["success_prob"], dtype=float),
        y=np.array(rows["y"], dtype=int),
    )


def replace_access(data: base.Dataset, access: np.ndarray) -> base.Dataset:
    return base.Dataset(
        site=data.site,
        cls=data.cls,
        site_angle=data.site_angle,
        base_theta=data.base_theta,
        base_r=data.base_r,
        base_xy=data.base_xy,
        distance=data.distance,
        approach_dot=data.approach_dot,
        clutter_count=data.clutter_count,
        blocked=data.blocked,
        access=access.astype(bool),
        true_affordance=data.true_affordance,
        success_prob=data.success_prob,
        y=data.y,
    )


def replace_cls(data: base.Dataset, cls: np.ndarray) -> base.Dataset:
    return base.Dataset(
        site=data.site,
        cls=cls.astype(int),
        site_angle=data.site_angle,
        base_theta=data.base_theta,
        base_r=data.base_r,
        base_xy=data.base_xy,
        distance=data.distance,
        approach_dot=data.approach_dot,
        clutter_count=data.clutter_count,
        blocked=data.blocked,
        access=data.access,
        true_affordance=data.true_affordance,
        success_prob=data.success_prob,
        y=data.y,
    )


def fit_caq_alpha(train: base.Dataset, alpha: float = 3.0) -> Dict[str, np.ndarray]:
    accessible = train.access
    global_mean = float(train.y[accessible].mean()) if accessible.any() else float(train.y.mean())
    z = np.full(N_CLASSES, global_mean, dtype=float)
    counts = np.zeros(N_CLASSES, dtype=int)
    for c in range(N_CLASSES):
        mask = accessible & (train.cls == c)
        counts[c] = int(mask.sum())
        if counts[c] > 0:
            z[c] = float((train.y[mask].sum() + alpha * global_mean) / (counts[c] + alpha))
    return {"z": z, "counts": counts, "global": np.array([global_mean])}


def fit_oracle_gate_class_mean(train: base.Dataset) -> Dict[str, np.ndarray]:
    return fit_caq_alpha(train, alpha=0.0)


def predict_oracle_intrinsic(data: base.Dataset) -> np.ndarray:
    return np.clip(data.true_affordance * data.access.astype(float) + 0.01 * (~data.access).astype(float), 1e-4, 1 - 1e-4)


def fit_context_table_bins(train: base.Dataset, bins: int = 8) -> Dict[str, object]:
    tb = theta_bin_custom(train.base_theta, bins)
    cb = base.clutter_bin(train.clutter_count)
    table: Dict[Tuple[int, int, int], List[int]] = {}
    for c, t, k, y in zip(train.cls, tb, cb, train.y):
        table.setdefault((int(c), int(t), int(k)), []).append(int(y))
    means = {key: float(np.mean(vals)) for key, vals in table.items()}
    class_mean = base.fit_object_only(train)
    return {"means": means, "class_mean": class_mean, "global": float(train.y.mean()), "bins": bins}


def predict_context_table_bins(model: Dict[str, object], data: base.Dataset) -> np.ndarray:
    bins = int(model["bins"])
    tb = theta_bin_custom(data.base_theta, bins)
    cb = base.clutter_bin(data.clutter_count)
    means = model["means"]
    class_mean = model["class_mean"]
    global_mean = float(model["global"])
    assert isinstance(means, dict)
    assert isinstance(class_mean, np.ndarray)
    preds = np.zeros(len(data.y), dtype=float)
    for i, (c, t, k) in enumerate(zip(data.cls, tb, cb)):
        preds[i] = means.get((int(c), int(t), int(k)), 0.70 * float(class_mean[int(c)]) + 0.30 * global_mean)
    return np.clip(preds, 1e-4, 1 - 1e-4)


def theta_bin_custom(theta: np.ndarray, bins: int) -> np.ndarray:
    return np.floor((theta + np.pi) / (2 * np.pi) * bins).astype(int).clip(0, bins - 1)


def one_hot(values: np.ndarray, depth: int) -> np.ndarray:
    out = np.zeros((len(values), depth), dtype=float)
    out[np.arange(len(values)), values.astype(int)] = 1.0
    return out


def logistic_features(data: base.Dataset, interactions: bool = False) -> np.ndarray:
    cls_oh = one_hot(data.cls, N_CLASSES)
    base_cols = [
        cls_oh,
        np.cos(data.site_angle)[:, None],
        np.sin(data.site_angle)[:, None],
        np.cos(data.base_theta)[:, None],
        np.sin(data.base_theta)[:, None],
        data.base_r[:, None],
        data.distance[:, None],
        data.approach_dot[:, None],
        (data.clutter_count / 7.0)[:, None],
        data.blocked.astype(float)[:, None],
        data.access.astype(float)[:, None],
    ]
    if interactions:
        base_cols.append(cls_oh * data.access.astype(float)[:, None])
        base_cols.append(cls_oh * np.cos(data.base_theta)[:, None])
        base_cols.append(cls_oh * np.sin(data.base_theta)[:, None])
    return np.column_stack(base_cols)


def fit_logistic_generic(train: base.Dataset, interactions: bool = False, steps: int = 24) -> Dict[str, np.ndarray | bool]:
    X = logistic_features(train, interactions=interactions)
    y = train.y.astype(float)
    mean = X.mean(axis=0)
    std = X.std(axis=0) + 1e-6
    Xn = (X - mean) / std
    Xb = np.column_stack([np.ones(len(Xn)), Xn])
    w = np.zeros(Xb.shape[1], dtype=float)
    l2 = 2e-3
    for _ in range(steps):
        p = 1.0 / (1.0 + np.exp(-np.clip(Xb @ w, -50, 50)))
        weights = np.clip(p * (1.0 - p), 1e-5, None)
        grad = Xb.T @ (p - y)
        grad[1:] += l2 * len(y) * w[1:]
        hessian = (Xb.T * weights) @ Xb
        hessian[1:, 1:] += np.eye(Xb.shape[1] - 1) * l2 * len(y)
        try:
            step = np.linalg.solve(hessian, grad)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(hessian, grad, rcond=None)[0]
        step_norm = float(np.linalg.norm(step))
        if step_norm > 8.0:
            step = step * (8.0 / step_norm)
        w -= step
        if float(np.linalg.norm(step)) < 1e-6:
            break
    return {"w": w, "mean": mean, "std": std, "interactions": interactions}


def predict_logistic_generic(model: Dict[str, np.ndarray | bool], data: base.Dataset) -> np.ndarray:
    X = logistic_features(data, interactions=bool(model["interactions"]))
    mean = model["mean"]
    std = model["std"]
    w = model["w"]
    assert isinstance(mean, np.ndarray)
    assert isinstance(std, np.ndarray)
    assert isinstance(w, np.ndarray)
    Xn = (X - mean) / std
    Xb = np.column_stack([np.ones(len(Xn)), Xn])
    return np.clip(1.0 / (1.0 + np.exp(-np.clip(Xb @ w, -50, 50))), 1e-4, 1 - 1e-4)


def calibration_stats(y: np.ndarray, p: np.ndarray, bins: int = 10) -> Dict[str, float]:
    y = y.astype(float)
    p = np.clip(p.astype(float), 1e-4, 1 - 1e-4)
    edges = np.linspace(0.0, 1.0, bins + 1)
    ece = 0.0
    xs: List[float] = []
    ys: List[float] = []
    weights: List[float] = []
    for i in range(bins):
        lo = edges[i]
        hi = edges[i + 1]
        mask = (p >= lo) & (p <= hi if i == bins - 1 else p < hi)
        if not mask.any():
            continue
        conf = float(p[mask].mean())
        acc = float(y[mask].mean())
        w = float(mask.mean())
        ece += w * abs(conf - acc)
        xs.append(conf)
        ys.append(acc)
        weights.append(float(mask.sum()))
    if len(xs) >= 2:
        x = np.array(xs)
        yb = np.array(ys)
        wt = np.array(weights)
        xbar = float(np.average(x, weights=wt))
        ybar = float(np.average(yb, weights=wt))
        denom = float(np.sum(wt * (x - xbar) ** 2))
        slope = float(np.sum(wt * (x - xbar) * (yb - ybar)) / denom) if denom > 1e-12 else 0.0
    else:
        slope = 0.0
    return {"ece": float(ece), "reliability_slope": slope}


def evaluate_full(name: str, data: base.Dataset, pred: np.ndarray) -> Dict[str, float | str]:
    out = base.evaluate(name, data, pred)
    cal = calibration_stats(data.y, pred)
    out.update(cal)
    out["mean_prediction"] = float(np.mean(pred))
    out["positive_rate"] = float(np.mean(data.y))
    out["access_rate"] = float(np.mean(data.access))
    return out


def fit_predict_all(train: base.Dataset, test: base.Dataset, logistic_steps: int) -> Dict[str, np.ndarray]:
    caq = fit_caq_alpha(train, alpha=3.0)
    caq_strong = fit_caq_alpha(train, alpha=20.0)
    object_only = base.fit_object_only(train)
    access_only = base.fit_access_only(train)
    context = fit_context_table_bins(train, bins=8)
    logistic = fit_logistic_generic(train, interactions=False, steps=logistic_steps)
    interaction = fit_logistic_generic(train, interactions=True, steps=logistic_steps)
    oracle_gate = fit_oracle_gate_class_mean(train)
    return {
        "conserved_quotient": base.predict_caq(caq, test),
        "caq_strong_shrinkage": base.predict_caq(caq_strong, test),
        "object_only": base.predict_object_only(object_only, test),
        "access_only": base.predict_access_only(access_only, test),
        "context_table": predict_context_table_bins(context, test),
        "monolithic_logistic": predict_logistic_generic(logistic, test),
        "interaction_logistic": predict_logistic_generic(interaction, test),
        "oracle_gate_class_mean": base.predict_caq(oracle_gate, test),
        "oracle_intrinsic": predict_oracle_intrinsic(test),
    }


def write_csv(rows: List[Dict[str, float | str]], path: Path) -> pd.DataFrame:
    ensure_dirs()
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return df


def run_main(seed_scale: int, logistic_steps: int) -> None:
    rows: List[Dict[str, float | str]] = []
    for shift_name, train_scenario, test_scenario in SHIFT_PAIRS:
        for seed in range(seed_scale):
            train = make_dataset(100_000 + 1_000 * seed + len(shift_name), 1000, train_scenario)
            test = make_dataset(200_000 + 1_000 * seed + len(shift_name), 3000, test_scenario)
            preds = fit_predict_all(train, test, logistic_steps=logistic_steps)
            for model, pred in preds.items():
                rows.append(
                    {
                        "suite": "main_shift",
                        "shift": shift_name,
                        "train_scenario": train_scenario,
                        "test_scenario": test_scenario,
                        "seed": seed,
                        "n_train": len(train.y),
                        "n_test": len(test.y),
                        **evaluate_full(model, test, pred),
                    }
                )
        log(f"main_shift {shift_name} complete")
    write_csv(rows, OUT / "main_shift_metrics.csv")


def apply_access_error(data: base.Dataset, seed: int, mode: str, rate: float) -> base.Dataset:
    rng = np.random.default_rng(seed)
    access = data.access.copy()
    if rate <= 0:
        return replace_access(data, access)
    if mode == "symmetric_random":
        flips = rng.random(len(access)) < rate
    elif mode == "false_access_only":
        flips = (~access) & (rng.random(len(access)) < rate)
    elif mode == "false_blocked_only":
        flips = access & (rng.random(len(access)) < rate)
    elif mode == "structured_margin":
        reach_margin = np.minimum(data.distance - REACH_MIN, REACH_MAX - data.distance)
        approach_margin = data.approach_dot - APPROACH_DOT_MIN
        clutter_penalty = np.where(data.blocked, -0.02, 0.12)
        margin = np.minimum(np.minimum(reach_margin, approach_margin), clutter_penalty)
        near = np.exp(-np.abs(margin) / 0.08)
        prob = np.clip(rate * near / (near.mean() + 1e-9), 0.0, 0.85)
        flips = rng.random(len(access)) < prob
    else:
        raise ValueError(f"unknown access-error mode: {mode}")
    access[flips] = ~access[flips]
    return replace_access(data, access)


def run_access(seed_scale: int) -> None:
    rows: List[Dict[str, float | str]] = []
    modes = ("symmetric_random", "false_access_only", "false_blocked_only", "structured_margin")
    rates = (0.0, 0.02, 0.05, 0.10, 0.15, 0.20, 0.30)
    for seed in range(seed_scale):
        train = make_dataset(310_000 + seed, 1000, "left_light")
        test = make_dataset(320_000 + seed, 3200, "right_medium")
        for mode in modes:
            for rate in rates:
                noisy_train = apply_access_error(train, 330_000 + seed, mode, rate)
                noisy_test = apply_access_error(test, 340_000 + seed, mode, rate)
                for model_name, alpha in (("conserved_quotient", 3.0), ("caq_strong_shrinkage", 20.0)):
                    caq = fit_caq_alpha(noisy_train, alpha=alpha)
                    pred = base.predict_caq(caq, noisy_test)
                    rows.append(
                        {
                            "suite": "access_error_taxonomy",
                            "mode": mode,
                            "rate": rate,
                            "seed": seed,
                            "n_train": len(train.y),
                            "n_test": len(test.y),
                            **evaluate_full(model_name, test, pred),
                        }
                    )
        log(f"access_error seed={seed} complete")
    write_csv(rows, OUT / "access_error_taxonomy.csv")


def corrupt_classes(data: base.Dataset, seed: int, rate: float, mode: str) -> base.Dataset:
    rng = np.random.default_rng(seed)
    cls = data.cls.copy()
    if rate <= 0:
        return replace_cls(data, cls)
    mask = rng.random(len(cls)) < rate
    if mode == "random_site":
        noise = rng.integers(1, N_CLASSES, size=int(mask.sum()))
        cls[mask] = (cls[mask] + noise) % N_CLASSES
    elif mode == "handle_slot_swap":
        swap = mask & ((cls == 0) | (cls == 1))
        cls[swap] = np.where(cls[swap] == 0, 1, 0)
    else:
        raise ValueError(f"unknown class-corruption mode: {mode}")
    return replace_cls(data, cls)


def run_correspondence(seed_scale: int, logistic_steps: int) -> None:
    rows: List[Dict[str, float | str]] = []
    modes = ("random_site", "handle_slot_swap")
    rates = (0.0, 0.02, 0.05, 0.10, 0.20, 0.30)
    for seed in range(seed_scale):
        train_true = make_dataset(410_000 + seed, 1000, "left_light")
        test_true = make_dataset(420_000 + seed, 3200, "right_medium")
        for mode in modes:
            for rate in rates:
                train = corrupt_classes(train_true, 430_000 + seed, rate, mode)
                test = corrupt_classes(test_true, 440_000 + seed, rate, mode)
                caq = fit_caq_alpha(train, alpha=3.0)
                pred_caq = base.predict_caq(caq, test)
                rows.append(
                    {
                        "suite": "correspondence_stress",
                        "mode": mode,
                        "rate": rate,
                        "seed": seed,
                        **evaluate_full("conserved_quotient", test_true, pred_caq),
                    }
                )
                if rate in (0.0, 0.10, 0.30):
                    interaction = fit_logistic_generic(train, interactions=True, steps=logistic_steps)
                    pred_log = predict_logistic_generic(interaction, test)
                    rows.append(
                        {
                            "suite": "correspondence_stress",
                            "mode": mode,
                            "rate": rate,
                            "seed": seed,
                            **evaluate_full("interaction_logistic", test_true, pred_log),
                        }
                    )
        log(f"correspondence seed={seed} complete")
    write_csv(rows, OUT / "correspondence_stress.csv")


def run_support(seed_scale: int, logistic_steps: int) -> None:
    rows: List[Dict[str, float | str]] = []
    train_sizes = (80, 160, 320, 640, 1280, 2560)
    context_bins = (4, 8, 12)
    for n_train in train_sizes:
        for seed in range(seed_scale):
            train = make_dataset(510_000 + seed + n_train, n_train, "left_light")
            test = make_dataset(520_000 + seed + n_train, 3000, "right_medium")
            caq = fit_caq_alpha(train, alpha=3.0)
            object_only = base.fit_object_only(train)
            access_only = base.fit_access_only(train)
            shared_preds = {
                "conserved_quotient": base.predict_caq(caq, test),
                "object_only": base.predict_object_only(object_only, test),
                "access_only": base.predict_access_only(access_only, test),
            }
            logistic_pred: np.ndarray | None = None
            if n_train in (80, 320, 1280, 2560):
                logistic = fit_logistic_generic(train, interactions=False, steps=logistic_steps)
                logistic_pred = predict_logistic_generic(logistic, test)
            for bins in context_bins:
                context = fit_context_table_bins(train, bins=bins)
                preds = dict(shared_preds)
                preds["context_table"] = predict_context_table_bins(context, test)
                if bins == 8 and logistic_pred is not None:
                    preds["monolithic_logistic"] = logistic_pred
                for model, pred in preds.items():
                    rows.append(
                        {
                            "suite": "support_burden",
                            "seed": seed,
                            "n_train": n_train,
                            "n_test": len(test.y),
                            "context_bins": bins,
                            **evaluate_full(model, test, pred),
                        }
                    )
        log(f"support n_train={n_train} complete")
    write_csv(rows, OUT / "support_burden.csv")


def residual_auc(labels: np.ndarray, scores: np.ndarray) -> float:
    return base.auc_score(labels.astype(int), scores.astype(float))


def run_residual(seed_scale: int) -> None:
    rows: List[Dict[str, float | str]] = []
    magnitudes = (0.0, 0.10, 0.20, 0.35, 0.55)
    for seed in range(seed_scale):
        train = make_dataset(610_000 + seed, 1100, "left_light")
        caq = fit_caq_alpha(train, alpha=3.0)
        for changed_class in range(N_CLASSES):
            for magnitude in magnitudes:
                changed_aff = CLASS_AFFORDANCE.copy()
                changed_aff[changed_class] = float(np.clip(changed_aff[changed_class] - magnitude, 0.02, 0.98))
                changed = make_dataset(620_000 + seed + 101 * changed_class, 1400, "right_medium", class_affordance=changed_aff)
                residuals: List[float] = []
                supports: List[int] = []
                for c in range(N_CLASSES):
                    mask = changed.access & (changed.cls == c)
                    supports.append(int(mask.sum()))
                    if mask.any():
                        residuals.append(abs(float(changed.y[mask].mean()) - float(caq["z"][c])))
                    else:
                        residuals.append(0.0)
                labels = np.zeros(N_CLASSES, dtype=int)
                labels[changed_class] = int(magnitude > 0)
                auc = residual_auc(labels, np.array(residuals)) if magnitude > 0 else float("nan")
                detected = int(np.argmax(residuals) == changed_class) if magnitude > 0 else 0
                for c in range(N_CLASSES):
                    rows.append(
                        {
                            "suite": "residual_diagnostics",
                            "seed": seed,
                            "changed_class": str(CLASS_NAMES[changed_class]),
                            "magnitude": magnitude,
                            "class": str(CLASS_NAMES[c]),
                            "is_changed": int(c == changed_class and magnitude > 0),
                            "residual": residuals[c],
                            "accessible_support": supports[c],
                            "residual_auc": auc,
                            "detected_changed_class": detected,
                        }
                    )
        log(f"residual seed={seed} complete")
    write_csv(rows, OUT / "residual_diagnostics.csv")


def run_geometry(seed_scale: int, logistic_steps: int) -> None:
    rows: List[Dict[str, float | str]] = []
    reach_scales = (0.72, 0.90, 1.08, 1.24)
    clutter_multipliers = (0.65, 1.0, 1.35, 1.70)
    for reach_scale in reach_scales:
        for clutter_mult in clutter_multipliers:
            for seed in range(seed_scale):
                train = make_dataset(710_000 + seed, 800, "left_light", reach_scale=reach_scale, clutter_multiplier=clutter_mult)
                test = make_dataset(720_000 + seed, 1800, "right_medium", reach_scale=reach_scale, clutter_multiplier=clutter_mult)
                caq = fit_caq_alpha(train, alpha=3.0)
                access_only = base.fit_access_only(train)
                preds = {
                    "conserved_quotient": base.predict_caq(caq, test),
                    "access_only": base.predict_access_only(access_only, test),
                    "oracle_intrinsic": predict_oracle_intrinsic(test),
                }
                if reach_scale in (0.72, 1.08) and clutter_mult in (0.65, 1.35):
                    logistic = fit_logistic_generic(train, interactions=True, steps=logistic_steps)
                    preds["interaction_logistic"] = predict_logistic_generic(logistic, test)
                for model, pred in preds.items():
                    rows.append(
                        {
                            "suite": "geometry_sensitivity",
                            "seed": seed,
                            "reach_scale": reach_scale,
                            "clutter_multiplier": clutter_mult,
                            **evaluate_full(model, test, pred),
                        }
                    )
            log(f"geometry reach={reach_scale:.2f} clutter={clutter_mult:.2f} complete")
    write_csv(rows, OUT / "geometry_sensitivity.csv")


def run_negative(seed_scale: int, logistic_steps: int) -> None:
    rows: List[Dict[str, float | str]] = []
    strengths = (0.0, 0.25, 0.50, 0.75, 1.00)
    for strength in strengths:
        for seed in range(seed_scale):
            train = make_dataset(810_000 + seed, 1200, "left_light", violation_strength=strength)
            test = make_dataset(820_000 + seed, 3200, "right_medium", violation_strength=strength)
            caq = fit_caq_alpha(train, alpha=3.0)
            context = fit_context_table_bins(train, bins=8)
            interaction = fit_logistic_generic(train, interactions=True, steps=logistic_steps)
            logistic = fit_logistic_generic(train, interactions=False, steps=logistic_steps)
            preds = {
                "conserved_quotient": base.predict_caq(caq, test),
                "context_table": predict_context_table_bins(context, test),
                "monolithic_logistic": predict_logistic_generic(logistic, test),
                "interaction_logistic": predict_logistic_generic(interaction, test),
                "oracle_intrinsic": predict_oracle_intrinsic(test),
            }
            for model, pred in preds.items():
                rows.append(
                    {
                        "suite": "negative_control",
                        "seed": seed,
                        "violation_strength": strength,
                        **evaluate_full(model, test, pred),
                    }
                )
        log(f"negative_control strength={strength:.2f} complete")
    write_csv(rows, OUT / "negative_controls.csv")


def agg_mean_sem(df: pd.DataFrame, by: Sequence[str], metrics: Sequence[str]) -> pd.DataFrame:
    grouped = df.groupby(list(by))[list(metrics)].agg(["mean", "sem"]).reset_index()
    grouped.columns = ["_".join([str(x) for x in col if str(x)]) for col in grouped.columns.to_flat_index()]
    return grouped


def make_main_leaderboard() -> pd.DataFrame:
    frames = []
    main_path = OUT / "main_shift_metrics.csv"
    if main_path.exists():
        main = pd.read_csv(main_path)
        frames.append(main[main["shift"] == "medium_cross"].assign(report_context="medium_cross"))
        frames.append(main.assign(report_context="all_main_shifts"))
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    metrics = ["brier", "log_loss", "accuracy", "f1", "auc", "ece", "blocked_false_positive_rate", "affordance_loss_rate"]
    leader = agg_mean_sem(df, ["report_context", "model"], metrics)
    leader.to_csv(OUT / "leaderboard.csv", index=False)
    return leader


def plot_bar_metric(df: pd.DataFrame, path: Path, title: str, metric: str, lower: bool = True) -> None:
    order = (
        df.groupby("model")[metric]
        .mean()
        .sort_values(ascending=lower)
        .index.tolist()
    )
    labels = [m.replace("_", "\n") for m in order]
    means = [float(df.loc[df["model"] == m, metric].mean()) for m in order]
    sems = [float(df.loc[df["model"] == m, metric].sem()) for m in order]
    colors = ["#2f6f73", "#536c9e", "#9a6b3f", "#a1424a", "#6c6f7d", "#7c5c92", "#3d7f4f", "#8c5b4c", "#4f6ca8"]
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    ax.bar(np.arange(len(order)), means, yerr=np.array(sems) * 1.96, capsize=3, color=colors[: len(order)])
    ax.set_xticks(np.arange(len(order)), labels, rotation=0)
    ax.set_ylabel(metric.replace("_", " "))
    ax.set_title(title)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def plot_line_group(
    df: pd.DataFrame,
    x_col: str,
    group_col: str,
    y_col: str,
    path: Path,
    title: str,
    xlabel: str,
    ylabel: str,
) -> None:
    fig, ax = plt.subplots(figsize=(7.0, 4.7))
    colors = ["#2f6f73", "#a1424a", "#536c9e", "#9a6b3f", "#6c6f7d", "#7c5c92"]
    for idx, (name, sub) in enumerate(df.groupby(group_col)):
        grouped = sub.groupby(x_col)[y_col].agg(["mean", "sem"]).reset_index()
        x = grouped[x_col].to_numpy(dtype=float)
        y = grouped["mean"].to_numpy(dtype=float)
        err = 1.96 * grouped["sem"].fillna(0).to_numpy(dtype=float)
        ax.errorbar(x, y, yerr=err, marker="o", lw=2, capsize=3, label=str(name).replace("_", " "), color=colors[idx % len(colors)])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def plot_heatmap(df: pd.DataFrame, path: Path) -> None:
    sub = df[df["model"] == "conserved_quotient"]
    pivot = sub.pivot_table(index="reach_scale", columns="clutter_multiplier", values="brier", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(6.2, 4.8))
    im = ax.imshow(pivot.to_numpy(dtype=float), aspect="auto", cmap="viridis")
    ax.set_xticks(np.arange(len(pivot.columns)), [f"{x:.2f}" for x in pivot.columns])
    ax.set_yticks(np.arange(len(pivot.index)), [f"{x:.2f}" for x in pivot.index])
    ax.set_xlabel("clutter multiplier")
    ax.set_ylabel("reach-annulus scale")
    ax.set_title("CAQ Brier across access geometry")
    fig.colorbar(im, ax=ax, label="Brier")
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def plot_reliability(df: pd.DataFrame, path: Path) -> None:
    # Reconstruct a compact reliability readout from mean prediction vs outcome.
    sub = df[df["shift"] == "medium_cross"]
    metrics = sub.groupby("model")[["ece", "brier", "log_loss"]].mean().sort_values("ece")
    fig, ax = plt.subplots(figsize=(7.0, 4.5))
    ax.scatter(metrics["brier"], metrics["ece"], s=85, color="#2f6f73")
    for model, row in metrics.iterrows():
        ax.text(float(row["brier"]) + 0.0004, float(row["ece"]), model.replace("_", " "), fontsize=8)
    ax.set_xlabel("Brier score")
    ax.set_ylabel("expected calibration error")
    ax.set_title("Calibration-sensitive error on medium shift")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def summarize(seed_scale: int) -> None:
    ensure_dirs()
    leader = make_main_leaderboard()
    figure_files: List[str] = []
    if (OUT / "main_shift_metrics.csv").exists():
        main = pd.read_csv(OUT / "main_shift_metrics.csv")
        medium = main[main["shift"] == "medium_cross"]
        plot_bar_metric(medium, FIG_OUT / "main_brier_leaderboard.png", "Medium-shift benchmark", "brier", lower=True)
        plot_bar_metric(medium, FIG_OUT / "main_calibration_leaderboard.png", "Calibration error on medium shift", "ece", lower=True)
        plot_reliability(main, FIG_OUT / "calibration_scatter.png")
        figure_files.extend(["main_brier_leaderboard.png", "main_calibration_leaderboard.png", "calibration_scatter.png"])
    if (OUT / "access_error_taxonomy.csv").exists():
        access = pd.read_csv(OUT / "access_error_taxonomy.csv")
        sub = access[access["model"] == "conserved_quotient"]
        plot_line_group(sub, "rate", "mode", "brier", FIG_OUT / "access_error_taxonomy.png", "Access-certificate error taxonomy", "gate error rate", "Brier")
        figure_files.append("access_error_taxonomy.png")
    if (OUT / "support_burden.csv").exists():
        support = pd.read_csv(OUT / "support_burden.csv")
        sub = support[(support["context_bins"] == 8) & support["model"].isin(["conserved_quotient", "context_table", "monolithic_logistic", "object_only", "access_only"])]
        plot_line_group(sub, "n_train", "model", "brier", FIG_OUT / "support_burden.png", "Support burden under shifted contexts", "training samples", "Brier")
        figure_files.append("support_burden.png")
    if (OUT / "correspondence_stress.csv").exists():
        corr = pd.read_csv(OUT / "correspondence_stress.csv")
        sub = corr[corr["model"] == "conserved_quotient"]
        plot_line_group(sub, "rate", "mode", "brier", FIG_OUT / "correspondence_stress.png", "Contact-correspondence stress", "class corruption rate", "Brier")
        figure_files.append("correspondence_stress.png")
    if (OUT / "residual_diagnostics.csv").exists():
        residual = pd.read_csv(OUT / "residual_diagnostics.csv")
        det = residual[residual["is_changed"] == 1].drop_duplicates(["seed", "changed_class", "magnitude"])
        plot_line_group(det, "magnitude", "changed_class", "detected_changed_class", FIG_OUT / "residual_detection.png", "Residual detection by change magnitude", "affordance drop", "top-residual detection rate")
        figure_files.append("residual_detection.png")
    if (OUT / "geometry_sensitivity.csv").exists():
        geom = pd.read_csv(OUT / "geometry_sensitivity.csv")
        plot_heatmap(geom, FIG_OUT / "geometry_sensitivity_heatmap.png")
        figure_files.append("geometry_sensitivity_heatmap.png")
    if (OUT / "negative_controls.csv").exists():
        neg = pd.read_csv(OUT / "negative_controls.csv")
        plot_line_group(neg, "violation_strength", "model", "brier", FIG_OUT / "negative_control.png", "When conservation is false", "violation strength", "Brier")
        figure_files.append("negative_control.png")
    for name in figure_files:
        shutil.copy2(FIG_OUT / name, PAPER_FIG / name)
    summaries: Dict[str, object] = {
        "seed_scale": seed_scale,
        "figure_files": figure_files,
        "csv_files": sorted(path.name for path in OUT.glob("*.csv")),
    }
    if not leader.empty:
        medium = leader[leader["report_context"] == "medium_cross"].copy()
        if not medium.empty:
            best_brier = medium.sort_values("brier_mean").iloc[0]
            best_auc = medium.sort_values("auc_mean", ascending=False).iloc[0]
            summaries["medium_best_brier_model"] = str(best_brier["model"])
            summaries["medium_best_brier"] = float(best_brier["brier_mean"])
            summaries["medium_best_auc_model"] = str(best_auc["model"])
            summaries["medium_best_auc"] = float(best_auc["auc_mean"])
    total_rows = 0
    total_eval_samples = 0
    for csv_path in OUT.glob("*.csv"):
        if csv_path.name == "leaderboard.csv":
            continue
        df = pd.read_csv(csv_path)
        total_rows += len(df)
        if "n_test" in df.columns:
            total_eval_samples += int(pd.to_numeric(df["n_test"], errors="coerce").fillna(0).sum())
    summaries["compact_metric_rows"] = total_rows
    summaries["evaluated_test_predictions_counting_models"] = total_eval_samples
    (OUT / "full_scale_summary.json").write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    write_markdown_summary(summaries)
    log("summarize complete")


def read_group_value(path: str, filters: Dict[str, object], metric: str) -> Tuple[float, float]:
    df = pd.read_csv(OUT / path)
    for key, value in filters.items():
        df = df[df[key] == value]
    return float(df[metric].mean()), float(df[metric].sem())


def write_markdown_summary(summary: Dict[str, object]) -> None:
    lines = [
        "# Full-Scale CAQ Results Summary",
        "",
        "The expanded suite is a synthetic mechanism study. It strengthens the CAQ claim only under the stated assumptions: known or accurate access gate, stable object/contact state, and available contact correspondence.",
        "",
        "## Artifacts",
    ]
    for csv_name in summary.get("csv_files", []):
        lines.append(f"- `results/full_scale/{csv_name}`")
    lines.extend(
        [
            "",
            "## Scale",
            f"- Seed scale: `{summary.get('seed_scale')}`.",
            f"- Compact metric rows: `{summary.get('compact_metric_rows')}`.",
            f"- Evaluated test predictions, counting model/suite evaluations: `{summary.get('evaluated_test_predictions_counting_models')}`.",
            "",
            "## Main Readout",
        ]
    )
    if "medium_best_brier_model" in summary:
        lines.append(f"- Best medium-shift Brier model: `{summary['medium_best_brier_model']}` with mean Brier `{float(summary['medium_best_brier']):.4f}`.")
        lines.append(f"- Best medium-shift AUC model: `{summary['medium_best_auc_model']}` with mean AUC `{float(summary['medium_best_auc']):.4f}`.")
    try:
        caq_brier, caq_brier_sem = read_group_value(
            "main_shift_metrics.csv", {"shift": "medium_cross", "model": "conserved_quotient"}, "brier"
        )
        int_brier, _ = read_group_value(
            "main_shift_metrics.csv", {"shift": "medium_cross", "model": "interaction_logistic"}, "brier"
        )
        ctx_brier, _ = read_group_value(
            "main_shift_metrics.csv", {"shift": "medium_cross", "model": "context_table"}, "brier"
        )
        oracle_brier, _ = read_group_value(
            "main_shift_metrics.csv", {"shift": "medium_cross", "model": "oracle_intrinsic"}, "brier"
        )
        lines.extend(
            [
                f"- Medium-shift CAQ Brier: `{caq_brier:.4f}` (SEM `{caq_brier_sem:.4f}`).",
                f"- Medium-shift interaction-logistic Brier: `{int_brier:.4f}`.",
                f"- Medium-shift context-table Brier: `{ctx_brier:.4f}`.",
                f"- Oracle-intrinsic Brier reference: `{oracle_brier:.4f}`.",
            ]
        )
    except Exception as exc:
        lines.append(f"- Main benchmark details unavailable: `{exc}`.")
    try:
        access = pd.read_csv(OUT / "access_error_taxonomy.csv")
        caq = access[access["model"] == "conserved_quotient"]
        base_brier = float(caq[(caq["mode"] == "symmetric_random") & (caq["rate"] == 0.0)]["brier"].mean())
        sym20 = float(caq[(caq["mode"] == "symmetric_random") & (caq["rate"] == 0.20)]["brier"].mean())
        fa20 = float(caq[(caq["mode"] == "false_access_only") & (caq["rate"] == 0.20)]["brier"].mean())
        fb20 = float(caq[(caq["mode"] == "false_blocked_only") & (caq["rate"] == 0.20)]["brier"].mean())
        lines.extend(
            [
                "",
                "## Access-Gate Stress",
                f"- Correct-gate CAQ Brier in taxonomy suite: `{base_brier:.4f}`.",
                f"- Symmetric 20% gate error CAQ Brier: `{sym20:.4f}`.",
                f"- False-access-only 20% error CAQ Brier: `{fa20:.4f}`.",
                f"- False-blocked-only 20% error CAQ Brier: `{fb20:.4f}`.",
            ]
        )
    except Exception as exc:
        lines.append(f"- Access taxonomy unavailable: `{exc}`.")
    try:
        support = pd.read_csv(OUT / "support_burden.csv")
        small = support[(support["n_train"] == 160) & (support["context_bins"] == 8)]
        caq_small = float(small[small["model"] == "conserved_quotient"]["brier"].mean())
        ctx_small = float(small[small["model"] == "context_table"]["brier"].mean())
        large = support[(support["n_train"] == 2560) & (support["context_bins"] == 8)]
        caq_large = float(large[large["model"] == "conserved_quotient"]["brier"].mean())
        ctx_large = float(large[large["model"] == "context_table"]["brier"].mean())
        lines.extend(
            [
                "",
                "## Support Burden",
                f"- At 160 training samples and 8 context bins, CAQ Brier is `{caq_small:.4f}` versus context table `{ctx_small:.4f}`.",
                f"- At 2560 training samples and 8 context bins, CAQ Brier is `{caq_large:.4f}` versus context table `{ctx_large:.4f}`.",
            ]
        )
    except Exception as exc:
        lines.append(f"- Support-burden details unavailable: `{exc}`.")
    try:
        neg = pd.read_csv(OUT / "negative_controls.csv")
        caq0 = float(neg[(neg["model"] == "conserved_quotient") & (neg["violation_strength"] == 0.0)]["brier"].mean())
        caq1 = float(neg[(neg["model"] == "conserved_quotient") & (neg["violation_strength"] == 1.0)]["brier"].mean())
        int1 = float(neg[(neg["model"] == "interaction_logistic") & (neg["violation_strength"] == 1.0)]["brier"].mean())
        lines.extend(
            [
                "",
                "## Negative Control",
                f"- CAQ Brier rises from `{caq0:.4f}` at conservation strength 0 violation to `{caq1:.4f}` at violation strength 1.",
                f"- Interaction logistic Brier at violation strength 1 is `{int1:.4f}`.",
            ]
        )
    except Exception as exc:
        lines.append(f"- Negative-control details unavailable: `{exc}`.")
    lines.extend(
        [
            "",
            "## Figures",
        ]
    )
    for fig_name in summary.get("figure_files", []):
        lines.append(f"- `paper/figures/{fig_name}`")
    lines.append("")
    (OUT / "full_scale_results_summary.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--suite",
        choices=("all", "main", "access", "correspondence", "support", "residual", "geometry", "negative", "summarize"),
        default="all",
    )
    parser.add_argument("--seed-scale", type=int, default=20)
    parser.add_argument("--logistic-steps", type=int, default=24)
    parser.add_argument("--fresh", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_dirs()
    if args.fresh and OUT.exists():
        for path in OUT.glob("*.csv"):
            path.unlink()
        if PROGRESS.exists():
            PROGRESS.unlink()
    log(f"full-scale suite={args.suite} seed_scale={args.seed_scale} logistic_steps={args.logistic_steps}")
    if args.suite in ("all", "main"):
        run_main(args.seed_scale, args.logistic_steps)
    if args.suite in ("all", "access"):
        run_access(args.seed_scale)
    if args.suite in ("all", "correspondence"):
        run_correspondence(args.seed_scale, args.logistic_steps)
    if args.suite in ("all", "support"):
        run_support(args.seed_scale, args.logistic_steps)
    if args.suite in ("all", "residual"):
        run_residual(args.seed_scale)
    if args.suite in ("all", "geometry"):
        run_geometry(args.seed_scale, args.logistic_steps)
    if args.suite in ("all", "negative"):
        run_negative(args.seed_scale, args.logistic_steps)
    if args.suite in ("all", "summarize"):
        summarize(args.seed_scale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
