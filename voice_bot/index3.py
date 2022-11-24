# Find the Sinch phone number assigned to your app
# and your application key and secret 
# at dashboard.sinch.com/voice/apps
import requests

key = "44fb22eb-d506-462c-bdea-77e05403b914"
secret = "lebFGvbmi0u9KtwmLW2IUA=="
fromNumber = "+447520651336"
to = "+919830728404"
locale = "en-US"
url = "https://calling.api.sinch.com/calling/v1/callouts"

payload = {
  "method": "CustomCallout",
        "customCallout": {
            "ice": "{\"action\": {\"destination\": {\"type\": \"number\",\"endpoint\": \"+916296821825\"  },\"cli\": \"+447520651336\",\"name\": \"ConnectPstn\"}}",
            "ace": "{\"action\":{\"name\": \"runMenu\",\"locale\":\"en-IN\",\"menus\": [{\"id\": \"main\",\"mainPrompt\": \"#tts[Hi there my name is Hrithik Paul, I am from Jis University if wanna know more about me press 2]\",\"options\": [{\"dtmf\": \"1\",\"action\": \"return(support)\"},{\"dtmf\": \"2\",\"action\": \"menu(sub)\"}]},{\"id\": \"sub\",\"mainPrompt\": \"#tts[JIS University is a private university located near Agarpara, West Bengal, India It was established in 2014 under JIS University Act, 2014. JIS University is a multi-disciplinary, unitary & non-affiliating university, offering courses in engineering, technology, sciences, humanities, law, pharmacy and management studies so press 3 for the adresses ]\",\"options\": [{\"dtmf\": \"3\",\"action\": \"menu(address)\"}]},{\"id\": \"address\",\"mainPrompt\": \"#tts[81,Nilgunj Road,Agarpara, Kolkata-700109.,thank you for calling if you wanna repeat everything press 4 or press 5]\",\"options\": [{\"dtmf\": \"4\",\"action\": \"menu(main)\"}]}]}}",
            "pie" : url,
            "dice" : url
        }
}

headers = { "Content-Type": "application/json" }

response = requests.post(url, json=payload, headers=headers, auth=(key, secret))

data = response.json()
print(data)