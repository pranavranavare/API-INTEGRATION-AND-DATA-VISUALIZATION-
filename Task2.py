import csv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# File paths
csv_file = "sample_data.csv.txt"
pdf_file = "automated_report.pdf"

styles = getSampleStyleSheet()

# Create PDF document
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
elements = []

# Title
elements.append(Paragraph("Automated Report of Sales ", styles["Title"]))
elements.append(Spacer(1, 10))

months = []
product_a = []
product_b = []

# Read CSV file
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        months.append(row["Month"])
        product_a.append(int(row["Product_A_Sales"]))
        product_b.append(int(row["Product_B_Sales"]))

# Analysis
total_a = sum(product_a)
total_b = sum(product_b)
avg_a = round(total_a / len(product_a), 2)
avg_b = round(total_b / len(product_b), 2)

# Summary
elements.append(Paragraph("Summary", styles["Heading2"]))
elements.append(Paragraph(f"Total Product A Sales: {total_a}", styles["BodyText"]))
elements.append(Paragraph(f"Total Product B Sales: {total_b}", styles["BodyText"]))
elements.append(Paragraph(f"Average Product A Sales: {avg_a}", styles["BodyText"]))
elements.append(Paragraph(f"Average Product B Sales: {avg_b}", styles["BodyText"]))
elements.append(Spacer(1, 10))

# Table
table_data = [["Month", "Product A", "Product B"]]

for i in range(len(months)):
    table_data.append([months[i], product_a[i], product_b[i]])

elements.append(Paragraph("Monthly Sales Data", styles["Heading2"]))
elements.append(Table(table_data))
elements.append(Spacer(1, 10))

elements.append(Paragraph("This PDF report was automatically generated using Python and ReportLab.", styles["BodyText"]))

# Build PDF
doc.build(elements)

print("PDF Report Generated Successfully!")
