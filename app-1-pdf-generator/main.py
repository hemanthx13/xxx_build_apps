from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

print(type(pdf))

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)

pdf.cell(w=40, h=12, txt="Hello There! KOKO", align="L", ln=1, border=1)
pdf.cell(w=0, h=20, txt="Hi There! ZUZU", align="L", ln=1, border=1)


pdf.set_font(family="Arial", style="I", size=15)

pdf.cell(w=50, h=12, txt="Hello There! PAPA", align="L", ln=1, border=1)
pdf.cell(w=60, h=20, txt="Hi There! Hemu", align="L", ln=1, border=1)

pdf.add_page() # Adds new page in this case 2nd page

pdf.set_font(family="Helvetica", style="U", size=12)

pdf.cell(w=50, h=12, txt="Hello There! Gopal", align="L", ln=1, border=1)


pdf.output("output.pdf")