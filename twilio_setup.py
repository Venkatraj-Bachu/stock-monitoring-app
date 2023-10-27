from twilio.rest import Client


class Twilio:
    """
    This class is used to send text messages to given phone number.\n
    Required parameters to call the class:\n
    account_sid: (type) str - TWILIO_ACCOUNT_SID.
    auth_token: (type) str - TWILIO_AUTH_TOKEN
    """

    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)
        pass

    def send_message(self, from_phone: str, to_phone: str, message: str = '') -> str:
        """
        Sends text message to the given phone number\n
        :param from_phone: (type) str - TWILIO PHONE NUMBER
        :param to_phone: (type) str - Phone you want to send the message to
        :param message: (type) str - The message you want to send.
            default value: ''
        :return: Message status
        """
        message = self.client.messages.create(
            body=f"{message}",
            from_=from_phone,
            to=to_phone,
        )

        return message.sid
