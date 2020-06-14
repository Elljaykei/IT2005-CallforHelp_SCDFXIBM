import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('xnaDEOYBnLuGTlj-9p6KCxFY1zjJFVaaem-NbTzQfvEV')
visual_recognition = VisualRecognitionV3(
    version='2020-06-13',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/5382a26a-8ae1-4d2d-88f5-4e46020ad3f0')

with open('./nonfire1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    print(json.dumps(classes, indent=2))
