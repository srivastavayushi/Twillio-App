from twilio.rest import Client 
import os

account_sid = os.environ('account_sid')
auth_token = os.environ('auth_token')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello World",
                    from='+15053374593',
                    to='+91 6390261421'
                )

print(message.sid)