from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_receipt(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Add a company logo (Replace 'logo.png' with the path to your image file)
    c.drawImage("logo.png", 180, 700, width=250, height=70)  # Adjust size and position for the logo
    
   
    c.setFont("Helvetica", 15)
    c.drawCentredString(305, 690, "Address: Kolkata-700001")
    c.drawCentredString(305, 670, "Phone Number : 91-040-40180***")
    c.drawCentredString(300, 650, "CIN: L24240KL1234PLC009876")
    c.drawCentredString(305, 630, "GSTIN: 36AACL1589J12H")
    # Draw a line below the header
    c.line(50, 622, 550, 622)
    
    # Add title "CASH RECEIPT"
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(300, 600, "TAX INVOICE")
    
      # Add dotted line below headers
    c.setDash(1, 2)  # Dotted line effect
    c.line(70, 595, 530, 595)
    # Draw the table headers
    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, 580, "Item Code")
    c.drawString(200, 580, "Qty.")
    c.drawString(420, 580, "Price")
     # Add dotted line below headers
    c.setDash(1, 2)  # Dotted line effect
    c.line(70, 570, 530, 570)
    # Sample product data
    products = [
        {"description": "AS2346F54  ","Qty.": 1, "price": 7.1},
        {"description": "BF1578G2", "Qty.": 1,"price": 2.2},
        {"description": "BH3586T8","Qty.": 1, "price": 3.4},
        {"description": "YT5678I8", "Qty.": 1,"price": 4.3},
        {"description": "IL0452V6","Qty.": 1, "price": 5.5},
    ]
    
    y = 550  # Starting y-coordinate for the product list
    
    # Reset dash style to solid line
    c.setDash(1, 0)
    
    # Add product list
    c.setFont("Helvetica", 12)
    for product in products:
        c.drawString(80, y, product['description'])
        c.drawString(205, y, f"{product['Qty.']}")
        c.drawString(420, y, f"{product['price']:.1f}")
        y -= 20

    # Add dotted line below headers
    c.setDash(1, 2)  # Dotted line effect
    c.line(70, 450, 530, 450)

    # Add total section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, y - 20, "Sub Total")
    c.drawString(205, y - 20, "5")
    c.drawString(420, y - 20, "16.5")
    
    # Add payment details
    c.setFont("Helvetica", 12)
    c.drawString(80, y - 40, "Cash")
    c.drawString(420, y - 40, "20.0")
    
    c.drawString(80, y - 60, "Change")
    c.drawString(420, y - 60, "3.5")
     # Add dotted line below headers
    c.setDash(1, 2)  # Dotted line effect
    c.line(70, 375, 530, 375)
    # Add footer details
    c.drawString(80, y - 100, "Bank card")
    c.drawString(420, y - 100, "...234")
    
    c.drawString(80, y - 120, "Approval Code")
    c.drawString(420, y - 120, "#123456")
    
    # Add a thank you message
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(300, y - 175, "THANK YOU!")
    
    # Add barcode placeholder (optional)
    c.drawImage("barcode.png", 180, 180, width=250, height=70) 
    
    # Save PDF
    c.save()

# Call function to create receipt
create_receipt("receipt.pdf")
