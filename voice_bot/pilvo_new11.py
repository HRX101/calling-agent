const express = require('express');
const bodyParser = require("body-parser");
const ngrok = require('ngrok');
const axios = require('axios')

const PORT = 8081;

const app = express();
app.use(bodyParser.json());

const APPLICATION_KEY = ''
const APPLICATION_SECRET = ''
const CLI = ''
const TO_NUMBER = ''
const eq = '\"'

app.post('/', async (req, res) => {
  let eventName = req.body.event;
  //console.log(`:: INCOMING HTTP BODY :: ", req.body)
  switch (eventName){
    case 'pie':
      var value = req.body.menuResult.value;
      console.log(`:: INCOMING EVENT ::`, req.body.event)
      //console.log(`:: INCOMING EVENT BODY ::`, req.body)
      console.log(`:: IVR MENU CHOICE :: Destination: `, TO_NUMBER, `selected value: `, value);
    case 'dice':
      console.log(`:: INCOMING EVENT ::`, req.body.event)
      //console.log(`:: INCOMING EVENT BODY ::`, req.body)
      res.sendStatus(200);
      break;
    default:
      //console.log(`:: INCOMING HTTP BODY::`, req.body)
      console.log(`:: ERROR ::  Sorry, there was an error with your request. Please inspect HTTP body above`);
      res.sendStatus(404);
  }
});

function calloutRunMenu(url) {
    axios({
      method: 'post',
      url: 'https://calling.api.sinch.com/calling/v1/callouts',
      data: {
        "method": "CustomCallout",
        "customCallout": {
            "ice": "{\"action\": {\"destination\": {\"type\": \"number\",\"endpoint\": "+eq+TO_NUMBER+eq"  },\"cli\": "+eq+CLI+eq",\"name\": \"ConnectPstn\"}}"
            "ace": "{\"action\": {\"name\": \"RunMenu\",\"locale\": \"en-US\",\"menus\": [{\"id\": \"main\",\"mainPrompt\": \"#tts[ Welcome to the main menu. Press 1 to confirm order or 2 to cancel]\",\"timeoutMills\": 5000,\"options\": [ {\"dtmf\": \"1\",\"action\": \"return(confirm)\"}, {\"dtmf\": \"2\",\"action\": \"return(cancel)\"}]}]}}",
            "pie" : url,
            "dice" : url
        }},
      auth: {
          username: APPLICATION_KEY,
          password: APPLICATION_SECRET
        },   
        headers: {
          'content-type': 'application/json'
      }
    }).then((response) => {
        console.log(`:: INFO :: Custom Callout Data: ${response.config.data}`); 
        }, (error) => {
          console.log(error);
        });
};

app.listen(PORT, async () => {
  const url = await ngrok.connect(PORT);
  console.log(`:: INFO :: Node.js local server is publicly-accessible at ${url}/`);
  console.log(`:: INFO :: Listening at http://localhost:` + PORT);
  console.log(`:: INFO :: CustomCallout initiated with outgoing IVR`);
  calloutRunMenu(url);
});
