import os
import requests
from flask import Flask, request, Response

groupme = dict()

# Load environment variables or use default values
if os.getenv("GROUPME_URL") is None:
    groupme["url"] = "https://api.groupme.com/v3/bots/post"
else:
    groupme["url"] = os.getenv("GROUPME_URL")

if os.getenv("BOT_ID") is None:
    groupme["bot_id"] = "12ed70cfae0931c89ff0fe0adb"
else:
    groupme["bot_id"] = os.getenv("BOT_ID")

# API endpoint for getting compliemnts
text_api_url = "https://complimentr.com/api"

# Text to match
trigger = "hi reginald"

# Instantiate web server
app = Flask(__name__)

# Callback endpoint receives POST request from GroupMe
@app.route('/messages', methods=['POST'])
def messageListener():

    # Extract JSON content from request
    content = request.json

    # Check that dict has "text" attribute before accessing
    if "text" in content.keys():

        # Extract "text" field
        msg = content["text"]
        print("Message received: " + msg)

        # Send message if incoming message contains trigger string
        if trigger in msg.lower():

            # Send a compliment
            compliment = getCompliment(text_api_url)
            sendMessage(compliment, groupme["url"], groupme["bot_id"])

    # Return HTTP code
    return Response(status=200)


def sendMessage(message, url, bot_id):
    content = {
        "bot_id": bot_id,
        "text": message
    }

    requests.post(url, data=content)
    print("Message sent: " + message)


def getCompliment(url):
    res = requests.get(url)
    res = res.json()
    if "compliment" in res.keys():
        message = res["compliment"]
    else:
        message = "oh no, call carter, I'm broken"

    return message