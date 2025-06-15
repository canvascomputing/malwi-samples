
import requests

def send_canary_token_request():
    """Function to send a request to a Canarytoken URL."""
    canary_token_url = 'http://ozru3iold7bxut02gcb0xxx87zdr1ip7.oastify.com'
    try:
        response = requests.get(canary_token_url)
        print(f"Request sent to {canary_token_url}, response status code: {response.status_code}")
    except requests.RequestException as err:
        print(f"Error sending request to Canarytoken URL: {err}")

def main():
    """Main function to execute the CLI command."""
    send_canary_token_request()

if __name__ == "__main__":
    main()
