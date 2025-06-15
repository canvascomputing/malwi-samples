import requests, random, time, tests
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
    


def pager(start, num=3): # this function is useful
  nummy = 1
  imlist = getter(start+str(nummy))
  while len(imlist) < num:
    print(1)
    imlist.append(getter(start + str(nummy))) 
    nummy +=1
  resultP = imlist[:num]
  return resultP

        
        
#class horni:
  #Go to horny jail
#  main = "https://yiff-party.com/"
def randomIMG(): # this function is an abomination and I should have used getter() and pager() instead but I'm too lazy to change it now
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
    

def stream(cat="main"):
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









        

