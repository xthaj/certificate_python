from PIL import Image, ImageDraw, ImageFont
import openpyxl
import os

# Load the PNG certificate template
template_image = Image.open("cert.jpg")

# Open the Excel file and select the sheet with names
excel_file = openpyxl.load_workbook("names.xlsx")
sheet = excel_file.active

# Get the column containing names (assuming it's in column A)
name_column = sheet["A"]

# Define the text color
text_color = (0, 0, 0)  # Black

# Create a folder to store the certificates if it doesn't exist
os.makedirs("certificates", exist_ok=True)

middle_line = template_image.height // 2

# Define the Y-axis position for the name text
# CHANGE THIS ACCORDING TO YOUR NEEDS!!
y_position = 800
chosen_x_margin = 300
# usually not needed to change this
font_size = 120
# like this
# y_position = 520 

# Define the font for the guiding lines' labels
label_font = ImageFont.truetype("arial.ttf", size=20)

# Generate certificates for the long and short names
for cell in name_column:
    name = cell.value

    # Create the certificate image with the name
    certificate_image = template_image.copy()
    draw = ImageDraw.Draw(certificate_image)

    # Calculate the X-axis position to center the text using draw.textlength
    font = ImageFont.truetype("arial.ttf", font_size)

    while True:
        text_width = draw.textlength(name, font=font)
        if text_width <= certificate_image.width - 2 * chosen_x_margin:
            break
        font_size -= 1  # Decrease font size
        y_position += 1 
        font = ImageFont.truetype("arial.ttf", font_size)

    x_position = (certificate_image.width - text_width) / 2

    # Add the name text to the image
    draw.text((x_position, y_position), name, fill=text_color, font=font)

    # Save the certificate image
    certificate_image.save(os.path.join("certificates", f"{name[:20]}.png"))

    # Close the certificate image
    certificate_image.close()

# Close the Excel file
excel_file.close()