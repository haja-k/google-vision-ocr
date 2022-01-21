# VISION
- An API by Google
- Used for Optical Character Recognition (OCR)

## Getting Started
- install package to get started with `pip install --upgrade google-cloud-vision`
- install other pip requirements
- create acc on google vision website under free trial (91 days)
    - create new project
    - authenticate project [email/url]
    - enable api
- go to project dashboard and then create a `service account key`
- key will be autodownloaded, i use json format
- drag key.json into project folder
- point system to the key that was created from google website by adding `os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../ocr/igneous-stone-338706-bcdcebad51fa.json”` into code
- import package to code `from google.cloud import vision`
- use `client = vision.ImageAnnotatorClient()` to connect to client
- end
## References
https://cloud.google.com/vision/docs/ocr
