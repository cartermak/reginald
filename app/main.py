import requests
from flask import Flask, request, Response

# Hardcoding is bad. shhhh
url = "https://api.groupme.com/v3/bots/post"
bot_id = "12ed70cfae0931c89ff0fe0adb"
trigger = "reginald"

# Instantiate web server
app = Flask(__name__)

# Define callback endpoint
@app.route('/messages',methods = ['POST'])
def messageListener():
    
    print("Message received")

    # Extract JSON content from request
    content = request.json
    
    # Check that dict has "text" attribute before accessing
    if "text" in content.keys():

        # Extract "text" field
        msg = content["text"]

        # Send message if incoming message contains trigger string
        if trigger in msg.lower():
            sendMessage(url,bot_id)
    
    # Return HTTP code
    return Response(status=200)

def sendMessage(url,bot_id):
    content = {
        "bot_id": bot_id,
        "text": "oh hello there"
    }

    requests.post(url, data=content)
    print("Message sent")
