import requests

def main():
    url = "hook_url"
    body = {
        "channel": "channel_original_name",
        "username": "Basic-Bot",
        "icon_url": "https://cdn-icons-png.flaticon.com/512/785/785116.png",
        "text": "Awesome message to send to the channel",
    }

    r = requests.post(url,  json=body,)

main()
