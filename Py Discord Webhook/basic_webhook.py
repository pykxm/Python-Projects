# Basic Discord Webhook Sender 

import requests

Webhook_URL = ""
Message = ""
username = ""

data = {
  "content": Message,
  "username": username
}

response = requests.post(Webhook_URL, json=data)

print("Message sent:", Message)
print("Status:", response.status_code)