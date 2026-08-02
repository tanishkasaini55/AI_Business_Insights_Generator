from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf_report(kpis, insights):

    filename = "Business_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph("<b>AI BUSINESS INSIGHTS REPORT</b>", styles["Title"])
    )

    # Date
    elements.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y %I:%M %p')}",
            styles["Normal"]
        )
    )

    elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    # KPI Heading
    elements.append(
        Paragraph("<b>Dashboard Summary</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(f"Total Revenue : ${kpis['Total Revenue']:,.2f}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"Total Cost : ${kpis['Total Cost']:,.2f}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"Units Sold : {kpis['Units Sold']:,}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"Countries : {kpis['Countries']}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"Categories : {kpis['Categories']}", styles["Normal"])
    )

    elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    # AI Section
    elements.append(
        Paragraph("<b>AI Business Insights</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(insights.replace("\n", "<br/>"), styles["Normal"])
    )

    doc.build(elements)

    return filename

