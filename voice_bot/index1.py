import audioop
import base64
import json
import os
from flask import Flask, request
from flask_sock import Sock, ConnectionClosed
from twilio.twiml.voice_response import VoiceResponse, Start
from twilio.rest import Client
import vosk

app = Flask(__name__)
sock = Sock(app)
account_sid="ACee3fa2e7fbf7e479f135eaea8e3b8ee9"
auth_token="fc1ad745db3f93d9a4154711f868ae91"
twilio_client = Client(account_sid,auth_token)
model = vosk.Model('model')

CL = '\x1b[0K'
BS = '\x08'


@app.route('/call', methods=['POST'])
def call():
    """Accept a phone call."""
    call = twilio_client.calls.create(
    from_='+1 314 948 5412',
    to='+916296821825',
    url='https://handler.twilio.com/twiml/EH02bc611f248b7a881266e5e91dbb1664?name=Sayani',
    record="True",
    recording_channels="dual"
)
    # TODO


@sock.route('/stream')
def stream(ws):
    """Receive and transcribe audio stream."""
    # TODO


if __name__ == '__main__':
    from pyngrok import ngrok
    port = 5000
    public_url = ngrok.connect(port, bind_tls=True).public_url
    number = twilio_client.incoming_phone_numbers.list()[0]
    number.update(voice_url=public_url + '/call')
    print(f'Waiting for calls on {number.phone_number}')

    app.run(port=port)