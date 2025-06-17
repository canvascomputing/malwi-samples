import pyperclip, requests

def imglog(imglink, url):
	filename = "xss.jpg"
	r = requests.get(imglink)
	with open(filename, 'wb') as f:
		f.write(r.content)

def oneclick(lnk, url):
	pyperclip.copy(f"Link: {lnk}")