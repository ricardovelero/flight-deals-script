from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_MSG_SERVICE_SID = os.environ.get("TWILIO_MSG_SERVICE_SID")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")


class NotificationManager:

    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms_msg(self, message):
        message = self.client.messages.create(
            body=message,
            messaging_service_sid=TWILIO_MSG_SERVICE_SID,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
