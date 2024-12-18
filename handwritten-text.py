# intract with azure cognitive services computer vision api
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# checks the atatus of next operation
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# authenticate the cognitive service api and key
from msrest.authentication import CognitiveServicesCredentials

import time

import cred
# url=endpoint and key are cognitive service


url=cred.url
key=cred.key

img = "https://i.ytimg.com/vi/1YFqJPCAEDo/maxresdefault.jpg"

# computervisionclient object name con and it uses endpoint url and key for authentication
con = ComputerVisionClient(url,CognitiveServicesCredentials(key))

#con allows to analyze img(line 12)for text content
# raw to give a raw response
res = con.read(img,raw=True)

# extracts location from api rersponse and header contain the url
loc = res.headers["Operation-Location"]

# operatiion id from location url
id = loc.split("/")[-1]

# loop for the status of text recognition
while True:
    # con.get_read_result(id) send request to id url to get current status of text recognition
    hand_text = con.get_read_result(id)
    # to check if its running or not started if any other statuts the loop breaks
    if hand_text.status not in ['notStarted','running']:
        break
    # to avoid overwhelming api request
    time.sleep(1)


# to check if it is completely successfully and iterates throight the extracted data
if hand_text.status == OperationStatusCodes.succeeded:
    # to iterate over recognized text
    for text in hand_text.analyze_result.read_results:
        for line in text.lines:
            # to print the text of each detected line   
            print(line.text)