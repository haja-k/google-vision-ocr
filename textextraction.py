import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('../ocr/img/Haja-Back.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

response = client.text_detection(image=image)    
texts = response.text_annotations   

print(response)

print('Texts:')    
for text in texts:        
    print('\n"{}"'.format(text.description))        
    vertices = (['({},{})'.format(vertex.x, vertex.y)                    
                for vertex in text.bounding_poly.vertices])        
    print('bounds: {}'.format(','.join(vertices))) 

print('Labels:')
for label in labels:
    print(label.description)