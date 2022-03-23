import json
import sys
from json import JSONDecodeError
from furhat_remote_api import FurhatRemoteAPI
import requests

def main():

    # furhat = FurhatRemoteAPI("192.168.8.175")
    # furhat = FurhatRemoteAPI("192.168.8.141")
    furhat = FurhatRemoteAPI("localhost")
    # this variable has to be changed every time you run ngrok
    ngrok = "7098-146-198-152-239"
    url_receive = "http://" + ngrok + ".ngrok.io/webhooks/furhat_robot/webhook"
    url_health = "http://" + ngrok + ".ngrok.io"

    voices = furhat.get_voices()
    furhat.set_voice(name='Matthew')
    furhat.say(text="My name is Furhat, and I'm a social robot. Hi there!", blocking=True)

    furhat_response = ""
    while furhat_response != "Bye":
        furhat_response = dialogue(furhat, url_receive)

    users = furhat.get_users()
    furhat.attend(user="CLOSEST")
    furhat.attend(userid="virtual-user-1")
    # furhat.attend(location="0.0,0.2,1.0")
    # furhat.set_led(red=200, green=50, blue=50)

def dialogue(furhat, url_receive):
    answer = furhat.listen()
    if answer.message == "":
        furhat.say(text="I don't think you said anything. Could you please repeat?", blocking=True)
        answer = furhat.listen()
        if answer.message == "":
            furhat.say(text="I still can't hear you, I'm sorry. Maybe we could talk another day!", blocking=True)
            sys.exit("User didn't say anything to Furhat.")
    data = {"sender": "furhat", "message": answer.message}
    post = requests.post(url_receive, data=json.dumps(data))
    try:
        response = post.json()[0].get("text")
    except KeyError:
        response = "I don't understand what you said. Could you please repeat?"
    except JSONDecodeError:
        response = "I'm not sure if I understood you - could you please repeat?"

    print(response)
    furhat.say(text=response, blocking=True)
    return response

if __name__ == "__main__":
    main()