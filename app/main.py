import requests
from flask import Flask, request

# Hardcoding is bad
url = "https://api.groupme.com/v3/bots/post"
bot_id = "12ed70cfae0931c89ff0fe0adb"
trigger = "reginald"

# Instantiate web server
app = Flask(__name__)

# Define callback endpoint
@app.route('/messages',methods = ['POST'])
def messageListener():

    # Extract JSON content from request
    content = request.json
    
    # Check that dict has "text" attribute before accessing
    if hasattr(content,"text"):

        # Extract "text" field
        msg = content["text"]

        # Send message if incoming message contains trigger string
        if trigger in msg.lower():
            sendMessage()


def sendMessage(url,bot_id):
    content = {
        "bot_id": bot_id,
        "text": "oh hello there"
    }

    requests.post(url, data=content)
