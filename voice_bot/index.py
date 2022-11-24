from twilio.rest import Client
import time
import pandas as pd
data=pd.read_excel("ph_number.xlsx")
columns=data.columns
col=columns[1]
print(col)
ph_numbers=[]
for j in data[col]:
    no="+91"+str(j)
    ph_numbers.append(no)
print(ph_numbers)


#account_sid="AC57ae63879ae3b8df3765988059702ef6"
#ACee3fa2e7fbf7e479f135eaea8e3b8ee9
#auth_token="a8960a38dccbd0b8be5e961d6aa5fa64"
#url='https://handler.twilio.com/twiml/EH02bc611f248b7a881266e5e91dbb1664?name=sayani'
account_sid="ACee3fa2e7fbf7e479f135eaea8e3b8ee9"
auth_token="fc1ad745db3f93d9a4154711f868ae91"
name="sayani"
client=Client(account_sid,auth_token)
class call_do:
    def __init__(self):
        self.account_sid=account_sid
        self.auth_token=auth_token
        self.name=name
    def ended_execution(self):
        execution = client.studio \
                  .v2 \
                  .flows('FWa732f9b7535ab5291789c3b4fc17ae0f') \
                  .executions('FN52580b67ab991ed31a5a3c1996024db3') \
                  .update(status='ended')

        
    def make_call(self,number):
        
        client=Client(self.account_sid,self.auth_token)
        self.execution = client.studio \
                    .v2 \
                    .flows('FWa732f9b7535ab5291789c3b4fc17ae0f') \
                    .executions \
                    .create(to="+91 80162 53206", from_='+1 314 948 5412f')
        
        return self.execution

#i=int(input("enter value  "))

#transcription = client.transcriptions('TRf696b81c9144605a1a82a82272a3d380') \.fetch()

#print(transcription.date_created)
call_send=call_do()
call_id=[]
"""
for i in ph_numbers:
    id=call_send.make_call(i)
    call_id.append(id)
    time.sleep(4)
call_send.ended_execution()
"""
id=call_send.make_call("+91 80162 53206")
print(id)
print("done")