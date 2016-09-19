from twilio.rest import TwilioRestClient

account_sid = "AC57c1ce6fc9f1af42d65f155cec3d3a04" # Your Account SID from www.twilio.com/console
auth_token  = "275f64fcdb51e9b48a1a5545f95724e7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+16504279837",    # Replace with your phone number
    from_="+16502496741") # Replace with your Twilio number

print(message.sid)
