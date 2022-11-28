import os,io 
import pandas as pd
from google.cloud import vision 
from google.cloud import vision_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:vision api/Google vision API test-8a0999498f6f.json'



client = vision.ImageAnnotatorClient()

with io.open('line.png')as image_file:
    text_file=image_file.read
image_detail = vision.Image(content=text_file)
response = client.document_text_detection(image=image_detail)
doctext = response.full_text_annotation.text
print(doctext)




