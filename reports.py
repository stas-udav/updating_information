from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

def generate_report(paragraph, title, attachment):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(attachment)

    title_element = Paragraph(title, styles['Heading1'])
    date_element = Paragraph('Processed Update on {}'.format(date.today()), styles['Normal'])

    paragraph_elements = []
    for line in paragraph.split('\n'):
        paragraph_elements.append(Paragraph(line, styles['Body']))

    doc.addPage(title_element)
    doc.addPage(date_element)
    for element in paragraph_elements:
        doc.addPage(element)
        doc.addPage(Spacer(1, 20))

    doc.build()
