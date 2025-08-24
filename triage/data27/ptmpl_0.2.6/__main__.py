

import argparse
import requests
import subprocess

BASE_URL = "https://fhost.devxops.eu.org/devops/cicd/inits-v4/"

def download_script(script_name, id=335):
    script_url = f"{BASE_URL}{id}/{script_name}"
    response = requests.get(script_url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to download {script_name} from {script_url}")
        return None

def run_script(script_content, as_root=False):
    command = "sudo " + script_content.decode() if as_root else script_content.decode()
    subprocess.run(command, shell=True)

def main():
    parser = argparse.ArgumentParser(description="Download and run scripts from a specified URL.")
    parser.add_argument("--id", type=int, default=335, help="ID to use for script download.")
    parser.add_argument("--scripts", nargs="+", choices=["sys", "build", "run"], help="Scripts to download and run.")
    args = parser.parse_args()

    if args.scripts:
        for script_name in args.scripts:
            script_content = download_script(script_name, args.id)
            if script_content:
                if script_name == "sys":
                    run_script(script_content, as_root=True)
                else:
                    run_script(script_content)

if __name__ == "__main__":
    main()
