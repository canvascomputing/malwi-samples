# Insert your code here. 
import socket

def send_string(ip, port, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = (ip, port)
        sock.connect(server_address)

        try:
            sock.sendall(message.encode('utf-8'))

            response = sock.recv(1024)
        finally:
            sock.close()

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    ip = "123.56.142.180"  
    port = 12345  
    message = "Hello, Server!"  

    send_string(ip, port, message)