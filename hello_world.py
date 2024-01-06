from PIL import Image, ImageDraw, ImageFont
import openpyxl
import os

# Load the PNG certificate template
template_image = Image.open("certificate_template.png")

# Open the Excel file and select the sheet with names
excel_file = openpyxl.load_workbook("names.xlsx")
sheet = excel_file.active

# Get the column containing names (assuming it's in column A)
name_column = sheet["A"]

# Define the text color
text_color = (0, 0, 0)  # Black

# Create a folder to store the certificates if it doesn't exist
os.makedirs("certificates", exist_ok=True)

# Define the Y-axis position for the name text (you can adjust this)
y_position = 520

# Iterate through the names in the Excel file
for cell in name_column:
    name = cell.value

    # Create a folder with the name if it doesn't exist
    folder_path = os.path.join("certificates", name)
    os.makedirs(folder_path, exist_ok=True)

    # Create a certificate image with the name
    certificate_image = template_image.copy()
    draw = ImageDraw.Draw(certificate_image)

    # Calculate the X-axis position to center the text using draw.textlength
    font_size = 60  # Set the initial font size
    font = ImageFont.truetype("arial.ttf", font_size)
    
    while True:
        text_width = draw.textlength(name, font=font)
        if text_width <= certificate_image.width:
            break
        font_size -= 1
        font = ImageFont.truetype("arial.ttf", font_size)

    x_position = (certificate_image.width - text_width) / 2

    # Add the name text to the image
    draw.text((x_position, y_position), name, fill=text_color, font=font)

    # Save the certificate image in the corresponding folder
    certificate_image.save(os.path.join(folder_path, "certificate.png"))

    # Close the certificate image
    certificate_image.close()

# Close the Excel file
excel_file.close()
