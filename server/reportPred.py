import os
from twilio.rest import Client
import sys

def report(content : str, recipient : str) -> str:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body = content,
            from_ = "+14243810732",
            to = recipient
        )
        return message.sid
    except:
        print("Error occured while sending report. Not sent.\n", sys.exc_info()[0])
        return 0

if __name__ == '__main__':
    content = 'How u doin?.'
    recipient = sys.argv[1]
    report(content, recipient)