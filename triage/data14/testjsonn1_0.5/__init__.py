


import requests
import subprocess
import os

def main(url, filename):
    # Download the file
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file saved as {filename}")
        
        # Execute the file
        try:
            subprocess.run(['pythonw', filename], check=True)
            print(f"Execution of {filename} was successful.")
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage
