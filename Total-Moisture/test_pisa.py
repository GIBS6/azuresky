import sys
from xhtml2pdf import pisa

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
    @page {
        size: a4 portrait;
        margin: 2cm;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
        }
    }
    body { font-family: Helvetica, Arial, sans-serif; font-size: 11pt; color: #333; }
    h1 { color: #003366; }
</style>
</head>
<body>
    <h1>AzureSky Coal Laboratory</h1>
    <p>Testing xhtml2pdf generation...</p>
</body>
</html>
"""

with open("test_output.pdf", "wb") as f:
    pisa_status = pisa.CreatePDF(html_content, dest=f)

print(f"PDF generation status: error={pisa_status.err}")
