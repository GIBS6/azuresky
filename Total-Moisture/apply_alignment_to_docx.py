import sys
import docx
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

def create_omml_equation(xml_string):
    """Parses raw OMML XML into an oxml element."""
    return parse_xml(xml_string)

def run_update():
    doc = docx.Document('_ Draft.docx')
    
    # -------------------------------------------------------------
    # 1. Update Footer (Rev 01, Date 10/2026, Next rev 10/2029)
    # -------------------------------------------------------------
    for section in doc.sections:
        footer = section.footer
        for table in footer.tables:
            for row in table.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        for r in p.runs:
                            if '00' in r.text:
                                r.text = r.text.replace('00', '01')
                            if '10/2025' in r.text:
                                r.text = r.text.replace('10/2025', '10/2026')
                            if '10/2028' in r.text:
                                r.text = r.text.replace('10/2028', '10/2029')

    # -------------------------------------------------------------
    # 2. Modify Paragraphs in Document
    # -------------------------------------------------------------
    # We inspect paragraphs by their index or content
    for p in doc.paragraphs:
        t = p.text.strip()
        
        # Section 1 Scope and Principle
        if t.startswith('This method describes the determination of total moisture'):
            p.text = (
                "This method describes the determination of total moisture in hard coal using a two-stage or "
                "single-stage thermal drying process in air. Moisture is determined by the loss in mass of the "
                "sample when heated in air at 105 ºC to 110 °C until constant mass is attained."
            )
        elif t.startswith('Reference Standards:'):
            p.text = (
                "Reference Standards: ISO 589:2008 (Methods A2 and B2), ISO 13909-4:2025, ISO 18283, AS001IW, AS023TF.\n\n"
                "Method Selection Criteria:\n"
                "• Two-Stage Determination (Mandatory): Required when the coal is visibly wet, dripping, or excessively moist, "
                "or when particle size/mass makes single-stage drying impractical or prone to moisture loss by evaporation and "
                "crusher choking during preparation.\n"
                "• Single-Stage Determination: Applicable to free-flowing, drier coal crushed directly to nominal top-size -10 mm."
            )
            
        # Section 2.1 Primary Split
        elif t.startswith('Obtain the primary bulk sample.'):
            p.text = (
                "1. Sample Acceptance: The nominal top-size of incoming coal accepted by the laboratory shall not exceed 50 mm "
                "(AS001IW Cl. 4.1). For a 50 mm top-size bulk sample, the minimum required mass is 35 kg (ISO 13909-4 Table 1)."
            )
        elif t.startswith('Cone and Quartering:'):
            p.text = (
                "2. Cone and Quartering: Form the coal into a cone, flatten the top uniformly, and divide into four quarters."
            )
        elif t.startswith('Select one quarter.'):
            p.text = (
                "3. Division & Representativeness: Select one quarter. If the mass of the chosen single quarter is less than the required 35 kg "
                "for a 50 mm top-size, take two opposite quarters to ensure statistical representativeness."
            )
        elif t.startswith('Initial Mass (m_1):'):
            p.text = (
                "4. Initial Mass (m_1): Immediately weigh the split sample on the calibrated balance and record the mass on LIMS and "
                "AS015TF-02. This is the initial \"As Received\" weight (m_1)."
            )
            
        # Section 2.2 Stage 1 Air Drying
        elif t.startswith('Spread the 35 kg sample thinly'):
            p.text = (
                "1. Spreading: Spread the 35 kg sample thinly on clean drying pans (coal layer loading ≤ 1 g/cm² per ISO 589)."
            )
        elif t.startswith('Allow the sample to air dry at ambient'):
            p.text = (
                "2. Drying Conditions: Allow the sample to air dry at ambient temperature (or in a fan-forced oven not exceeding 40 °C) "
                "until \"visibly dry.\"\n"
                "Note / Rationale: The drying temperature must strictly NOT exceed 40 °C to prevent coal oxidation (especially in lower-rank coals). "
                "Temperatures > 40 °C promote chemical oxygen chemisorption and mass gain, resulting in severe negative analytical bias."
            )
        elif t.startswith('Stability Check:'):
            p.text = (
                "3. Stability Check: Weigh the pans back on LIMS. Air drying is complete when the mass loss between successive checks is "
                "less than 0.1 g (< 0.1 g)."
            )
        elif t.startswith('Record the final air-dried mass (m_2).'):
            p.text = (
                "4. Final Air-Dried Mass (m_2): Record the final air-dried mass (m_2) on LIMS and AS015TF-02."
            )
            
        # Section 3 Sub-Sampling & Crushing (Crushing Sequence)
        elif t.startswith('Primary Crush:'):
            p.text = "• Step 1 (Primary Crush): Pass the air-dried sample through the 25 mm crusher."
        elif t.startswith('Division: Use a Riffle Splitter'):
            p.text = "• Step 2 (Division): Use a clean Riffle Splitter to reduce the mass in between stage crushing."
        elif t.startswith('Secondary Crush:'):
            p.text = "• Step 3 (Secondary Crush):"
        elif t.strip() == 'For Single-Stage: Crush to -10 mm.':
            p.text = "    - For Single-Stage: Crush to -10 mm."
        elif t.strip() == 'For Two-Stage: Crush to -3 mm.':
            p.text = "    - For Two-Stage: Crush to -3 mm."
            
        # Section 3.2 Final Preparation
        elif t.startswith('Riffle the crushed material'):
            p.text = "• Step 4 (Riffling): Riffle the crushed material to achieve a sample of 1 kg per riffled side."
        elif t.startswith('Duplicate Pans:'):
            p.text = "• Step 5 (Duplicate Pans): Prepare two clean, dry moisture pans. Tare each pan on the LIMS-connected balance."
        elif t.startswith('Transfer the 1 kg sub-sample'):
            p.text = (
                "• Transfer & Initial Mass (m_3): Transfer the 1 kg sub-sample into the tared pans and immediately capture the initial net mass (m_3) "
                "on LIMS for both Pan A and Pan B."
            )
            
        # Section 4 Oven Drying
        elif t.startswith('Place pans in the oven at 105'):
            p.text = "1. Place duplicate pans in the oven pre-heated to 105 °C to 110 °C (nominal setpoint ≤ 107 °C)."
        elif t.startswith('Initial Interval:'):
            p.text = "2. Initial Interval: Dry continuously for 3 hours."
        elif t.startswith('First Weighing:'):
            p.text = "3. First Weighing: Capture mass on LIMS after 3 hours, then return to oven for 30 minutes."
        elif t.startswith('Stability Criteria:'):
            p.text = (
                "4. Stability Criteria: If mass loss between consecutive 30-minute intervals is ≤ 0.1 g, the sample will read "
                "\"stable\" in LIMS, signaling that drying is complete. Capture final stabilized mass (m_4) on LIMS."
            )
        elif t.startswith('Failure Limit:'):
            p.text = (
                "5. Failure Limit: If the sample does not stabilize within 5 hours, the test is marked as \"Failed\" in LIMS, "
                "the test is invalidated, and it must be repeated completely using a backup split."
            )
            
        # Section 4.2 Single-Stage Moisture
        elif t.startswith('Follow the same procedure as above, but the sample remains'):
            p.text = (
                "1. Duplicate 1 kg portions crushed to -10 mm are placed in the oven at 105 °C to 110 °C.\n"
                "2. The sample remains in the oven for the full 5-hour duration continuously, without the 3-hour initial lapse check.\n"
                "3. Remove pans and weigh hot as soon as possible (within 5 minutes per ISO 589 Cl. 8.2.1) to avoid atmospheric moisture re-adsorption."
            )
        elif t.startswith('Capture final stabilized mass on LIMS.'):
            p.text = "4. Capture final stabilized mass on LIMS and AS015TF-01."
            
        # Section 5.1 Free moisture example
        elif t.startswith('m_2 = Mass of sample after air drying.'):
            p.text = (
                "m_2 = Mass of sample after air drying (kg).\n\n"
                "Calculation Example (Assessment Q10):\n"
                "Given m_1 = 35.00 kg (as received) and m_2 = 32.55 kg (air dried):\n"
                "m_ar = [(35.00 - 32.55) / 35.00] × 100 = (2.45 / 35.00) × 100 = 7.00%"
            )
            
        # Section 5.3 Total Moisture formula text
        elif t.startswith('For a two-stage determination, the moisture is calculated as follows:'):
            p.text = (
                "For a two-stage determination, the moisture is calculated as follows:\n"
                "TM = m_ar + [(100 - m_ar) × m_res] / 100\n\n"
                "For a single-stage determination (ISO 589 Method B2):\n"
                "TM = [(m_2 - m_3) / (m_2 - m_1)] × 100\n"
                "Where m_1 = pan tare, m_2 = tare + sample before drying, m_3 = tare + sample after 5 h drying."
            )
            
        # Section 6 Precision Limits
        elif t.startswith('Note: If the difference between Pan A and Pan B exceeds 0.30'):
            p.text = (
                "Repeatability Limit & LIMS Repeat Alert:\n"
                "If the difference between duplicate Pan A and Pan B exceeds 0.30% for 2nd stage moisture (|M_res,A - M_res,B| > 0.30%) "
                "or 0.50% for Total Moisture, LIMS triggers a \"repeat\" alert; the sample test is invalidated and must be repeated.\n\n"
                "Worked Example (Assessment Q11):\n"
                "Duplicate pans Pan A M_res = 4.20% and Pan B M_res = 4.58%.\n"
                "Difference: |4.58% - 4.20%| = 0.38%. Since 0.38% > 0.30%, the pair does not comply with repeatability. "
                "LIMS triggers a \"repeat\" alert requiring a complete re-test."
            )
        elif t.startswith('Note: LIMS calculates the total moisture slightly differently'):
            p.text = (
                "Note on LIMS vs. ISO 589 Formula Alignment (Assessment Q12):\n"
                "LIMS calculates total moisture by averaging the duplicate residual moistures first (M_res,avg) and inserting it "
                "directly into the TM formula: TM = m_ar + [(100 - m_ar) × M_res,avg] / 100.\n"
                "In contrast, the ISO 589 standard calculates total moisture for Pan A and Pan B individually and averages them at the end.\n"
                "Because the equation is mathematically linear, both methods yield identical numerical results, and both methods are fully accepted at AzureSky."
            )

    # -------------------------------------------------------------
    # 3. Fix OMML Math Equations in P49 and P54/P55
    # -------------------------------------------------------------
    # Let's inspect paragraphs to find the OMML equations and fix numerator tags
    for p in doc.paragraphs:
        xml = p._p.xml
        if 'm_2-m_1' in xml or ('m_1' in xml and 'm_2' in xml and '<m:oMath' in xml):
            # Replace numerator m_2 - m_1 with m_1 - m_2
            # Let's inspect the xml and swap m2 and m1 in numerator
            p_xml = p._p.xml
            # Replace the run text in the numerator
            p_xml = p_xml.replace('<m:t>2</m:t>', 'TEMP_SWAP_2')
            p_xml = p_xml.replace('<m:t>1</m:t>', '<m:t>2</m:t>')
            p_xml = p_xml.replace('TEMP_SWAP_2', '<m:t>1</m:t>')
            new_p = parse_xml(p_xml)
            p._p.getparent().replace(p._p, new_p)
            print("Fixed Free Moisture OMML equation!")
            break
            
    for p in doc.paragraphs:
        xml = p._p.xml
        if 'm_4-m_3' in xml or ('m_4' in xml and 'm_3' in xml and '<m:oMath' in xml):
            # Replace numerator m_4 - m_3 with m_3 - m_4
            p_xml = p._p.xml
            p_xml = p_xml.replace('<m:t>4</m:t>', 'TEMP_SWAP_4')
            p_xml = p_xml.replace('<m:t>3</m:t>', '<m:t>4</m:t>')
            p_xml = p_xml.replace('TEMP_SWAP_4', '<m:t>3</m:t>')
            new_p = parse_xml(p_xml)
            p._p.getparent().replace(p._p, new_p)
            print("Fixed Residual Moisture OMML equation!")
            break

    # -------------------------------------------------------------
    # 4. Add Section 7: Equipment Verification and Quality Control
    # -------------------------------------------------------------
    # Insert Section 7 before the Revision Table
    # Table 1 is Revision Table
    rev_table = doc.tables[1]
    
    # We can add Section 7 right before the revision table
    # Find the paragraph or position before rev_table
    p_before_table = None
    for p in doc.paragraphs:
        if p._p.getnext() == rev_table._tbl or (rev_table._tbl in list(p._p.itersiblings())):
            pass
            
    # Add Section 7 text to a paragraph before the table
    # In doc.paragraphs, let's find the last paragraph before Revision Table
    for i, p in enumerate(doc.paragraphs):
        if 'Revision Table' in p.text:
            p.text = '' # Clear if it was duplicate text
            
    # Let's find paragraph 68 or the paragraph right after Table 0 (Precision Table)
    p_prec_note = None
    for p in doc.paragraphs:
        if 'Note on LIMS vs. ISO 589' in p.text:
            p_prec_note = p
            break
            
    if p_prec_note:
        # Add heading and paragraphs after p_prec_note
        p_h7 = p_prec_note.insert_paragraph_before()
        # Instead, let's append to the document before table 1
        # In python-docx, insert_paragraph_before on table 1's previous element
        rev_tbl_elem = rev_table._tbl
        
        # Create elements for Section 7
        sect7_xml = """
        <w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
          <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
          <w:r><w:t>7. Equipment Verification and Quality Control</w:t></w:r>
        </w:p>
        """
        sect7_body_xml = """
        <w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
          <w:r><w:t>To ensure metrological traceability under ISO/IEC 17025 Clause 6.4:&#10;• Moisture Drying Oven (AS023TF): Calibrated thermocouple reading (Average + Correction Factor) checked daily against tolerance 105 °C to 110 °C (nominal indicator set point ≤ 107 °C).&#10;• Crusher Efficiency Checks (AS001IW Cl. 4.1):&#10;  - 25 mm &amp; 10 mm crushers: Verified every Monday at the start of shift before work commences.&#10;  - 3 mm &amp; 4.75 mm crushers: Verified on the day of use before use.</w:t></w:r>
        </w:p>
        """
        p7_elem = parse_xml(sect7_xml)
        p7_body_elem = parse_xml(sect7_body_xml)
        rev_tbl_elem.addprevious(p7_elem)
        rev_tbl_elem.addprevious(p7_body_elem)
        print("Inserted Section 7 before Revision Table!")

    # -------------------------------------------------------------
    # 5. Update Revision Table (Table 1)
    # -------------------------------------------------------------
    row_rev1 = rev_table.rows[2]
    row_rev1.cells[0].text = "01"
    row_rev1.cells[1].text = "10/2026"
    row_rev1.cells[2].text = (
        "Full technical alignment with ISO 589:2008, ISO 13909-4:2025, and AZCA-015 assessment: "
        "corrected formula signs (m1 - m2 and m3 - m4), added method selection criteria, coal oxidation rationale (≤ 40 °C), "
        "50 mm incoming top-size limit, 5-step crushing sequence, single-stage hot weighing protocol, "
        "equipment verification controls (AS023TF / AS001IW), and repeatability alert threshold."
    )
    print("Updated Revision Table row 1!")

    # Save to _ Draft.docx and also AS015IW DETERMINATION OF TOTAL MOISTURE Rev 01.docx
    doc.save('_ Draft.docx')
    doc.save('AS015IW DETERMINATION OF TOTAL MOISTURE Rev 01.docx')
    print("Saved modified _ Draft.docx and AS015IW DETERMINATION OF TOTAL MOISTURE Rev 01.docx successfully!")

if __name__ == '__main__':
    run_update()
