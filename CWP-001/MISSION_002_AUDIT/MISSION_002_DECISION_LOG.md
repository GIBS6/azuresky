# CWP-001: MISSION 002 DECISION LOG
## Traceable Log of Technical, Operational & Quality-Management Decisions Required from Authorized Personnel

```
Document ID:     CWP-001-AUD-002-DEC
Project:         Coal Washability Testing Laboratory Capability (CWP-001)
Mission:         Mission 002 — Technical Method and QMS Gap Verification
Parent System:   AzureSky (Pty) Ltd — ISO/IEC 17025:2017 Accredited Quality Management System
Audit Date:      13 October 2026
Audit Authority: Read-Only Verification Baseline (Decisions Reserved for Authorized Roles)
```

---

## 1. Decision Governance & Authority Principles

In accordance with **ISO/IEC 17025:2017** (Clauses 5, 6.2, 7.2, and 8.4) and the [CWP-001 Architecture Freeze Protocol](file:///c:/Projects/AzureSky/CWP-001/CWP-001_ARCHITECTURE_FREEZE.md#L96-L98):

> **Antigravity AI operates in an advisory and investigative capacity only. It has NO authority to approve controlled procedures, grant accreditations, reassign asset numbers in live registers, modify quality policies, or approve capital expenditure.**

Every item in this decision log must be formally resolved by the designated AzureSky authority:
* **Laboratory Manager (S. Nyambi)**: Quality system ownership, accreditation scope, resource allocation, and document approval.
* **Technical Signatory / Lab Supervisor (T. Maponya)**: Method validation review, equipment metrology, competency assessment, and test reporting.
* **Project Owner / Director**: Corporate strategy, capital expenditure, and commercial contracts.

---

## 2. Structured Decision Register

### DEC-01: Master Document Duplicate Disposition
* **Domain**: Governance & Document Control (Clause 8.4)
* **Context**: Four master documents exist as identical duplicates across the workspace root and subdirectories (`CWP-001_ARCHITECTURE_FREEZE.md`, `AZURESKY_WASHABILITY_CURRENT_STATE_MAP.md`, `CWP-001_STANDARDS_REGISTER.md`, `CWP-001_STANDARDS_VERIFICATION_MATRIX.md`). Furthermore, `CWP-001_DOCUMENT_LINK_AND_EVIDENCE_REGISTER.md` has two non-identical versions.
* **Options**:
  1. *Option A (Recommended)*: Declare root files as the sole authoritative master artifacts; move all subfolder duplicates to an archive folder (`00_ARCHIVE_HISTORICAL/`) to eliminate version confusion.
  2. *Option B*: Retain subfolder copies as read-only module mirrors, maintaining exact synchronization via file-hash validation scripts.
* **Technical / Quality Impact**: Retaining unsynchronized duplicate files violates document control principles (ISO 17025 Cl 8.4) and leads to conflicting working drafts.
* **Decision Authority**: Laboratory Manager (S. Nyambi) / Project Owner
* **Status**: **PENDING REVIEW**

---

### DEC-02: Standards Library Ingestion & Procurement
* **Domain**: Method Selection & Normative Baseline (Clause 7.2.1)
* **Context**: The controlled QMS library (`Z:\...\ISO STANDARDS\`) does not contain controlled PDF copies of `ISO 1953:2025` (Size analysis), `ISO 18283:2022` (Manual sampling), or `ISO 13909-1:2025` (Mechanical sampling), despite these standards being cited across CWP-001. Furthermore, `AS008IW` still cites withdrawn `ISO 18283:2006`, and `AS006IW` cites `ISO 562:2010` (while the 2024 edition is on record).
* **Options**:
  1. *Option A (Recommended)*: Formally procure single-user licensed PDF copies of `ISO 1953:2025` and `ISO 18283:2022` and ingest them into `Z:\...\ISO STANDARDS\`; update references in `AS008IW` and `AS006IW`.
  2. *Option B*: Restrict washability documentation to existing standards on record, retaining national SANS endorsements where available.
* **Technical / Quality Impact**: Relying on standards not held in the laboratory library exposes AzureSky to non-conformances during SANAS assessments under Clause 7.2.1.2.
* **Decision Authority**: Laboratory Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---

### DEC-03: Sampling Scope Boundary for Washability Testing
* **Domain**: Scope of Testing & Statement of Conformity (Clause 5.3 & 7.3)
* **Context**: [`ASMF 5.3 Statement of Conformity REV 02`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%205/ASMF%205.3%20Statement%20of%20Conformity%20(Defining%20scope%20of%20work)%20REV%2002.docx#L30-L36) Section 5 explicitly excludes sampling from AzureSky's claimed scope of conformity and future accreditation ("Sampling is treated as a support activity and is not included within the laboratory's claimed scope of conformity").
* **Options**:
  1. *Option A (Recommended)*: Define CWP-001 washability testing strictly as a **Laboratory Testing Service on As-Received Samples**. Test reports will carry mandatory disclaimers that sampling was not performed by AzureSky and results apply only to the sample as received.
  2. *Option B*: Extend the capability project to establish an accredited field sampling service per ISO 18283 / ISO 13909.
* **Technical / Quality Impact**: Option A requires minimal QMS expansion and eliminates major field sampling liabilities. Option B requires vehicle/equipment capex, on-site sampling audits, and extensive sampler competency dossiers.
* **Decision Authority**: Laboratory Manager (S. Nyambi) / Project Owner
* **Status**: **PENDING REVIEW**

---

### DEC-04: Sample Preparation Flowsheet Architecture
* **Domain**: Process Control & Comminution Strategy (Clause 7.2.1)
* **Context**: [`AS001IW Rev 05`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS001IW%20PROCEDURE%20ON%20SAMPLE%20PREPARATION%20OF%20HARD%20COAL%20Rev%2005.docx) enforces crushing all received bulk coal through 25 mm $\to$ 10 mm $\to$ 3 mm crushers. If applied to washability, it destroys $+50\text{ mm}$ and $+25\text{ mm}$ lump coal before density separation.
* **Options**:
  1. *Option A (Recommended)*: Amend `AS001IW` to Rev 06 by adding a formal "Washability Preparation Branch" that screens and splits lump fractions *before* destructive comminution.
  2. *Option B*: Issue a dedicated, standalone procedure `AS017IW: Preparation of Hard Coal Samples for Washability and Size Analysis`.
* **Technical / Quality Impact**: Option A preserves single-SOP governance for preparation; Option B completely decouples commercial customer washability from CRM/PT production.
* **Decision Authority**: Technical Signatory (T. Maponya) / Lab Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---

### DEC-05: Product Drying Protocol & Temperature Gate
* **Domain**: Technical Method Defensibility (ISO 7936 Clause 8.5)
* **Context**: Current procedure [`AS013IW Rev 01`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS013IW%20FLOAT%20AND%20SINK%20WASHABILITY%20STANDARD%20OPERATING%20PROCEDURE.docx#L89) instructs analysts to "air-dry the floats until they are visibly dry". This subjective instruction allows variable retained moisture to distort fraction masses.
* **Options**:
  1. *Option A (Recommended)*: Mandate controlled forced-air thermal drying at $\le 40^\circ\text{C}$ in a dedicated drying oven until mass change is $< 0.1\%$ per hour. Preserves inherent moisture without thermal coal oxidation.
  2. *Option B*: Dry at $105\text{--}110^\circ\text{C}$ to constant dry mass. Faster, but alters coal oxidation state and volatilizes light hydrocarbons.
* **Technical / Quality Impact**: Option A complies fully with ISO 7936 Clause 8.5 for non-oxidised coal; requires oven capacity allocation (Mokopoledi oven `AS00111`).
* **Decision Authority**: Technical Signatory (T. Maponya)
* **Status**: **PENDING REVIEW**

---

### DEC-06: Correction of Particle Size Mass Loss Rule
* **Domain**: Mathematical Validity & Metrological Integrity (ISO 1953 Clause 9.2)
* **Context**: [`AS014IW Rev 01`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS014IW%20DETERMINATION%20OF%20PARTICLE%20SIZE%20DISTRIBUTION.docx#L45-L55) Section 5.2 forces all sieving mass loss into the fines receiver. This introduces positive systematic error into fines yield.
* **Options**:
  1. *Option A (Recommended)*: Amend Section 5.2 to distribute sieving mass loss proportionally across all size fractions if total loss is $\le 1.0\%$; reject test if loss exceeds $1.0\%$.
  2. *Option B*: Report unassigned mass loss as a distinct line item on the test report if $\le 1.0\%$.
* **Technical / Quality Impact**: Option A aligns directly with ISO 1953:2025 international practice and eliminates systematic fines bias.
* **Decision Authority**: Technical Signatory (T. Maponya) / Lab Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---

### DEC-07: Phase 1 Density Medium Selection
* **Domain**: Chemical Metrology, Safety & Environmental Compliance
* **Context**: [`AS013IW`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%207/7.2.%20SELECTION,%20VERIFICATION%20AND%20VALIDATION%20OF%20METHODS/7.2.1.%20SELECTION%20AND%20VERIFICATION%20OF%20METHODS/PROCEDURES/AS013IW%20FLOAT%20AND%20SINK%20WASHABILITY%20STANDARD%20OPERATING%20PROCEDURE.docx#L64) utilizes aqueous $\text{ZnCl}_2$ (RD 1.30–1.90). Study `CWP-001-DM-001` evaluated non-toxic alternatives (Sodium Polytungstate / LST).
* **Options**:
  1. *Option A (Recommended)*: Reaffirm aqueous $\text{ZnCl}_2$ as the authorized primary medium for Phase 1 coarse washability due to pre-existing stock and operational familiarity; mandate closed-circuit rinse recovery.
  2. *Option B*: Transition immediately to Sodium Polytungstate (SPT) or LST to eliminate chemical hazard and effluent disposal liabilities.
* **Technical / Quality Impact**: Option A requires strict Hazchem controls (OEL $1\text{ mg/m}^3$) and licensed hazardous waste disposal. Option B incurs substantially higher initial chemical purchase costs (~R 8,000/kg for SPT).
* **Decision Authority**: Project Owner / Laboratory Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---

### DEC-08: Physical Method Validation Campaign Scheduling
* **Domain**: Accreditation Evidence & Method Validation (Clause 7.2.2 & SANAS TR-26)
* **Context**: Document `CWP-001-VAL-001` contains unverified modeled benchmark figures. No physical Float-and-Sink validation trials have been conducted or witnessed on `Z:\`.
* **Options**:
  1. *Option A (Recommended)*: Authorize an official 3-week laboratory validation campaign: source 3 bulk coal lots (low, medium, high ash); perform 10 witnessed replicate separations; generate empirical mass loss and ash balance repeatability data under T. Maponya.
  2. *Option B*: Defer validation until commercial washability contracts are secured, running validation concurrently with the initial commercial batches.
* **Technical / Quality Impact**: Option A establishes defensible validation evidence prior to client reporting. Option B risks issuing unvalidated data contrary to ISO 17025 Clause 7.2.2.
* **Decision Authority**: Laboratory Manager (S. Nyambi) / Technical Signatory (T. Maponya)
* **Status**: **PENDING REVIEW**

---

### DEC-09: Equipment Register Asset Number Collisions & Ingestion
* **Domain**: Resource Management & Metrological Traceability (Clause 6.4)
* **Context**: Master register [`6.3 EQUIPMENT REGISTER.xlsx`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/17025/CLAUSE%206/EQUIPMENT/6.3%20EQUIPMENT%20REGISTER.xlsx) contains duplicate ID assignments (`AS8284` assigned to probe and crusher; `AS00111` assigned to oven and hygrometer) and omits hydrometers, separation baths, and test sieves.
* **Options**:
  1. *Option A (Recommended)*: Reassign unique asset IDs in `6.3 ER` (e.g. `AS8284-CR` for 25 mm crusher, `AS00111-HY` for CTS hygrometer); enter hydrometer set and test sieves with calibration intervals.
  2. *Option B*: Create a supplementary sub-register for washability equipment.
* **Technical / Quality Impact**: Option A maintains single-register governance per freeze protocol; Option B creates a shadow register violating [CWP-001_ARCHITECTURE_FREEZE.md Section 2](file:///c:/Projects/AzureSky/CWP-001/CWP-001_ARCHITECTURE_FREEZE.md#L63).
* **Decision Authority**: Laboratory Supervisor (T. Maponya) / Lab Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---

### DEC-10: Hazardous Chemical Waste Management Authorization
* **Domain**: Statutory Environmental Compliance (NEMWA Act 59 / GN R. 634)
* **Context**: [`AS009IW`](file:///Z:/AZURESKY%20SYSTEM/AZURESKY%20QMS/PROCEDURES/AS009IW%20WASTE%20MANAGEMENT%20PROCEDURE.docx) covers solid waste only. Washability operations generate zinc-bearing rinse effluent.
* **Options**:
  1. *Option A (Recommended)*: Authorize a Liquid Chemical Waste Addendum to `AS009IW`; approve capital for a 500 L closed-loop wash water settling tank; contract a licensed hazardous waste management provider (Class A/B disposal).
  2. *Option B*: Neutralize rinse effluent internally prior to municipal sewer discharge.
* **Technical / Quality Impact**: Discharging zinc solutions into municipal sewers is strictly prohibited under the National Water Act and municipal bylaws. Option A is legally mandatory for operational defensibility.
* **Decision Authority**: Operations Manager / Laboratory Manager (S. Nyambi)
* **Status**: **PENDING REVIEW**

---
*End of Mission 002 Decision Log.*
