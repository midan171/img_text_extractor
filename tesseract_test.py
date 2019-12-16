import os
from PIL import Image
import pytesseract


dir_path = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(dir_path,"images")

img_source = os.path.join(dataset_path,"lebron_james.jpg")

im = Image.open(img_source)
text = pytesseract.image_to_string(im, lang="eng")
print(text)