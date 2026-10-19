# AS015IW: PROCEDURE ON THE DETERMINATION OF TOTAL MOISTURE IN HARD COAL
## Standard Operating Procedure for Single-Stage and Two-Stage Thermal Drying Methods
### AzureSky In-House Validated Method based on ISO 589:2008 and ISO 13909-4:2025

```
========================================================================================
Document ID:         AS015IW Rev 01
Replaces:            AS015IW Rev 00 (Effective 08/2025)
Document Type:       Controlled Standard Operating Procedure (Type C)
QMS Classification:  In-House Validated Test Procedure (ISO/IEC 17025:2017 Clause 7.2)
Governing Principles:ISO 589:2008 (Hard coal — Determination of total moisture)
                     ISO 13909-4:2025 (Coal — Preparation of test samples)
                     ISO 18283:2006 (Manual sampling)
Supporting SOPs:     AS001IW Rev 04 (Hard Coal Sample Preparation Procedure)
Associated Forms:    AS015TF-01 (Raw Data Sheet — Single-Stage Total Moisture)
                     AS015TF-02 (Raw Data Sheet — Two-Stage Total Moisture)
                     AS023TF (Verification Report — Drying Oven)
Decision Rules:      AS010IW (Statements of Conformity & Decision Rules per ISO 17025 Cl. 7.8.6)
Compiled By:         Tshepo Maponya — Laboratory Supervisor / Technical Signatory
Approved By:         Nonhlanhla Msibi — Operations Manager
Effective Date:      October 2026
Next Review Date:    October 2029
Revision Status:     01
Distribution:        Controlled Document — AzureSky Coal Laboratory
========================================================================================
```

---

## 1. Scope, Principle and Method Selection

### 1.1. Scope
This procedure specifies the gravimetric determination of total moisture in hard coal received at AzureSky Coal Laboratory. The method is applicable to run-of-mine (ROM) coal, washed product streams, borehole core samples, and customer consignment samples not susceptible to rapid thermal oxidation.

This procedure constitutes an **AzureSky In-House Validated Method** developed under ISO/IEC 17025:2017 Clause 7.2.2, grounded in the core thermodynamic principles of **ISO 589:2008** and the mechanical sample reduction principles of **ISO 13909-4:2025**.

### 1.2. Principle
The moisture content of coal is determined by measuring the loss in mass when the sample is heated in air at a controlled temperature of **$105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$** until constant mass is attained.

The laboratory operates two distinct analytical pathways:
* **Two-Stage Thermal Drying (Clauses 2, 3, and 4.1)**: Free (surface) moisture is determined by low-temperature air drying ($\le 40\ ^\circ\text{C}$), followed by comminution and determination of residual moisture at $105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$.
* **Single-Stage Thermal Drying (Clause 4.2)**: Total moisture is determined directly by single-stage thermal drying at $105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$ on coal reduced directly to nominal top-size $-10\text{ mm}$ (ISO 589 Method B2).

### 1.3. Method Selection and Sample Condition Criteria
The analyst shall apply the following laboratory criteria to select the determination pathway:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              METHOD SELECTION DECISION MATRIX                          │
├─────────────────────────┬───────────────────────────────┬──────────────────────────────┤
│ Incoming Sample State   │ Analytical Pathway            │ Technical Rationale          │
├─────────────────────────┼───────────────────────────────┼──────────────────────────────┤
│ • Unreduced bulk coal   │ TWO-STAGE DETERMINATION       │ Prevents uncontrolled loss   │
│   (nominal top-size     │ (Clauses 2, 3 and 4.1)        │ of moisture from milling     │
│   up to 50 mm);         │                               │ heat/air flow; prevents jaw  │
│ • Visibly wet, dripping,│                               │ crusher choking, caking, and │
│   or excessively moist; │                               │ screen blinding.             │
│ • Separated water in    │                               │                              │
│   sample container.     │                               │                              │
├─────────────────────────┼───────────────────────────────┼──────────────────────────────┤
│ • Free-flowing, dry     │ SINGLE-STAGE DETERMINATION    │ Allows direct oven drying    │
│   coal;                 │ (Clause 4.2; ISO 589          │ at -10 mm without Stage 1    │
│ • Prepared directly at  │  Method B2)                   │ air-drying delay.            │
│   nominal top-size      │                               │                              │
│   -10 mm.               │                               │                              │
└─────────────────────────┴───────────────────────────────┴──────────────────────────────┘
```

> [!IMPORTANT]
> **Separation of Water in Containers (ISO 13909-4 & ISO 589 Clause 7.5)**:
> If the coal sample is so wet that free water separates inside the sample container during transit, the whole sample and its container shall be air-dried together until this condition no longer applies. The loss in mass is recorded and incorporated into the first-stage moisture calculation.

---

## 2. Sample Reception, Mass and Primary Division

### 2.1. Incoming Sample Specifications and Division
1. **Traceability**: Record consignment details in the Sample Receiving Book and generate a unique LIMS barcode.
2. **Maximum Nominal Top-Size Acceptance Limit**:
   * Per [AS001IW Clause 4.1](file:///c:/Projects/AzureSky/Total-Moisture/AS001IW%20PROCEDURE%20ON%20SAMPLE%20PREPARATION%20OF%20HARD%20COAL%20Rev%2004.pdf), the nominal top-size of incoming bulk samples accepted by the laboratory **shall not exceed $50\text{ mm}$**.
   * Samples exceeding $50\text{ mm}$ must be flagged and referred to the Laboratory Supervisor prior to comminution.
3. **Minimum Bulk Sample Mass Requirement (ISO 13909-4:2025 Table 1)**:
   * For a $50\text{ mm}$ nominal top-size bulk coal sample, the minimum sample mass required after division to ensure sampling representativeness is **$35\text{ kg}$**.
   * *Critical Distinction*: The $35\text{ kg}$ specification represents the minimum required mass of the divided bulk sample to maintain sampling precision; it is distinct from the mass placed on individual drying pans.
4. **Primary Division by Cone and Quartering**:
   * Form the bulk sample into an even cone on a clean, impervious floor.
   * Flatten the apex uniformly and divide into four equal quarters.
   * Select one quarter.
   * **Representativeness Rule**: If the mass of the chosen single quarter is less than the mandatory **$35\text{ kg}$**, the analyst must **combine two opposite quarters** to ensure statistical representativeness.
5. **Initial "As Received" Bulk Mass ($m_1$ / $m_{1,\text{bulk}}$)**:
   * Immediately weigh the divided bulk sample on the calibrated platform balance to the nearest $0.01\text{ kg}$.
   * Capture and lock $m_1$ on LIMS and log it on raw data sheet [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx).

---

### 2.2. Stage 1: Air Drying (Free / Surface Moisture)

1. **Spreading & Tray Loading**:
   * Spread the divided sample thinly and evenly over clean, dry, tared drying pans.
   * In accordance with ISO 589 Clause 6.3.1, the layer loading of coal **shall not exceed $1\text{ g/cm}^2$**. If the sample volume is large, use multiple trays.
2. **Drying Conditions & Oxidation Safeguard**:
   * Air dry the sample at ambient laboratory temperature or in a dedicated fan-forced oven **not exceeding $40\ ^\circ\text{C}$** until visibly dry.
   * **Temperature Restriction ($\le 40\ ^\circ\text{C}$)**: Under ISO 589 Clause 6.1.1 and Clause 8.1.1, the drying temperature must strictly NOT exceed $40\ ^\circ\text{C}$. Temperatures above $40\ ^\circ\text{C}$ accelerate thermal oxidation of the coal matrix, resulting in chemisorption of atmospheric oxygen, mass gain, and severe negative analytical bias.
   * **Ambient Re-equilibration**: When a heated drying oven ($\le 40\ ^\circ\text{C}$) is used, the coal sample **must re-equilibrate to ambient laboratory temperature** before re-weighing (ISO 589 Clause 8.1.1).
3. **Constant-Mass & Stability Criteria**:
   * **ISO 589 Normative Constant-Mass Definition**: Constant mass is achieved when the change in mass does not exceed **$0.2\%$ absolute** during a further drying period of not less than $25\%$ of the initial drying duration.
   * **AzureSky Operational Criterion on LIMS**: In routine daily laboratory throughput, air drying is declared complete when the consecutive mass loss between check weighings is **less than $0.1\text{ g}$** ($< 0.1\text{ g}$).
4. **Final Air-Dried Bulk Mass ($m_2$ / $m_{2,\text{bulk}}$)**:
   * Record the final air-dried bulk mass ($m_2$, in kg) on LIMS and [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx).

---

## 3. Sub-Sampling and Comminution (Crushing Sequence)

### 3.1. Crushing Sequence
Comminution shall be conducted rapidly using validated jaw crushers. High-speed grinding mills must never be used.

* **Step 1 (Primary Crush)**: Pass the air-dried sample through the **$25\text{ mm}$ jaw crusher**.
* **Step 2 (Division)**: Use a clean, properly sized **Riffle Splitter** to reduce sample mass between crushing stages.
* **Step 3 (Secondary Comminution)**:
  * **For Single-Stage**: Crush sample to nominal top-size **$-10\text{ mm}$**.
  * **For Two-Stage (AzureSky Validated Procedure)**: Crush sample to **$-3\text{ mm}$** using the calibrated fine crusher.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│             METHOD VALIDATION NOTE: TWO-STAGE TEST PORTION & TOP-SIZE                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ISO 589:2008 Clause 8.1.2 (Method A2) specifies reduction to 2.8 mm nominal top-size   │
│ with micro test portions of (10 ± 1) g in shallow dishes (loading ≤ 0.3 g/cm²).         │
│                                                                                        │
│ AzureSky operates an In-House Validated Macro-Procedure (ISO 17025 Cl. 7.2.2):         │
│ Air-dried coal is crushed to -3 mm, and duplicate test portions of 1 kg each are dried │
│ in large pans. This macro test portion significantly reduces subsampling variance on   │
│ heterogeneous industrial coals. The procedure has been validated against the micro     │
│ method and proven fit-for-purpose under AzureSky QA/QC protocols.                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.2. Final Preparation of Duplicate Pans
* **Step 4 (Riffling)**: Riffle the $-3\text{ mm}$ crushed coal to achieve representative portions of **$1\text{ kg}$ per riffled side**.
* **Step 5 (Duplicate Pans)**: Prepare two clean, dry moisture pans. Tare each pan on the LIMS-interfaced balance. Transfer approximately $1\text{ kg}$ into **Pan A** and $1\text{ kg}$ into **Pan B**. Immediately capture the initial net sample mass ($m_3$, in grams) on LIMS and [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx).

---

## 4. Oven Drying (Residual and Single-Stage Moisture)

### 4.1. Two-Stage Residual Moisture ($-3\text{ mm}$ AzureSky Macro Procedure)
1. **Oven Operating Conditions**: Place duplicate pans in the oven pre-heated to **$105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$**. Oven air circulation shall provide a minimum of 5 atmosphere changes per hour (ISO 589 Clause 6.1.3).
2. **Initial Drying Interval**: Dry continuously for **3.0 hours**.
3. **Intermediate Weighing**: Remove pans after 3 hours, capture mass on LIMS, and return pans to the oven for a further **30 minutes**.
4. **Constant-Mass & Stability Criteria**:
   * **ISO 589 Normative Constant-Mass**: Mass change $\le 0.2\%$ absolute over $\ge 25\%$ additional drying duration.
   * **AzureSky Operational Criterion on LIMS**: The sample status reads **"stable"** on LIMS when the mass loss between consecutive 30-minute intervals is **$\le 0.1\text{ g}$**.
   * Record the final net stabilized dried mass ($m_4$, in grams) on LIMS and [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx).
5. **Maximum Oven Limit & Failure Action**:
   * If the sample fails to stabilize within **$5.0\text{ hours}$** of total oven residence time, the test is marked as **"Failed"** in LIMS.
   * **Action**: The test is invalidated and must be completely repeated using a backup split from the $-3\text{ mm}$ retained sample.

---

### 4.2. Single-Stage Total Moisture ($-10\text{ mm}$ Coal — ISO 589 Method B2)
1. **Sample Portions & Loading**:
   * Per ISO 589 Clause 8.2.1, extract at least two duplicate test portions of **minimum $600\text{ g}$ each** (AzureSky routinely uses duplicate $\sim 1000\text{ g}$ charges) from the $-10\text{ mm}$ sample.
   * Spread evenly on clean trays such that coal layer loading **does not exceed $1\text{ g/cm}^2$**.
2. **Drying Conditions & Constant Mass**:
   * Place trays in the drying oven controlled at **$105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$**.
   * Heat until constant mass is attained (normative criterion: change $\le 0.2\%$ absolute). In AzureSky routine operations, a continuous duration of **$5.0\text{ hours}$** is applied, confirmed by constant mass.
3. **Hot Weighing Protocol (ISO 589 Clause 8.2.1)**:
   * Remove trays from the oven and weigh while hot as soon as possible (**within 5 minutes**) to prevent moisture adsorption from cooling air.
4. **Mass Recording**:
   * Record empty tray tare ($m_1$), gross initial mass before drying ($m_2$), and gross dried mass ($m_3$) on LIMS and [AS015TF-01](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-01%20Raw%20Data%20Sheet%20-%20Single-Stage%20Total%20Moisture.docx).

---

## 5. Calculations and Standardized Variable Definitions

To eliminate variable naming conflicts across laboratory forms, the nomenclature for Single-Stage and Two-Stage calculations is strictly segregated:

### 5.1. Surface (Free / Air-Dry) Moisture ($M_{ar}$) — Two-Stage Stage 1
$$M_{ar} = \left( \frac{m_1 - m_2}{m_1} \right) \times 100$$
Where (per [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx)):
* $m_1$ = Initial bulk sample mass as received ($kg$).
* $m_2$ = Mass of bulk sample after Stage 1 air drying ($kg$).

*Calculation Example (Assessment Q10)*:
$$\text{Given } m_1 = 35.00\text{ kg}, \, m_2 = 32.55\text{ kg} \implies M_{ar} = \left( \frac{35.00 - 32.55}{35.00} \right) \times 100 = \left( \frac{2.45}{35.00} \right) \times 100 = \mathbf{7.00\%}$$

---

### 5.2. Residual Moisture ($M_{res}$) — Two-Stage Stage 2
Calculated for each duplicate pan:
$$M_{res} = \left( \frac{m_3 - m_4}{m_3} \right) \times 100$$
Where (per [AS015TF-02](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-02%20Raw%20Data%20Sheet%20-%20Two-Stage%20Total%20Moisture.docx)):
* $m_3$ = Initial net mass of $-3\text{ mm}$ test sample before oven drying ($\sim 1000\text{ g}$ net charge, in $g$).
* $m_4$ = Final net stabilized mass of test sample after oven drying ($g$).

---

### 5.3. Total Moisture ($TM$) Equations

#### A. Two-Stage Total Moisture (ISO 589 Equation 3)
$$TM = M_{ar} + \frac{(100 - M_{ar}) \times M_{res}}{100}$$

* **ISO 589 Calculation Flow**: Calculates $TM_A$ for Pan A and $TM_B$ for Pan B individually, then reports the mean:
  $$TM_{\text{report}} = \frac{TM_A + TM_B}{2}$$
* **AzureSky LIMS Calculation Flow**: Averages the duplicate residual moistures first ($M_{res,\text{avg}} = \frac{M_{res,A} + M_{res,B}}{2}$) and inserts directly into the $TM$ equation:
  $$TM_{\text{LIMS}} = M_{ar} + \frac{(100 - M_{ar}) \times M_{res,\text{avg}}}{100}$$
* *Mathematical Equivalence*: Because the equation is linear, both methods yield identical numerical results and both are approved under AzureSky QMS.

#### B. Single-Stage Total Moisture (ISO 589:2008 Clause 8.2.3 Equation 5)
$$TM = \left( \frac{m_2 - m_3}{m_2 - m_1} \right) \times 100$$
Where (per [AS015TF-01](file:///c:/Projects/AzureSky/Total-Moisture/AS015TF-01%20Raw%20Data%20Sheet%20-%20Single-Stage%20Total%20Moisture.docx)):
* $m_1$ = Mass of empty, clean, dry drying tray tare ($g$).
* $m_2$ = Gross mass of drying tray plus test sample before oven drying ($g$).
* $m_3$ = Gross mass of drying tray plus test sample after oven drying ($g$).
* Net initial sample mass = $(m_2 - m_1)$; Net moisture loss = $(m_2 - m_3)$.

---

## 6. Precision Limits and AzureSky Decision Rules

### 6.1. ISO 589 Normative Precision Limits (ISO 589 Table 1)
```
┌───────────────────────────────────────┬──────────────────────┬────────────────────────┐
│ Property                              │ Repeatability Limit  │ Reproducibility Limit  │
│                                       │ (r, Same Operator)   │ (R, Different Labs)    │
├───────────────────────────────────────┼──────────────────────┼────────────────────────┤
│ Second-Stage Moisture (M_res)         │ 0.30 %               │ Not Applicable         │
│ Total Moisture (TM)                   │ 0.50 %               │ 1.50 %                 │
└───────────────────────────────────────┴──────────────────────┴────────────────────────┘
```

### 6.2. AzureSky Laboratory Decision Rule (ISO/IEC 17025 Clause 7.8.6 / AS010IW)
To ensure that only valid, traceable data is released to clients, AzureSky enforces an automated **LIMS Repeat Decision Rule**:
1. **Second-Stage Duplicate Check**:
   $$\Delta M_{res} = |M_{res,A} - M_{res,B}|$$
   * If $\Delta M_{res} \le 0.30\%$: Meets repeatability. Result approved.
   * If $\Delta M_{res} > 0.30\%$: LIMS triggers a **"REPEAT ALERT"**.
2. **Total Moisture Duplicate Check**:
   $$\Delta TM = |TM_A - TM_B|$$
   * If $\Delta TM > 0.50\%$: Exceeds total moisture repeatability limit.
3. **Mandatory Retest Action**:
   * A Repeat Alert automatically locks the job from authorization.
   * The test portion is invalidated.
   * The analyst must re-riffle fresh duplicate test portions from the retained sample and repeat the determination.

*Worked Example (Assessment Q11)*:
Pan A $M_{res} = 4.20\%$, Pan B $M_{res} = 4.58\% \implies |4.58\% - 4.20\%| = 0.38\%$. Since $0.38\% > 0.30\%$, the pair fails repeatability. LIMS triggers a REPEAT ALERT and the test is repeated.

---

## 7. Equipment Metrology and Verification Controls

Equipment verification must strictly comply with the approved laboratory control forms and schedules under ISO/IEC 17025 Clause 6.4:

1. **Moisture Drying Oven ([AS023TF Rev 00](file:///c:/Projects/AzureSky/Total-Moisture/AS023TF-ISO%20MOISTURE%20OVEN%20VERIFICATION%20-.pdf))**:
   * **Frequency**: Daily before use.
   * **Method**: Calibrated thermocouple reading (Average of 3 readings + Thermocouple Correction Factor) evaluated against the oven indicator set point and verified within the working tolerance limit of **$105\ ^\circ\text{C}$ to $110\ ^\circ\text{C}$** (nominal setpoint $\le 107\ ^\circ\text{C}$).
2. **Crusher Sieve Efficiencies ([AS001IW Rev 04 Clause 4.1](file:///c:/Projects/AzureSky/Total-Moisture/AS001IW%20PROCEDURE%20ON%20SAMPLE%20PREPARATION%20OF%20HARD%20COAL%20Rev%2004.pdf))**:
   * **Coarse Crushers ($25\text{ mm}$ and $10\text{ mm}$)**: Efficiency check conducted **every Monday at the beginning of the shift** before work commences.
   * **Fine Crushers ($3\text{ mm}$ and $4.75\text{ mm}$)**: Efficiency check conducted **on the day of use, immediately before using the crusher**.
3. **Balances**: Daily verification using calibrated check weights ($1000.0\text{ g} \pm 0.1\text{ g}$).

---

## 8. Revision History Table

| Revision No. | Effective Date | Reason for Revision & Key Changes | Author / Approval |
| :---: | :---: | :--- | :--- |
| **00** | 08/2025 | Initial creation and implementation of laboratory test procedure. | T. Maponya / N. Msibi |
| **01** | 10/2026 | Technical revision and standardization:<br>1. Standardized variable notation: isolated Single-Stage variables ($m_1$ = tare, $m_2$ = gross initial, $m_3$ = gross dried per ISO 589 Cl. 8.2.3 and AS015TF-01) from Two-Stage variables ($m_1, m_2$ bulk; $m_3, m_4$ net).<br>2. Formally documented AzureSky in-house validated macro-pan procedure ($1\text{ kg}$ at $-3\text{ mm}$) alongside ISO 589:2008 normative criteria.<br>3. Aligned bulk preparation with ISO 13909-4:2025 Table 1 ($35\text{ kg}$ min mass at $50\text{ mm}$) and documented free water separation handling.<br>4. Incorporated ISO 589 constant-mass definitions ($\le 0.2\%$ over $\ge 25\%$ duration) and ambient re-equilibration requirements for air drying ($\le 40\ ^\circ\text{C}$).<br>5. Differentiated ISO 589 normative precision limits from AzureSky internal LIMS repeat decision rules (AS010IW).<br>6. Aligned equipment controls with AS023TF and AS001IW. | T. Maponya / N. Msibi |
