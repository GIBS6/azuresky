#!/usr/bin/env python3
r"""
AzureSky Quality Management System — Laboratory Calculation Engine
Document ID: AS_CALC_WASH_01 Rev 01
Associated SOP: AS013IW Rev 02 (Float and Sink Analysis of Hard Coal)
Standards: ISO 7936:2022, ISO 1953:2025, ISO 1171, ISO 1928, ISO/IEC 17025:2017
Author: Gift Chisali — Laboratory Supervisor
Technical Review: S. Nyambi — Laboratory Manager
Location: c:\Projects\AzureSky\CWP-001\11_CALCULATIONS\AS_CALC_WASH_01.py

Purpose:
    Performs fully verified gravimetric mass-balance reconciliation, fractional
    yield normalization, cumulative floats/sinks quality calculations, reconstituted
    head ash/CV reconciliation, near-density material (NDM) index of difficulty,
    and Tromp partition curve cut-point determination (d50, Ep, I).
"""

import sys
import math
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class FractionInput:
    code: str
    lower_rd: Optional[float]  # None for floats of lowest RD
    upper_rd: Optional[float]  # None for sinks of highest RD
    dry_mass_g: float
    ash_pct: float
    moisture_pct: Optional[float] = None
    cv_mj_kg: Optional[float] = None


@dataclass
class FractionOutput:
    code: str
    rd_interval: str
    mid_rd: float
    dry_mass_g: float
    fractional_yield_pct: float
    ash_pct: float
    moisture_pct: Optional[float]
    cv_mj_kg: Optional[float]
    cum_floats_yield_pct: float
    cum_floats_ash_pct: float
    cum_floats_cv_mj_kg: Optional[float]
    cum_sinks_yield_pct: float
    cum_sinks_ash_pct: float
    cum_sinks_cv_mj_kg: Optional[float]


@dataclass
class QualityReconciliation:
    head_value: float
    reconstituted_value: float
    absolute_delta: float
    acceptance_tolerance: float
    status: str


@dataclass
class MassBalanceQC:
    feed_mass_g: float
    recovered_mass_g: float
    mass_loss_g: float
    mass_loss_pct: float
    target_limit_pct: float
    hard_limit_pct: float
    status: str  # "PASS (TARGET)", "CONDITIONAL PASS", "FAIL (NON-CONFORMANCE)"


@dataclass
class WashabilityReport:
    sample_id: str
    size_fraction: str
    mass_qc: MassBalanceQC
    ash_qc: Optional[QualityReconciliation]
    cv_qc: Optional[QualityReconciliation]
    fractions: List[FractionOutput]
    near_density_material: Dict[str, float]


def format_rd_label(lower: Optional[float], upper: Optional[float]) -> Tuple[str, float]:
    """Generates standard interval label and nominal midpoint RD."""
    if lower is None and upper is not None:
        return f"Floats < {upper:.2f}", upper - 0.05
    elif lower is not None and upper is None:
        return f"Sinks > {lower:.2f}", lower + 0.05
    elif lower is not None and upper is not None:
        return f"{lower:.2f} - {upper:.2f}", (lower + upper) / 2.0
    else:
        return "Unknown", 1.50


def compute_washability(
    sample_id: str,
    size_fraction: str,
    feed_mass_g: float,
    fractions: List[FractionInput],
    head_ash_pct: Optional[float] = None,
    head_cv_mj_kg: Optional[float] = None,
) -> WashabilityReport:
    """
    Core calculation engine executing ISO 7936:2022 washability math.
    """
    total_recovered_mass = sum(f.dry_mass_g for f in fractions)
    mass_loss_g = feed_mass_g - total_recovered_mass
    mass_loss_pct = (mass_loss_g / feed_mass_g) * 100.0 if feed_mass_g > 0 else 0.0

    # Mass balance QC gate (Target <= 1.0%, Hard limit <= 2.0%)
    if abs(mass_loss_pct) <= 1.0:
        mass_status = "PASS (TARGET)"
    elif abs(mass_loss_pct) <= 2.0:
        mass_status = "CONDITIONAL PASS (SUPERVISOR REVIEW REQUIRED)"
    else:
        mass_status = "FAIL (NON-CONFORMANCE — TEST INVALID)"

    mass_qc = MassBalanceQC(
        feed_mass_g=round(feed_mass_g, 2),
        recovered_mass_g=round(total_recovered_mass, 2),
        mass_loss_g=round(mass_loss_g, 2),
        mass_loss_pct=round(mass_loss_pct, 2),
        target_limit_pct=1.00,
        hard_limit_pct=2.00,
        status=mass_status,
    )

    # Normalized yields: ISO 7936 normalizes recovered fractions to 100.00%
    fraction_yields = [
        (f.dry_mass_g / total_recovered_mass) * 100.0 if total_recovered_mass > 0 else 0.0
        for f in fractions
    ]

    # Reconstituted ash and CV
    rec_ash = sum(y * f.ash_pct for y, f in zip(fraction_yields, fractions)) / 100.0
    rec_cv = (
        sum(y * f.cv_mj_kg for y, f in zip(fraction_yields, fractions) if f.cv_mj_kg is not None)
        / 100.0
        if any(f.cv_mj_kg is not None for f in fractions)
        else None
    )

    # Ash QC gate (|delta| <= 0.50% absolute per ISO 1171 / AS003IW)
    ash_qc = None
    if head_ash_pct is not None:
        delta_ash = abs(head_ash_pct - rec_ash)
        ash_qc = QualityReconciliation(
            head_value=round(head_ash_pct, 2),
            reconstituted_value=round(rec_ash, 2),
            absolute_delta=round(delta_ash, 2),
            acceptance_tolerance=0.50,
            status="PASS" if delta_ash <= 0.50 else "FAIL (NCR REQUIRED)",
        )

    # CV QC gate (|delta| <= 0.30 MJ/kg per ISO 1928 / AS007IW)
    cv_qc = None
    if head_cv_mj_kg is not None and rec_cv is not None:
        delta_cv = abs(head_cv_mj_kg - rec_cv)
        cv_qc = QualityReconciliation(
            head_value=round(head_cv_mj_kg, 2),
            reconstituted_value=round(rec_cv, 2),
            absolute_delta=round(delta_cv, 2),
            acceptance_tolerance=0.30,
            status="PASS" if delta_cv <= 0.30 else "FAIL (NCR REQUIRED)",
        )

    # Cumulative calculations
    n = len(fractions)
    cum_floats_y = 0.0
    cum_floats_ash_prod = 0.0
    cum_floats_cv_prod = 0.0

    output_fractions: List[FractionOutput] = []

    for i in range(n):
        y = fraction_yields[i]
        f = fractions[i]
        label, mid_rd = format_rd_label(f.lower_rd, f.upper_rd)

        # Cumulative Floats
        cum_floats_y += y
        cum_floats_ash_prod += y * f.ash_pct
        cum_ash = cum_floats_ash_prod / cum_floats_y if cum_floats_y > 0 else 0.0

        cum_cv = None
        if f.cv_mj_kg is not None:
            cum_floats_cv_prod += y * f.cv_mj_kg
            cum_cv = cum_floats_cv_prod / cum_floats_y if cum_floats_y > 0 else None

        # Cumulative Sinks (from index i to n-1)
        sinks_y = sum(fraction_yields[k] for k in range(i, n))
        sinks_ash_prod = sum(fraction_yields[k] * fractions[k].ash_pct for k in range(i, n))
        sinks_ash = sinks_ash_prod / sinks_y if sinks_y > 0 else 0.0

        sinks_cv = None
        if any(fractions[k].cv_mj_kg is not None for k in range(i, n)):
            sinks_cv_prod = sum(
                fraction_yields[k] * (fractions[k].cv_mj_kg or 0.0) for k in range(i, n)
            )
            sinks_cv = sinks_cv_prod / sinks_y if sinks_y > 0 else None

        output_fractions.append(
            FractionOutput(
                code=f.code,
                rd_interval=label,
                mid_rd=round(mid_rd, 3),
                dry_mass_g=round(f.dry_mass_g, 1),
                fractional_yield_pct=round(y, 2),
                ash_pct=round(f.ash_pct, 2),
                moisture_pct=round(f.moisture_pct, 2) if f.moisture_pct is not None else None,
                cv_mj_kg=round(f.cv_mj_kg, 2) if f.cv_mj_kg is not None else None,
                cum_floats_yield_pct=round(cum_floats_y, 2),
                cum_floats_ash_pct=round(cum_ash, 2),
                cum_floats_cv_mj_kg=round(cum_cv, 2) if cum_cv is not None else None,
                cum_sinks_yield_pct=round(sinks_y, 2),
                cum_sinks_ash_pct=round(sinks_ash, 2),
                cum_sinks_cv_mj_kg=round(sinks_cv, 2) if sinks_cv is not None else None,
            )
        )

    # Near-Density Material (NDM ± 0.10 RD) calculation for intermediate cut densities
    # Evaluates total coal yield within ±0.10 RD of a cut point
    ndm_results: Dict[str, float] = {}
    cut_densities = [1.40, 1.50, 1.60, 1.70, 1.80]
    for cut in cut_densities:
        low_bound = round(cut - 0.10, 2)
        high_bound = round(cut + 0.10, 2)
        ndm_yield = 0.0
        for y, f in zip(fraction_yields, fractions):
            _, mid = format_rd_label(f.lower_rd, f.upper_rd)
            if low_bound <= mid <= high_bound:
                ndm_yield += y
        ndm_results[f"NDM at {cut:.2f} RD (±0.10 RD)"] = round(ndm_yield, 2)

    return WashabilityReport(
        sample_id=sample_id,
        size_fraction=size_fraction,
        mass_qc=mass_qc,
        ash_qc=ash_qc,
        cv_qc=cv_qc,
        fractions=output_fractions,
        near_density_material=ndm_results,
    )


def compute_tromp_parameters(
    densities: List[float], partition_coefficients: List[float]
) -> Dict[str, float]:
    """
    Interpolates d25, d50, d75 from a partition curve and computes:
    Ep (Ecart Probable) = (d75 - d25) / 2
    Imperfection (I) = Ep / (d50 - 1.0)
    """
    def interpolate_density(target_pc: float) -> float:
        for i in range(len(partition_coefficients) - 1):
            p1 = partition_coefficients[i]
            p2 = partition_coefficients[i + 1]
            if (p1 <= target_pc <= p2) or (p2 <= target_pc <= p1):
                d1 = densities[i]
                d2 = densities[i + 1]
                if p2 == p1:
                    return d1
                return d1 + (target_pc - p1) * (d2 - d1) / (p2 - p1)
        return float("nan")

    d25 = interpolate_density(25.0)
    d50 = interpolate_density(50.0)
    d75 = interpolate_density(75.0)
    ep = (d75 - d25) / 2.0 if not (math.isnan(d75) or math.isnan(d25)) else float("nan")
    imperfection = ep / (d50 - 1.0) if not (math.isnan(ep) or math.isnan(d50) or d50 <= 1.0) else float("nan")

    return {
        "d25_g_cm3": round(d25, 4),
        "d50_cut_point_g_cm3": round(d50, 4),
        "d75_g_cm3": round(d75, 4),
        "ep_ecart_probable": round(ep, 4),
        "imperfection_I": round(imperfection, 4),
    }


def print_washability_table(report: WashabilityReport):
    """Prints clean, audit-ready ISO 7936 washability table to stdout."""
    print("=" * 115)
    print(f"AZURESKY (PTY) LTD — COAL WASHABILITY REPORT (ISO 7936:2022 / AS013IW Rev 02)")
    print(f"Sample ID:      {report.sample_id}")
    print(f"Size Fraction:  {report.size_fraction}")
    print("=" * 115)
    print(
        f"Feed Mass:      {report.mass_qc.feed_mass_g:.1f} g  |  "
        f"Recovered: {report.mass_qc.recovered_mass_g:.1f} g  |  "
        f"Loss: {report.mass_qc.mass_loss_g:.1f} g ({report.mass_qc.mass_loss_pct:.2f}%)  |  "
        f"Status: {report.mass_qc.status}"
    )
    if report.ash_qc:
        print(
            f"Ash Balance:    Head = {report.ash_qc.head_value:.2f}%  |  "
            f"Reconstituted = {report.ash_qc.reconstituted_value:.2f}%  |  "
            f"|Delta| = {report.ash_qc.absolute_delta:.2f}% (Limit <= 0.50%)  |  "
            f"Status: {report.ash_qc.status}"
        )
    if report.cv_qc:
        print(
            f"CV Balance:     Head = {report.cv_qc.head_value:.2f} MJ/kg  |  "
            f"Reconstituted = {report.cv_qc.reconstituted_value:.2f} MJ/kg  |  "
            f"|Delta| = {report.cv_qc.absolute_delta:.2f} MJ/kg (Limit <= 0.30)  |  "
            f"Status: {report.cv_qc.status}"
        )
    print("-" * 115)
    headers = [
        "Code",
        "RD Interval",
        "Mass (g)",
        "Yield (%)",
        "Ash (%)",
        "CV (MJ/kg)",
        "Cum Fl Y (%)",
        "Cum Fl Ash (%)",
        "Cum Sk Y (%)",
        "Cum Sk Ash (%)",
    ]
    print(
        f"{headers[0]:<6} {headers[1]:<16} {headers[2]:>9} {headers[3]:>10} {headers[4]:>9} "
        f"{headers[5]:>11} {headers[6]:>13} {headers[7]:>15} {headers[8]:>13} {headers[9]:>15}"
    )
    print("-" * 115)
    for f in report.fractions:
        cv_str = f"{f.cv_mj_kg:.2f}" if f.cv_mj_kg is not None else "-"
        print(
            f"{f.code:<6} {f.rd_interval:<16} {f.dry_mass_g:>9.1f} {f.fractional_yield_pct:>10.2f} "
            f"{f.ash_pct:>9.2f} {cv_str:>11} {f.cum_floats_yield_pct:>13.2f} {f.cum_floats_ash_pct:>15.2f} "
            f"{f.cum_sinks_yield_pct:>13.2f} {f.cum_sinks_ash_pct:>15.2f}"
        )
    print("=" * 115)
    print("NEAR-DENSITY MATERIAL (NDM ±0.10 RD) — BIRD INDEX OF SEPARATION DIFFICULTY:")
    for k, v in report.near_density_material.items():
        if v < 7.0:
            diff = "Simple separation"
        elif v <= 10.0:
            diff = "Moderately difficult"
        elif v <= 15.0:
            diff = "Difficult separation"
        elif v <= 20.0:
            diff = "Very difficult separation"
        else:
            diff = "Extremely difficult separation (High misplacement risk)"
        print(f"  • {k:<30}: {v:>6.2f} %  ==>  {diff}")
    print("=" * 115)


def get_benchmark_dataset(dataset_name: str = "VAL-COAL-A") -> Tuple[float, List[FractionInput], float, float]:
    """Returns official CWP-001 validation benchmark datasets."""
    if dataset_name == "VAL-COAL-A":
        # Witbank Seam 4 Bituminous Steam Coal (Matches CWP-001-VAL-001 Section 4.3)
        feed_mass = 6245.0  # grams
        head_ash = 26.35    # % db
        head_cv = 21.78     # MJ/kg gross CV
        fractions = [
            FractionInput("F-01", None, 1.40, 1865.6, 8.20, 3.20, 28.45),
            FractionInput("F-02", 1.40, 1.50, 1554.7, 14.60, 2.90, 25.80),
            FractionInput("F-03", 1.50, 1.60, 808.4, 21.80, 2.70, 23.10),
            FractionInput("F-04", 1.60, 1.70, 497.5, 30.20, 2.40, 19.95),
            FractionInput("F-05", 1.70, 1.80, 373.1, 41.50, 2.00, 16.20),
            FractionInput("S-01", 1.80, None, 1119.5, 68.40, 1.50, 7.40),
        ]
        return feed_mass, fractions, head_ash, head_cv

    elif dataset_name == "VAL-COAL-B":
        # Highveld Seam 2 Industrial Blend
        feed_mass = 10000.0
        head_ash = 28.20
        head_cv = 22.80
        fractions = [
            FractionInput("F-01", None, 1.30, 420.0, 8.10, 3.0, 29.50),
            FractionInput("F-02", 1.30, 1.40, 1680.0, 12.30, 2.8, 27.60),
            FractionInput("F-03", 1.40, 1.50, 2150.0, 16.80, 2.6, 25.40),
            FractionInput("F-04", 1.50, 1.60, 1820.0, 23.50, 2.3, 22.30),
            FractionInput("F-05", 1.60, 1.70, 1250.0, 31.00, 2.1, 19.20),
            FractionInput("F-06", 1.70, 1.80, 890.0, 41.50, 1.8, 15.60),
            FractionInput("F-07", 1.80, 1.90, 640.0, 52.80, 1.5, 11.40),
            FractionInput("S-01", 1.90, None, 1100.0, 72.00, 1.1, 6.20),
        ]
        return feed_mass, fractions, head_ash, head_cv

    else:
        raise ValueError(f"Unknown benchmark dataset: {dataset_name}")


def main():
    """Runs calculation engine with benchmark data and self-tests."""
    print("=" * 115)
    print("AZURESKY ISO 7936:2022 WASHABILITY ENGINE (AS_CALC_WASH_01.py)")
    print("Executing Self-Test & Quality Reconciliation with Benchmark VAL-COAL-A...")
    print("=" * 115)

    feed_mass, fractions, head_ash, head_cv = get_benchmark_dataset("VAL-COAL-A")
    report = compute_washability(
        sample_id="VAL-COAL-A-01",
        size_fraction="+0.5 mm to +25.0 mm",
        feed_mass_g=feed_mass,
        fractions=fractions,
        head_ash_pct=head_ash,
        head_cv_mj_kg=head_cv,
    )

    print_washability_table(report)

    # Verification Assertions (Self-Test)
    assert report.mass_qc.status == "PASS (TARGET)", f"Mass balance failed: {report.mass_qc.status}"
    assert report.mass_qc.mass_loss_pct <= 1.0, f"Mass loss exceeds target 1.0%: {report.mass_qc.mass_loss_pct}"
    assert report.ash_qc.status == "PASS", f"Ash reconstitution failed: {report.ash_qc.status}"
    assert report.cv_qc.status == "PASS", f"CV reconstitution failed: {report.cv_qc.status}"
    assert abs(report.fractions[-1].cum_floats_yield_pct - 100.0) < 0.01, "Final cumulative yield != 100%"

    print("\n[VERIFICATION AUDIT]: All Self-Test Assertions PASSED successfully.")

    # Tromp Partition Curve demonstration
    print("\n" + "=" * 115)
    print("TROMP PARTITION CURVE EVALUATION (ISO 7936 Clause 8):")
    simulated_rd = [1.35, 1.45, 1.55, 1.65, 1.75, 1.85]
    simulated_pc = [2.5, 12.0, 42.0, 78.0, 94.0, 98.5]
    tromp = compute_tromp_parameters(simulated_rd, simulated_pc)
    for k, v in tromp.items():
        print(f"  • {k:<25}: {v:.4f}")
    print("=" * 115)


if __name__ == "__main__":
    main()
