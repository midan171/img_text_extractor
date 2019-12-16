import os
from PIL import Image
import pytesseract
from text_detection import text_localization
import functions as f

dir_path = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(dir_path,"images")

img_source = os.path.join(dataset_path,"lebron_james.jpg")






#for Every img the ocr process is as follows


#img candidate text areas detection (localization)
candidate_text_areas = text_localization(img_source)

#process candidate text areas with a thresholding algorithm
#paper algorithm modified k-means
#baseline algorithm cv2 simple threshholding

thresh_text_areas = []


#pre-process/threshlolding
#chose a function from functions to pre-process the img
#   f.to_black_white()
#   f.img_thresh_binary()
#   f.img_thresh_adative()
#   f.img_thresh_adative_gaus()


for i in range(len(candidate_text_areas)):
    im = candidate_text_areas[i]
    thresh_text_areas.append(f.img_thresh_adative_gaus(im))






#candidate_text_areas = thresh_text_areas
#finally ocr to every text area candidate
for i in range(len(candidate_text_areas)):
    im = candidate_text_areas[i]
    text = pytesseract.image_to_string(im, lang="eng")
    print("text area ",i+1,": ",text)



