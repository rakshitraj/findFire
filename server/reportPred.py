import os
from twilio.rest import Client

def report(content : str, recipient : str) -> str:
    # account_sid = os.environ['ACe3b1da447e3240e9f3a86c9c9d0f2bd1']
    # auth_token = os.environ['ee52b014111ef236675482121ce74fe2']
    # client = Client(account_sid, auth_token)
    try:
        client = Client('ACe3b1da447e3240e9f3a86c9c9d0f2bd1', 'ee52b014111ef236675482121ce74fe2')

        message = client.messages.create(
            body = content,
            from_ = "+14243810732",
            to = recipient
        )
        return message.sid
    except:
        return 0

if __name__ == '__main__':
    content = 'Hello.'
    recipient = "+918084272322"
    report(content, recipient)