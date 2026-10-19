import sys
import docx
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

def update_document(input_path, output_path):
    doc = docx.Document(input_path)
    
    # 1. Update Footer (Revision 01, Date 10/2026, Next rev 10/2029)
    for section in doc.sections:
        footer = section.footer
        for table in footer.tables:
            for row in table.rows:
                for cell in row.cells:
                    if '00' in cell.text and 'Revision no' not in cell.text:
                        cell.text = cell.text.replace('00', '01')
                    if '10/2025' in cell.text:
                        cell.text = cell.text.replace('10/2025', '10/2026')
                    if '10/2028' in cell.text:
                        cell.text = cell.text.replace('10/2028', '10/2029')
                        
    # 2. Update Table of Contents if needed, or paragraphs
    print(f"Loaded {len(doc.paragraphs)} paragraphs.")
    
if __name__ == '__main__':
    update_document('_ Draft.docx', '_ Draft_test.docx')
    print("Test finished successfully.")
