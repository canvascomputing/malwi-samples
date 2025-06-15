
import sys
import random
import subprocess as sp
from path import Path


def cli(cl, rc = 0, out = None):

    workdir = Path(__file__).dirname()

    P = sp.Popen(cl, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=workdir)

    stdout, stderr = P.communicate()

    if stderr.strip():
        sys.stdout.write(stderr)

    if isinstance(rc, int):
        assert P.returncode == rc
    if isinstance(out, bytes):
        assert stdout.rstrip() == out
    if isinstance(out, str):
        assert stdout.rstrip() == out.encode()

    return stdout


def test_checksum_1():
    cli('k3 sha1 darwin.txt', out=b"56495e2447c7e816cfe28fad4ff85f0a1c041467")
    cli('k3 sha1 feynman.txt', out=b"d6254e6b8f9483aec9b35f5d2a2fa4d7e914f248")
    cli('k3 sha256 feynman.txt', out=b"1ecea1ef0e4985f9eecf50890f0969272b2e68896370ec73979eb14b457e24ca")
    cli('k3 sha256 feynman_copy.txt', out=b"1ecea1ef0e4985f9eecf50890f0969272b2e68896370ec73979eb14b457e24ca")


def test_getset_1():
    "Can we set & retrieve a value associated with a file"
    teststr = 'test{}'.format(random.random())
    cli(f'k3 set test {teststr} feynman.txt')
    cli(f'k3 get test feynman.txt', out=teststr)


def test_getset_2 ():
    "Is a set value unique to a give file (or copy)"
    teststr = 'test{}'.format(random.random())
    cli(f'k3 unset test feynman.txt')
    cli(f'k3 unset test darwin.txt')
    cli(f'k3 set test {teststr} feynman.txt')
    cli(f'k3 get test feynman.txt', out=teststr)
    cli(f'k3 get test feynman_copy.txt', out=teststr)
    cli(f'k3 get test darwin.txt', out='<undefined>')


def test_get_set_unset():
    teststr = 'test{}'.format(random.random())
    cli(f'k3 unset test feynman.txt')
    cli(f'k3 get test feynman.txt', out=f"<undefined>")
    cli(f'k3 set test {teststr} feynman.txt')
    cli(f'k3 get test feynman.txt', out=teststr)
    cli(f'k3 unset test feynman.txt')
    cli(f'k3 get test feynman.txt', out=f"<undefined>")

def test_tag():
    cli('k3 unset tag feynman.txt')
    cli('k3 get tag feynman.txt', out='<undefined>')
    cli('k3 set tag a feynman.txt')
    cli('k3 get tag feynman.txt', out='a')
    cli('k3 set tag b feynman.txt')
    cli('k3 get tag feynman.txt', out='a, b')
    cli('k3 unset tag=a feynman.txt')
    cli('k3 get tag feynman.txt', out='b')
    cli('k3 set tag c feynman.txt')
    cli('k3 get tag feynman.txt', out='b, c')
