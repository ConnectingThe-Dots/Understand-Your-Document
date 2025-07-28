from fpdf import FPDF

def create_test_pdf(path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Title", ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test document", ln=1, align="L")
    pdf.output(path)
