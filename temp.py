import os,io 
import pandas as pd
from google.cloud import vision 
from google.cloud import vision_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'diesel-skyline-370014-86ff31eb0ca5.json'



client = vision.ImageAnnotatorClient()
path=r'/home/vishnu/Documents/Handwritten-text-to-digitalized-versions-Dev-track/sample datasets'
img='line.png'
final_path=os.path.join(path,img)
with io.open(final_path,'rb')as image_file:
    text_file=image_file.read()
    image_detail = vision.Image(content=text_file)
    response = client.document_text_detection(image=image_detail)
    doctext = response.full_text_annotation.text
    print(doctext)
