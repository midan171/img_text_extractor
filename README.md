# img_text_extractor
A python application that uses computer vision to extract text from images.

-Run ocr.py

-ocr.py calls text_localization.py from text_detection.py file
  which calls frozen_east_text_detection.pb, the pretrained 
	neural net based text area detection model

-then ocr.py calls a function for pre-processing from the functions in functions.py

