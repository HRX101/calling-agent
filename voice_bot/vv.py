import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid="ACee3fa2e7fbf7e479f135eaea8e3b8ee9"
auth_token="fc1ad745db3f93d9a4154711f868ae91"
client = Client(account_sid, auth_token)
validation_request = client.validation_requests \
                           .create(
                                friendly_name='My Home Phone Number',
                                phone_number='+918016253206'
                            )