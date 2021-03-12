import osfrom twilio.rest import Client

def report():
    account_sid = os.environ['twilio_sid']
    auth_token = os.environ['twilio_auth']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "Hello World. Chika Chika!",
        from = "+14243810732",
        to = "+918084272322"
    )

print(message.sid)