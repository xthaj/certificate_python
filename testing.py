from PIL import Image, ImageDraw, ImageFont
import os

# Load the PNG certificate template
template_image = Image.open("cert.jpg")

# Define two sample names
long_name = "Alexander Jonathan Williams Powell The Second"
short_name = "Emma Smith"

# Define the text color
text_color = (0, 0, 0)  # Black

# Create a folder to store the certificates if it doesn't exist
os.makedirs("testing", exist_ok=True)

middle_line = template_image.height // 2

# Define the Y-axis position for the name text
# CHANGE THIS ACCORDING TO YOUR NEEDS!!
y_position = 800
chosen_x_margin = 300
font_size = 120
# like this
# y_position = 520 


# Define the margins and middle line positions
margin_50 = 50
margin_100 = 100
margin_200 = 220

# Define the font for the guiding lines' labels
label_font = ImageFont.truetype("arial.ttf", size=20)

# Generate certificates for the long and short names
for name in [long_name, short_name]:
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

    # Draw red guiding lines and their labels
    # Vertical lines
    for margin in [margin_50, margin_100, margin_200]:
        draw.line([(margin, 0), (margin, certificate_image.height)], fill=(255, 0, 0), width=2)
        draw.line([(certificate_image.width - margin, 0), (certificate_image.width - margin, certificate_image.height)], fill=(255, 0, 0), width=2)
        draw.text((margin - 20, 10), str(margin), fill=(255, 0, 0), font=label_font)
        draw.text((certificate_image.width - margin + 10, 10), str(margin), fill=(255, 0, 0), font=label_font)

    # Horizontal lines
    for margin in [margin_50, margin_100]:
        draw.line([(0, middle_line - margin), (certificate_image.width, middle_line - margin)], fill=(255, 0, 0), width=2)
        draw.line([(0, middle_line + margin), (certificate_image.width, middle_line + margin)], fill=(255, 0, 0), width=2)
        draw.text((10, middle_line - margin - 20), str(middle_line - margin - 20), fill=(255, 0, 0), font=label_font)
        draw.text((10, middle_line + margin + 10), str(middle_line + margin + 10), fill=(255, 0, 0), font=label_font)

    # Middle line
    draw.line([(0, middle_line), (certificate_image.width, middle_line)], fill=(255, 0, 0), width=2)
    draw.text((10, middle_line - 20), str(middle_line - 20) + " (middle)", fill=(255, 0, 0), font=label_font)

    # Save the certificate image
    certificate_image.save(os.path.join("testing", f"{name[:20]}.png"))

    # Close the certificate image
    certificate_image.close()
