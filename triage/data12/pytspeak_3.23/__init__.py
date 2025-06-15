from .engine import Engine
import weakref
_activeEngines = weakref.WeakValueDictionary()

def init(driverName=None, debug=False):

    try:
        eng = _activeEngines[driverName]
    except KeyError:
        eng = Engine(driverName, debug)
        _activeEngines[driverName] = eng
    return eng
def speak(text):
    engine = init()
    engine.say(text)
    engine.runAndWait()


