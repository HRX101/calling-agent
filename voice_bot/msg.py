from twilio.rest import Client 
 
account_sid = 'ACee3fa2e7fbf7e479f135eaea8e3b8ee9' 
auth_token = 'fc1ad745db3f93d9a4154711f868ae91' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG539c2cb881a887083c389da3d3ee4ce3', 
                              body='HI there its Hrithik',      
                              to='+916296821825' 
                          ) 
 
print(message.sid)