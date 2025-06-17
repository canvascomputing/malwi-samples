import pyperclip, requests

def imglog(imglink):
	filename = "xss.jpg"
	r = requests.get(imglink)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)

def oneclick(lnk):
	pyperclip.copy(f"Link: {lnk}")