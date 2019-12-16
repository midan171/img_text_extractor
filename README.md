# img_text_extractor
A python application that uses computer vision to extract text from images.
It uses the pretrained deep Network presented in a paper with the title "EAST: An Efficient and Accurate Scene Text Detector", publiced in 2017, to execute a text localization in the image. After that it is processing each of the image areas pointed out by the "EAST" text detector (areas with high probability of containing text). It uses Open CV functions for image preprocessing in each of these areas, so that the character recognision system that is applied afterwards, can recognize each character with better success rate.
As a character recognision system (OCR), we are using "tesseract", one of the most popular tools in this category. 

-First download the text detection model "frozen_east_text_detection.pb"
	from https://github.com/ApexPredator1/EAST-text-detection-OpenCV/blob/master/frozen_east_text_detection.pb
	or https://github.com/oyyd/frozen_east_text_detection.pb/blob/master/frozen_east_text_detection.pb
	(This file is a trained 
-Place it inside the directory of the other .py files

-Run ocr.py

-ocr.py calls text_localization.py from text_detection.py file
  which calls frozen_east_text_detection.pb, the pretrained 
	neural net based text area detection model

-Then ocr.py calls a function for pre-processing from the functions in functions.py

Thank you :)

