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

 # Add elements in doc and make add space between them
    elements = [title_element, date_element, Spacer(1, 12)] + paragraph_elements
    doc.build(elements)
# add spaces between paragraphs    
    for element in paragraph_elements:
        elements.append(Spacer(1, 12))
