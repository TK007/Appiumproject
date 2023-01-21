import services as services
from twilio.rest import Client
#import os

account_sid = "AC61db60418982c93b5d564640c67fe880"
auth_token = "b9bcbb5a7ea3f966f625874841289773"
client = Client(account_sid, auth_token)

# service = client.sync.services.create()
# print(service.sid)
# message = client.messages.create(
#     to="+919988163919",
#     from_="+13252307093",
#     body="This was sent from twilio")
# messages = client.messages.list(limit=5)
#
# for record in messages:
#
#     print(record.body)

# verification = client.verify \
#                      .services("ISa71e3faeebda79db6c3fa82c51d35c2f") \
#                      .verifications \
#                      .create(to='+13252307093', channel='sms')
#
# print(verification.status)
