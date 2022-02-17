import logging
from sanic import Blueprint, response
from rasa.core.channels.channel import UserMessage
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel

logger = logging.getLogger(__name__)

class PepperConnector(InputChannel):
    # the webhook is:
    # http://localhost:5005/webhooks/pepper_robot/webhook
    # localhost must be replaced with a ngrok address
    @classmethod
    def name(cls):
        return "pepper_robot"

    def blueprint(self, on_new_message):
        pepper_webhook = Blueprint("pepper_webhook", __name__)

        @pepper_webhook.route("/", methods=["GET"])
        async def health(re,quest):
            return response.json({"status": "ok"})

        @pepper_webhook.route("/webhook", methods=["POST"])
        async def receive(request):
            payload = request.json
            sender = payload.get("sender")
            message = payload.get("message")
            print("User: " + message)

            collector = CollectingOutputChannel()
            await on_new_message(UserMessage(message, collector))
            responses = [m["text"] for m in collector.messages]

            if responses:
                print("Pepper: " + responses[0])
                return response.json(collector.messages)
            else:
                print("Pepper: I don\'t understand what you said. Could you please repeat?")
                message = {'recipient_id': 'default', 'text:': 'I don\'t understand what you said. Could you please '
                                                               'repeat?'}
                return response.json(message)

        return pepper_webhook
