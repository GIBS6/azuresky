# AZCA-015: OPERATOR STUDY & EXAM PREPARATION GUIDE
## Determination of Total Moisture in Hard Coal (Single-Stage & Two-Stage)

```
========================================================================================
Training Module:      AZCA-015 Technical Competency
Target SOP:           AS015IW Rev 01 (Determination of Total Moisture)
Governing Standards:  ISO 589:2008 | ISO 13909-4:2025 | ISO 17025:2017
Pass Mark:            80% (20 / 25 points) + 100% on Critical Questions (*5 and *6)
Critical Gate Policy: ZERO-TOLERANCE on Q5 and Q6 (Immediate stoppage if incorrect)
Target Audience:      Coal Laboratory Analysts, Preparation Technicians, Technical Signatories
========================================================================================
```

---

## 1. Quick Overview: Why and How We Measure Total Moisture

Coal moisture directly impacts commercial valuation, energy content (Calorific Value), transport costs, and plant handling.

```
Total Moisture (TM) = Surface (Free) Moisture (Stage 1) + Residual Moisture (Stage 2)
```

* **Surface (Free) Moisture ($M_{ar}$)**: Water on the exterior surface of coal particles. Measured by air drying bulk coal at low temperature ($\le 40\ ^\circ\text{C}$).
* **Residual Moisture ($M_{res}$)**: Water retained inside the coal pores and capillaries. Measured by oven drying $-3\text{ mm}$ coal at $105\ ^\circ\text{C} - 110\ ^\circ\text{C}$ in AzureSky's in-house validated macro-pan method.
* **Single-Stage Moisture**: Direct oven drying of $-10\text{ mm}$ coal for 5 hours when coal is already dry and free-flowing (ISO 589 Method B2).

---

## 2. THE TWO ZERO-TOLERANCE CRITICAL QUESTIONS

> [!CAUTION]
> **ASSESSMENT STOPPAGE RULE**: In AZCA-015, if you miss even one detail in Question *5 or Question *6, the test stops immediately and you receive a **NOT YET COMPETENT** grade. Memorize these two questions thoroughly.

---

### Critical Question *5: The 5-Step Procedural Sequence (5 Marks — Must be 100% Correct)

You must be able to list these **5 steps in exact sequential order**:

```
Step 1: Spread 35 kg sample thinly on clean drying pans until "visibly dry" 
        (at ambient room temperature or fan-forced oven ≤ 40 °C; layer loading ≤ 1 g/cm²).

Step 2: Perform Stage 1 stability check on LIMS: air drying is complete when 
        consecutive mass loss is < 0.1 g (ISO constant-mass: change ≤ 0.2% absolute).

Step 3: Primary crush the air-dried coal through the 25 mm crusher, then reduce 
        mass using the clean Riffle Splitter.

Step 4: Secondary crush the sample:
        • Crush to -10 mm for Single-Stage determination, OR
        • Crush to -3 mm for Two-Stage determination (AzureSky macro-pan method).

Step 5: Final division using the Riffle Splitter to achieve 1 kg per side, 
        tare moisture pans on the balance, transfer into duplicate 
        Pan A and Pan B, and capture initial mass m3 on LIMS.
```

---

### Critical Question *6: Oven Temperature & Stability Timing (2 Marks — Must be 100% Correct)

You must state the exact numbers:

```
1. Exact Operating Temperature Range (1 Mark):
   105 °C to 110 °C (Nominal setpoint ≤ 107 °C)

2. Initial Drying Duration & Stability Criterion (1 Mark):
   • Initial drying: dry continuously for 3 hours before first weighing.
   • Check interval: return pans to the oven for 30 minutes at a time.
   • Stability criterion: the sample is stable when the mass loss between 
     consecutive 30-minute intervals is ≤ 0.1 g.
```

---

## 3. High-Yield Question Guide: Questions 1 to 12 (Total: 25 Marks)

### Question 1: Method Selection & Principle [2 Marks]
* **What are the two methods?** Single-Stage and Two-Stage thermal drying (1 pt).
* **When is Two-Stage required?** When coal is **visibly wet, dripping, or excessively moist**, where free water separates in the transit container (air-dried with container per ISO 13909-4 / ISO 589 Clause 7.5), or when particle size/bulk mass makes direct crushing prone to moisture loss by evaporation or mechanical choking/blinding of the crusher (1 pt).

### Question 2: Sample Mass & Top-Size [2 Marks]
* **Minimum bulk sample mass for $50\text{ mm}$ top-size**: **$35\text{ kg}$** per ISO 13909-4:2025 Table 1 (1 pt).  
  *(Note: This $35\text{ kg}$ is the divided bulk sample mass required for representativeness, not the drying pan charge).*
* **Maximum nominal top-size accepted by the lab**: **$\le 50\text{ mm}$** per AS001IW Clause 4.1 (1 pt).

### Question 3: Cone & Quartering Rule [2 Marks]
* **Procedure**: Form coal into a cone, flatten the top, divide into four equal quarters, select one quarter (1 pt).
* **If mass $< 35\text{ kg}$**: Combine **two opposite quarters** to ensure statistical representativeness (1 pt).

### Question 4: Stage 1 Temperature & Oxidation Rationale [2 Marks]
* **Temperature limit & re-equilibration**: Ambient or fan-forced oven **$\le 40\ ^\circ\text{C}$**. When a heated oven is used, the coal must **re-equilibrate to ambient temperature before re-weighing** (1 pt).
* **Why not $> 40\ ^\circ\text{C}$?** High temperatures accelerate **thermal oxidation** of coal. Oxidation causes atmospheric oxygen to chemically chemisorb onto the coal matrix, causing **mass gain**, which artificially suppresses calculated moisture loss and leads to severe negative analytical bias (1 pt).

### Question 7: Oven Failure Limit [1 Mark]
* **Maximum allowable drying time**: **5.0 hours** (0.5 pt).
* **Mandatory Action**: If sample fails to stabilize within 5 hours, LIMS marks the test as **"Failed"**. The test is invalidated and must be completely repeated with a backup split from the $-3\text{ mm}$ retained sample (0.5 pt).

### Question 8: Single-Stage vs Two-Stage Oven Drying [1 Mark]
* In **Single-Stage ($-10\text{ mm}$)**, duplicate test portions ($\ge 600\text{ g}$, routine $\sim 1000\text{ g}$) remain in the oven for the **full 5-hour duration continuously** without any 3-hour check.
* **Hot weighing requirement**: Trays must be removed and weighed while hot as soon as possible (**within 5 minutes** per ISO 589 Clause 8.2.1) to avoid atmospheric moisture re-adsorption (1 pt).

### Question 9: Equipment Verification Controls [2 Marks]
* **Moisture Oven ([AS023TF](file:///c:/Projects/AzureSky/Total-Moisture/AS023TF-ISO%20MOISTURE%20OVEN%20VERIFICATION%20-.pdf))**: Daily verified before use using a calibrated thermocouple ($\text{Average of 3 Readings} + \text{Correction Factor}$) evaluated within $105\ ^\circ\text{C} - 110\ ^\circ\text{C}$ (indicator setpoint target $\le 107\ ^\circ\text{C}$) (1 pt).
* **Crusher Efficiency ([AS001IW Clause 4.1](file:///c:/Projects/AzureSky/Total-Moisture/AS001IW%20PROCEDURE%20ON%20SAMPLE%20PREPARATION%20OF%20HARD%20COAL%20Rev%2004.pdf))**:
  * Coarse crushers ($25\text{ mm}$ and $10\text{ mm}$): **Every Monday at the start of shift before work commences** (0.5 pt).
  * Fine crushers ($3\text{ mm}$ and $4.75\text{ mm}$): **On the day of use, immediately before using the crusher** (0.5 pt).

### Question 10: Surface (Free) Moisture Calculation [2 Marks]
* **Formula & Definitions**:
  $$M_{ar} = \left(\frac{m_1 - m_2}{m_1}\right) \times 100$$
  where $m_1$ = initial bulk sample mass as received ($kg$), $m_2$ = air-dried bulk mass ($kg$) (1 pt).
* **Calculation with given numbers**:
  * $m_1 = 35.00\text{ kg}$ (as received)
  * $m_2 = 32.55\text{ kg}$ (air dried)
  $$M_{ar} = \left(\frac{35.00 - 32.55}{35.00}\right) \times 100 = \left(\frac{2.45}{35.00}\right) \times 100 = \mathbf{7.00\%} \quad (1\text{ pt})$$

### Question 11: Repeatability Limits & LIMS Repeat Alert [2 Marks]
* **Given**: Pan A $M_{res} = 4.20\%$, Pan B $M_{res} = 4.58\%$.
* **Difference calculation & compliance**: $|4.58\% - 4.20\%| = 0.38\%$. The repeatability limit for 2nd stage moisture is **$0.30\%$**. Since $0.38\% > 0.30\%$, it **DOES NOT COMPLY** (1 pt).
* **LIMS Alert & Action**: LIMS triggers an automated **"REPEAT ALERT"**. Results are quarantined, the test is invalidated, and the analyst must re-split and re-run the determination from retained sample (1 pt).

### Question 12: LIMS vs. ISO 589 Calculation Alignment [2 Marks]
* **Calculation difference**:
  * **AzureSky LIMS**: Averages duplicate residual moistures first ($M_{res,\text{avg}}$) and plugs it directly into the $TM$ formula: $TM = M_{ar} + \frac{(100 - M_{ar}) \times M_{res,\text{avg}}}{100}$ (1 pt).
  * **ISO 589 Standard**: Calculates $TM$ for Pan A and Pan B separately, then averages them at the very end: $TM = \frac{TM_A + TM_B}{2}$.
* **Are both accepted?** **YES**. Because the mathematical equation is linear, both methods yield identical numerical results, and both are approved under AzureSky QMS (1 pt).

---

## 4. Responsible Self-Test Scoring Matrix

| Question | Topic | Points | Responsible Sub-Mark Breakdown |
| :---: | :--- | :---: | :--- |
| **Q1** | Method Selection | **2** | 1 pt: Single & Two-Stage; 1 pt: wet coal / choking conditions |
| **Q2** | Min Mass & Max Top Size | **2** | 1 pt: $35\text{ kg}$ min mass; 1 pt: $\le 50\text{ mm}$ lab limit |
| **Q3** | Cone & Quartering Rule | **2** | 1 pt: 4 quarters method; 1 pt: combine 2 opposite quarters if $< 35\text{ kg}$ |
| **Q4** | Air-Drying Temp & Rationale | **2** | 1 pt: $\le 40\ ^\circ\text{C}$ & re-equilibration; 1 pt: thermal oxidation mass gain |
| **Q5\*** | **CRITICAL: 5-Step Procedural Flow** | **5\*** | **1 pt each for all 5 steps in correct order (Zero tolerance!)** |
| **Q6\*** | **CRITICAL: Temp & Stability Timing** | **2\*** | **1 pt: $105-110\ ^\circ\text{C}$ range; 1 pt: $3\text{ h}$ initial, $30\text{ m}$ check, $\le 0.1\text{ g}$** |
| **Q7** | Max Oven Time & Failure Action | **1** | 0.5 pt: $5\text{ hours}$ max; 0.5 pt: mark Failed in LIMS and repeat |
| **Q8** | Single-Stage Oven Residence | **1** | 0.5 pt: $5\text{ hours}$ continuous; 0.5 pt: weigh hot within $5\text{ minutes}$ |
| **Q9** | Equipment Verification Schedules | **2** | 1 pt: oven thermocouple check; 1 pt: Monday & Day-of-use crusher checks |
| **Q10** | Free Moisture Formula & Math | **2** | 1 pt: formula with defined variables; 1 pt: worked math to $7.00\%$ |
| **Q11** | Repeatability Check & LIMS Alert | **2** | 1 pt: $|0.38\%| > 0.30\%$ fails; 1 pt: LIMS Repeat Alert & retest |
| **Q12** | LIMS vs ISO 589 Alignment | **2** | 1 pt: explain calculation difference; 1 pt: confirm mathematical equivalence |
| **TOTAL** | | **25** | **Passing Mark: Minimum 20 / 25 (80%) AND 100% on Q5 & Q6** |
