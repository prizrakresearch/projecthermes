import requests

# Pushover credentials
APP_TOKEN = "adjpcj5jnhwbutcsszwkj4pkoypvzi"
USER_KEY = "usgw5rbgxfpcozo8dspfzxcmcmywpj"
pushover_mail = "hq87z35m3e@pomail.net"

#Pushing a notification via Pushover
url = "https://api.pushover.net/1/messages.json"
payload = {
    "token": APP_TOKEN,
    "user": USER_KEY,
    "title": "Today's Index Performance Has Been Published 💸❗️",
    "message": "📎 Your market insights are ready - open Hermes to take a look 👀.",
    "priority": 1,
    "sound": "pushover"
    }
files = {
    "attachment": open("/Users/adyothuria/Documents/Python Projects/Hermes/Support & Scheduling Files/notificationImage.jpg", "rb")
}
r = requests.post(url, data=payload, files=files)
if r.status_code == 200:
    print("Post-Execution PushNotification Sent")
else:
    print("Post-Execution PushNotification Failure: ", r.text)