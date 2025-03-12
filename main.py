import os
from twilio.rest import Client

account_sid = "ACf256dae43773c52c3428f39b36e3cddb"
auth_token = "c775a9f572324ad96458bed9c4adab72"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+5527998149569",
    from_="+17724947219",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)