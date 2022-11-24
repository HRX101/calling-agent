import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid="ACee3fa2e7fbf7e479f135eaea8e3b8ee9"
auth_token="fc1ad745db3f93d9a4154711f868ae91"
client = Client(account_sid, auth_token)

execution = client.studio \
                  .v2 \
                  .flows('FWa732f9b7535ab5291789c3b4fc17ae0f') \
                  .executions('FN52580b67ab991ed31a5a3c1996024db3') \
                  .update(status='ended')

print(execution.sid)