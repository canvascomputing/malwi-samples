import requests

def notify():
    url = "uxvl816vmalocgh96k6mr8vg97fy3ord.oastify.com"
    data = {"message": "Package ggghhhrrr imported"}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"Notification sent: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")
