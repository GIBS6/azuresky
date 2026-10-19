# CWP-001: MISSION 002 EVIDENCE INDEX
## Controlled Inventory of Inspected Files, Exact Paths, Revisions, and Inspection Baseline

```
Document ID:     CWP-001-AUD-002-EVI
Project:         Coal Washability Testing Laboratory Capability (CWP-001)
Mission:         Mission 002 — Technical Method and QMS Gap Verification
Parent System:   AzureSky (Pty) Ltd — ISO/IEC 17025:2017 Accredited Quality Management System
Inspection Date: 13 October 2026
Audit Mode:      Read-Only Evidence Verification
Classification:  Quality Audit Record & Metrological Traceability Index
```

---

## 1. Scope & Verification Protocol

This index records every document, spreadsheet, standard, and record inspected during **Mission 002**. Each entry specifies the exact physical filesystem path, document identifier, controlled revision number, inspection date, and any technical access or interpretation limitations.

### Path & Location Conventions:
* **Live Controlled QMS**: `Z:\AZURESKY SYSTEM\AZURESKY QMS\`
* **CWP-001 Working Repository**: `C:\Projects\AzureSky\CWP-001\`
* **Read-Only Archaeology Extract**: `C:\Projects\AzureSky\CWP-001\00_EXISTING_SYSTEM_ARCHEOLOGY\`

---

## 2. Live AzureSky Controlled QMS Documents (Drive `Z:\`)

| Item # | Document Title & Controlled Path | Document ID | Rev / Date | Status in QMS | Inspection Date | Limitations & Observations |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **QMS-01** | [`ASMF 5.3 Statement of Conformity (Defining scope of work) REV 02.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%205/ASMF%205.3%20Statement%20of%20Conformity%20(Defining%20scope%20of%20work)%20REV%2002.docx) | ASMF 5.3 | Rev 02<br/>(09/2026) | Approved | 2026-10-13 | Inspected via python-docx. Confirms SANAS accreditation for Prep, Ash, VM, CV, MIAS, TM. Declares Float & Sink (ISO 7936) and PSD (ISO 1953) as NOT accredited. Sampling excluded from scope. |
| **QMS-02** | [`AS013IW FLOAT AND SINK WASHABILITY STANDARD OPERATING PROCEDURE.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS013IW%20FLOAT%20AND%20SINK%20WASHABILITY%20STANDARD%20OPERATING%20PROCEDURE.docx) | AS013IW | Rev 01 | Controlled SOP | 2026-10-13 | Inspected in full. Coarse coal only (-25 mm +0.5 mm); 6 kg charges; ZnCl₂ solutions; buckets/scoops; drying "until visibly dry"; mass balance limit $\le 2\%$. Cites "ISO 13909-3" as preparation (editorial error). |
| **QMS-03** | [`ASMF 02- FLOAT AND SINK VALIDATION FORM.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/ASMF%2002-%20FLOAT%20AND%20SINK%20VALIDATION%20FORM.docx) | ASMF 02 | Current | Controlled Form | 2026-10-13 | Located in `...PROCEDURES\`, not in a `FORMS\` subfolder. Blank table for hydrometer verification RD 1.30–2.00 ($\pm 0.002\text{ g/cm}^3$). Contains no method validation data. |
| **QMS-04** | [`AS014IW DETERMINATION OF PARTICLE SIZE DISTRIBUTION.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS014IW%20DETERMINATION%20OF%20PARTICLE%20SIZE%20DISTRIBUTION.docx) | AS014IW | Rev 01 | Controlled SOP | 2026-10-13 | Inspected in full. Dry sieving; scalping at 22.4 mm; manual 2-person rocking screen; fines sieving 2 min; Section 5.2 forces all mass loss into fines receiver. Cites "ISO 1953" undated. |
| **QMS-05** | [`AS001IW PROCEDURE ON SAMPLE PREPARATION OF HARD COAL Rev 05.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS001IW%20PROCEDURE%20ON%20SAMPLE%20PREPARATION%20OF%20HARD%20COAL%20Rev%2005.docx) | AS001IW | Rev 05<br/>(21/09/2026) | Approved & Accredited | 2026-10-13 | Inspected in full. Governs stage comminution (25 mm $\to$ 10 mm $\to$ 3 mm), pulverising ($-212\text{ }\mu\text{m}$), and 210 L mixing drum for CRM/PT lots. Omits non-destructive sizing branch. |
| **QMS-06** | [`AS003IW PROCEDURE ON THE DETERMINATION OF ASH CONTENT rev 01.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS003IW%20PROCEDURE%20ON%20THE%20DETERMINATION%20OF%20ASH%20CONTENT%20rev%2001.docx) | AS003IW | Rev 01 | Approved & Accredited | 2026-10-13 | Inspected. ISO 1171 slow ramping to $815 \pm 5^\circ\text{C}$; porcelain crucibles; ATS muffle furnace; LIMS auto-transfer. Valid for washability fraction analysis. |
| **QMS-07** | [`AS004IW  PROCEDURE ON DETERMINATION OF INHERENT(ANALYSIS) MOISTURE REV 02.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS004IW%20%20PROCEDURE%20ON%20DETERMINATION%20OF%20INHERENT(ANALYSIS)%20MOISTURE%20REV%2002.docx) | AS004IW | Rev 02 | Approved & Accredited | 2026-10-13 | Note: filename contains two spaces after AS004IW. Inherent moisture ($M_{\text{ad}}$) at 105–110°C; SANS 5925. Valid for dry-basis conversion ($A_{\text{d}}$). |
| **QMS-08** | [`AS006IW PROCEDURE ON ISO VOLATILE DETERMINATION rev 02.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS006IW%20PROCEDURE%20ON%20ISO%20VOLATILE%20DETERMINATION%20rev%2002.docx) | AS006IW | Rev 02<br/>(15/06/2026) | Approved & Accredited | 2026-10-13 | Inspected. $900 \pm 5^\circ\text{C}$ for 7 min in silica crucibles. Cites ISO 562:2010 in text, though ISO 562:2024 is present in QMS library. |
| **QMS-09** | [`AS007IW PROCEDURE ON CALORIFIC VALUE DETERMINATION.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS007IW%20PROCEDURE%20ON%20CALORIFIC%20VALUE%20DETERMINATION.docx) | AS007IW | Rev 01 | Approved & Accredited | 2026-10-13 | Inspected. Bomb calorimeter with benzoic acid; ISO 1928:2020. Valid for composite product analysis. |
| **QMS-10** | [`AS008IW SAMPLING PROCEDURE.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS008IW%20SAMPLING%20PROCEDURE.docx) | AS008IW | Rev 01 | Controlled SOP | 2026-10-13 | Inspected. Manual sampling for CRM/PT lots citing ISO 18283:2006 (superseded). Excluded from accredited scope per ASMF 5.3. |
| **QMS-11** | [`6.3 EQUIPMENT REGISTER.xlsx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%206/EQUIPMENT/6.3%20EQUIPMENT%20REGISTER.xlsx) | Doc 6.3 ER | Current | Controlled Register | 2026-10-13 | Inspected via zipfile/XML. 27 items listed. Contains ID collision on AS8284 and AS00111. Completely omits hydrometers, F&S baths, and test sieves. |
| **QMS-12** | [`6.5. AZURESKY METROLOGICAL TRACEABILITY MEMORANDUM.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%206/EQUIPMENT/6.5.%20AZURESKY%20METROLOGICAL%20TRACEABILITY%20MEMORANDUM.docx) | Doc 6.5 | Rev 01 | Controlled Policy | 2026-10-13 | Policy establishing unbroken calibration chains to NMISA via SANAS-accredited calibration laboratories (Micron Lab & Montech). |
| **QMS-13** | [`COMPETENCY MATRIX 01.xlsx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%206/PERSONNEL%20COMPETENCY/6.2%20COMPETENCY%20MATRIX/COMPETENCY%20MATRIX%2001.xlsx) | ASHR005 Comp 01 | Rev 0 | Controlled Matrix | 2026-10-13 | Inspected. Authorized by S. Nyambi. Tracks 5 analysts. Columns: Prep, Moisture, Ash, Volatiles, CV, QC, NCs. F&S and PSD are completely absent. |
| **QMS-14** | [`UB001 UNCERTAINTY BUDGET rev 01.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.6.%20MEASUREMENT%20UNCERTAINTY/UB001%20UNCERTAINTY%20BUDGET%20rev%2001.docx) | UB001 | Rev 01 | Controlled Budget | 2026-10-13 | Master uncertainty evaluation for balances, ovens, furnaces, thermometers, Ash, Moisture, VM, CV. Washability measurands not addressed. |
| **QMS-15** | [`AS001V ENSURING VALIDITY OF RESULTS PROCEDURE.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.7%20ENSURING%20VALIDATION%20OF%20RESULTS/AS001V%20ENSURING%20VALIDITY%20OF%20RESULTS%20PROCEDURE.docx) | AS001V | Rev 01 | Controlled SOP | 2026-10-13 | Repeatability gates: Ash, VM, IM, CV, TM, PSD (2% precision). F&S mass balance and recovery gates absent. |
| **QMS-16** | [`AS001MMV- Memorandum Validation of Methods ISO 17025 7.2.2.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.2.%20METHOD%20VALIDATION/AS001MMV-%20Memorandum%20Validation%20of%20Methods%20ISO%2017025%207.2.2.docx) | AS001MMV | Current<br/>(20/10/2025) | Controlled Policy | 2026-10-13 | Method validation policy under Clause 7.2.2 and SANAS TR-26. Confirms validation dossiers on Z: for Ash, Moisture, VM, CV, TM, Prep. No F&S validation file exists. |
| **QMS-17** | [`AS002LV- LIMS VALIDATION FOR FUNCTIONALITY.xlsx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.11.%20MANAGEMENT%20OF%20RECORDS/AS002LV-%20LIMS%20VALIDATION%20FOR%20FUNCTIONALITY.xlsx) | AS002LV | Current | Controlled Record | 2026-10-13 | Inspected via XML. Sheets: 'VOLATILE MATTER', 'INHERENT MOISTURE', 'ASH'. Washability reduction formulas and PSD calculations are absent. |
| **QMS-18** | [`ASMF 7.11 Data Integrity Risk Management Procedure.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.11.%20MANAGEMENT%20OF%20RECORDS/ASMF%207.11%20Data%20Integrity%20Risk%20Management%20Procedure.docx) | ASMF 7.11 | Rev 01 | Controlled SOP | 2026-10-13 | Data governance, spreadsheet protection, user access levels, audit trails. Applies to washability spreadsheet validation. |
| **QMS-19** | [`7.8. REPORTING OF RESULTS.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.8%20REPORTING/7.8.%20REPORTING%20OF%20RESULTS.docx) | Doc 7.8 | Rev 01 | Controlled Policy | 2026-10-13 | Section 4.8 enforces SANAS R04: SANAS logo only on accredited parameters; non-accredited results must carry explicit disclaimers. |
| **QMS-20** | [`AS010IW STATEMENTS OF CONFORMITY & DECISION RULES.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/PROCEDURES/AS010IW%20STATEMENTS%20OF%20CONFORMITY%20&%20DECISION%20RULES.docx) | AS010IW | Rev 00 | Controlled SOP | 2026-10-13 | Guard-band decision rules per ILAC-G8. Default to reporting measured values unless conformity statement requested. Located in `PROCEDURES\`. |
| **QMS-21** | [`7.17 MANAGEMENT OF NON-CONFORMING WORK Rev 05.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.10%20NON%20CONFORMING%20WORK/7.17%20MANAGEMENT%20OF%20NON-CONFORMING%20WORK%20Rev%2005.docx) | Doc 7.17 | Rev 05 | Controlled SOP | 2026-10-13 | Immediate halt-work authority; SANAS F03-09 NCR form; RCA forms AS001MF / AS004MF. Folder is `7.10 NON CONFORMING WORK`. |
| **QMS-22** | [`AS009IW WASTE MANAGEMENT PROCEDURE.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/PROCEDURES/AS009IW%20WASTE%20MANAGEMENT%20PROCEDURE.docx) | AS009IW | Rev 01<br/>(29/09/2025) | Controlled SOP | 2026-10-13 | Covers solid coal residues (Drum 1), plastics (Drum 2), boxes (Drum 3). Completely omits liquid hazardous chemical waste and ZnCl₂ rinse water. |
| **QMS-23** | [`8.4 DOCUMENT CONTROL Rev 01.docx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%208/8.4%20DOCUMENT%20CONTROL%20Rev%2001.docx) | Doc 8.4 | Rev 01 | Controlled SOP | 2026-10-13 | Master document control procedure governing review cycles, technical signatory review, lab manager approvals, and QMS issuance. |

---

## 3. Normative Standards Library Files on Record (Drive `Z:\`)

| Item # | Standard File on `Z:\` | Edition | File Path | Ingestion Status |
| :---: | :--- | :---: | :--- | :--- |
| **STD-01** | `WASHABILITY-ISO_7936_2022(en).pdf` | ISO 7936:2022 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-02** | `SAMPLE PREP-ISO_13909-4_2025(en).pdf` | ISO 13909-4:2025 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-03** | `ISO ASH-ISO_1171_2024(en) AS.pdf` | ISO 1171:2024 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-04** | `VOLATILE MATTER-ISO_562_2024(en).pdf` | ISO 562:2024 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-05** | `CV-ISO_1928_2020(en).pdf` | ISO 1928:2020 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-06** | `TM-ISO_589_2008(en).pdf` | ISO 589:2008 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record (superseded by 2024 edition). |
| **STD-07** | `AFT DETERMINATION-ISO_540_2025(en).pdf` | ISO 540:2025 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record (subcontracted test). |
| **STD-08** | `ISO_IEC_17025_2017(en).pdf` | ISO/IEC 17025:2017 | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | Controlled PDF copy on record. |
| **STD-09** | *ISO 1953 (Size analysis by sieving)* | Missing | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | **NOT LOCATED** in QMS library. |
| **STD-10** | *ISO 18283 (Manual sampling)* | Missing | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | **NOT LOCATED** in QMS library. |
| **STD-11** | *ISO 13909-1 (Mechanical sampling general)* | Missing | `Z:\AZURESKY SYSTEM\AZURESKY QMS\17025\CLAUSE 7\7.2...\ISO STANDARDS\` | **NOT LOCATED** in QMS library. |

---

## 4. CWP-001 Project Documents Inspected (Drive `C:\`)

| Item # | Document Title & Workspace Path | Declared ID | Document Type & Status | Inspection Notes & Verification |
| :---: | :--- | :---: | :---: | :--- |
| **WS-01** | [`CWP-001_ARCHITECTURE_FREEZE.md`](file:///c:/Projects/AzureSky/CWP-001/CWP-001_ARCHITECTURE_FREEZE.md) | CWP-001-GOV-001 | Frozen Protocol | Root copy identical to `00_GOVERNANCE/CWP-001_ARCHITECTURE_FREEZE.md`. Locks 22-module structure and QMS boundaries. |
| **WS-02** | [`AZURESKY_WASHABILITY_CURRENT_STATE_MAP.md`](file:///c:/Projects/AzureSky/CWP-001/AZURESKY_WASHABILITY_CURRENT_STATE_MAP.md) | CWP-001-ARCH-001 | Audit Baseline | Root copy identical to `01_EXISTING_AZURESKY_SYSTEM/...`. Detailed 13-point archaeological audit of live QMS. |
| **WS-03** | [`CWP-001_STANDARDS_REGISTER.md`](file:///c:/Projects/AzureSky/CWP-001/CWP-001_STANDARDS_REGISTER.md) | CWP-001-REG-001 | Normative Register | Root copy identical to `02_STANDARDS/...`. 7-layer compliance matrix. Cites ISO 1953:2025 and ISO 13909:2025 series. |
| **WS-04** | [`CWP-001_STANDARDS_VERIFICATION_MATRIX.md`](file:///c:/Projects/AzureSky/CWP-001/CWP-001_STANDARDS_VERIFICATION_MATRIX.md) | CWP-001-AUDIT-001 | Verification Matrix | Root copy identical to `03_GAP_ANALYSIS/...`. Line-by-line comparison of standards against live QMS evidence. |
| **WS-05** | [`CWP-001_DOCUMENT_LINK_AND_EVIDENCE_REGISTER.md`](file:///c:/Projects/AzureSky/CWP-001/CWP-001_DOCUMENT_LINK_AND_EVIDENCE_REGISTER.md) | CWP-001-REG-002 | Master Register | **Diverges** from copy in `01_EXISTING_AZURESKY_SYSTEM/`. Contains broken links to QMS files due to filename mismatches. |
| **WS-06** | [`AS013IW_Rev_02_PROCEDURE_ON_FLOAT_AND_SINK_ANALYSIS.md`](file:///c:/Projects/AzureSky/CWP-001/17_SOPS_AND_FORMS/AS013IW_Rev_02_PROCEDURE_ON_FLOAT_AND_SINK_ANALYSIS.md) | AS013IW Rev 02 | Type C Proposal | Proposed SOP. Marked "CONTROLLED SOP PROPOSAL — SUBMITTED FOR FORMAL QMS APPROVAL". Unapproved by QMS authorities. |
| **WS-07** | [`AS030TF_FLOAT_AND_SINK_BENCHSHEET_AND_CALCULATION_TEMPLATE.md`](file:///c:/Projects/AzureSky/CWP-001/17_SOPS_AND_FORMS/AS030TF_FLOAT_AND_SINK_BENCHSHEET_AND_CALCULATION_TEMPLATE.md) | AS030TF Rev 01 | Type C Proposal | Proposed bench recording form. Not issued into QMS. |
| **WS-08** | [`CWP-001-VAL-001_FLOAT_AND_SINK_METHOD_VALIDATION_DOSSIER.md`](file:///c:/Projects/AzureSky/CWP-001/13_METHOD_VALIDATION/CWP-001-VAL-001_FLOAT_AND_SINK_METHOD_VALIDATION_DOSSIER.md) | CWP-001-VAL-001 | Type D Proposal | Validation dossier proposal with modeled performance figures. Marked "READY FOR TECHNICAL REVIEW". Unwitnessed in lab. |
| **WS-09** | [`UB001-FS-01_WASHABILITY_MEASUREMENT_UNCERTAINTY_MODEL.md`](file:///c:/Projects/AzureSky/CWP-001/14_MEASUREMENT_UNCERTAINTY/UB001-FS-01_WASHABILITY_MEASUREMENT_UNCERTAINTY_MODEL.md) | UB001-FS-01 | Type D Proposal | Mathematical uncertainty model for Yield, Cut-Point, Cum Ash. Not ingested into QMS UB001. |
| **WS-10** | [`AZCA-007_FLOAT_AND_SINK_COMPETENCY_ASSESSMENT_PROTOCOL.md`](file:///c:/Projects/AzureSky/CWP-001/16_COMPETENCY/AZCA-007_FLOAT_AND_SINK_COMPETENCY_ASSESSMENT_PROTOCOL.md) | AZCA-007 Rev 01 | Type D Proposal | 4-stage competency protocol. Not authorized or added to live Competency Matrix. |
| **WS-11** | [`CWP-002_EQUIPMENT_PERFORMANCE_AND_GAP_SPECIFICATION.md`](file:///c:/Projects/AzureSky/CWP-001/15_EQUIPMENT_AND_METROLOGY/CWP-002_EQUIPMENT_PERFORMANCE_AND_GAP_SPECIFICATION.md) | CWP-002 Rev 01 | Type D Proposal | Apparatus gap analysis and procurement Bill of Quantities. Proposal only. |
| **WS-12** | [`CWP-REP-001_ISO_17025_WASHABILITY_TEST_REPORT_TEMPLATE.md`](file:///c:/Projects/AzureSky/CWP-001/19_REPORTING/CWP-REP-001_ISO_17025_WASHABILITY_TEST_REPORT_TEMPLATE.md) | CWP-REP-001 Rev 01 | Type D Proposal | Client report template. Complies with ISO 17025 Cl 7.8 and ILAC-G8. Proposal only. |
| **WS-13** | [`CWP-001-DM-001_DENSITY_MEDIUM_SELECTION_AND_ENVIRONMENTAL_STUDY.md`](file:///c:/Projects/AzureSky/CWP-001/07_DENSITY_MEDIA/CWP-001-DM-001_DENSITY_MEDIUM_SELECTION_AND_ENVIRONMENTAL_STUDY.md) | CWP-001-DM-001 | Type D Study | Engineering trade-off evaluating ZnCl₂ vs SPT/CsCl/organics, Stokes settling kinetics, and closed-loop wash water. |

---

## 5. Archaeological Mirror Files (`00_EXISTING_SYSTEM_ARCHEOLOGY\`)

All 16 text extraction files in `C:\Projects\AzureSky\CWP-001\00_EXISTING_SYSTEM_ARCHEOLOGY\` were inspected. Direct textual comparisons against the live `.docx` and `.xlsx` files on `Z:\` confirm that these files represent **accurate, read-only forensic extractions** taken from `Z:\` during the baseline audit. They carry no independent authority.

---
*End of Mission 002 Evidence Index.*
