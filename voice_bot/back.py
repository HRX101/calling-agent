payload = {
  "method": "ttsCallout",
  "event":"pie",
  "ttsCallout": {
    "cli": fromNumber,
    "destination": {
      "type": "number",
      "endpoint": to
    },
    "locale": "en-US",
    "name":"runMenu",
    "prompts": "#tts[press 1 to hangup and 2 to do some task so go for it why you are waiting honey just go]",
      "options":[{
        "dtmf":1,
        "action":"hangup"
      },
      {
        "dtmf":2,
        "prompts":"#tts[press 2 to do some task]"
      }
      ]
 
    
    }
  
  

}
# Find the Sinch phone number assigned to your app
# and your application key and secret 
# at dashboard.sinch.com/voice/apps
import requests

key = ""
secret = ""
fromNumber = ""
to = ""
locale = ""
url = "https://calling.api.sinch.com/calling/v1/callouts"

payload = {
  "method": "ttsCallout",
  "ttsCallout": {
    "cli": fromNumber,
    "destination": {
      "type": "number",
      "endpoint": to
    },
    "locale": locale,
    "text": "Hello, this is a call from Sinch. Congratulations! You made your first call."
  }
}

headers = { "Content-Type": "application/json" }

response = requests.post(url, json=payload, headers=headers, auth=(key, secret))

data = response.json()
print(data)