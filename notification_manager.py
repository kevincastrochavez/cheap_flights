from twilio.rest import Client

TWILIO_SID = 'AC5b27a5c19d21e6edbccaae83a7146d53'
TWILIO_AUTH_TOKEN = '7226f275dea2b22df8f0965cc47aba56'
TWILIO_VIRTUAL_NUMBER = '+19302019526'
TWILIO_VERIFIED_NUMBER = '+13853541824'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
