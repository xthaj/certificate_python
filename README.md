For auto-making certificates

# How to use

1. Add certificate template (image)

   Change the following line of code in both `testing.py` and `main.py` according to the filename:

   ```python
   template_image = Image.open("cert.jpg")

2. Adjust the margin and y axis on `testing.py`
   Run `testing.py`, check the result on `testing` folder. Adjust the code below accordingly, until everything looks right. Copy paste correct values to `main.py`

   ```python
    # CHANGE THIS ACCORDING TO YOUR NEEDS!!
    y_position = 800
    chosen_x_margin = 300
    font_size = 120

3. Fill `names.xlsx` accordingly
4. Run `main.py`
5. Results should be on `certificates` folder
