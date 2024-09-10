from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import reportlab.rl_config
import copy

reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import csv

# Initialize variables and canvas
packet = io.BytesIO()
pdfmetrics.registerFont(TTFont('LEMONMILK', 'LEMONMILK-Light.ttf'))

names = []
x = 107
y = 655
max_names_per_page = 8

# Read names from file
with open('names.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        names.append(row[0])

# Calculate number of pages
pages = math.ceil(len(names) / max_names_per_page)

# Load existing PDF (template PDF)
existing_pdf = PdfFileReader(open("original.pdf", "rb"))
output = PdfFileWriter()

for page_num in range(pages):
    print(f"Processing page {page_num + 1}")

    # Reset the x and y for each new page
    x = 107
    y = 655

    packet = io.BytesIO()  # Create a new canvas for each page
    can = canvas.Canvas(packet, pagesize=letter)

    # Loop over the names for the current page
    for i in range(max_names_per_page):
        name_index = page_num * max_names_per_page + i
        if name_index >= len(names):
            break  # Stop if we've placed all names

        can.setFont('LEMONMILK', 35 - len(names[name_index]))

        # Draw the name, alternating positions
        if (i % 2 == 1):
            can.drawString(x, y, names[name_index])
            x = 107
            y -= 155
        else:
            can.drawString(x, y, names[name_index])
            x += 241

    # Save the canvas and add it to the new page
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # Create a fresh copy of the template page to avoid modifying the original
    template_page = copy.copy(existing_pdf.getPage(0))

    # Merge new content with the fresh copy of the template page
    template_page.mergePage(new_pdf.getPage(0))
    output.addPage(template_page)

# Save the final output PDF
outputStream = open(f"namesToPrint_{pages}.pdf", "wb")
output.write(outputStream)
outputStream.close()
