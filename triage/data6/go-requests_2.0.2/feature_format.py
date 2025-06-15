#!encoding=utf-8

import json
import os
import sys
import re
import pandas as pd
sys.path.append(os.environ["PRJ_PATH"])
from nlp_rules.myconfig import PRJ_PATH
import time
import traceback

PHONE2LOC = pd.read_csv(os.path.join(PRJ_PATH, "data/PHONE2LOC.csv"))
PHONE2LOC_DCT = {}
for items in PHONE2LOC.iterrows():
    try:
        _loc = items[1][0].split("\t")[0]
        _items = items[1][0].split("\t")[1]
        PHONE2LOC_DCT[_items[3:9]] = _loc
    except:
        traceback.print_exc()
        pass
#print(PHONE2LOC_DCT)

def age2group(age):
    """ 年纪划入年龄段 """
    if len(re.findall("^[0-6][周多]?岁", age))>0:
        return "婴幼儿" # 0-6
    elif len(re.findall("^((?:[1[0-2]|[789])[周多]?岁)|^([一二三四五六]年级)", age))>0:
        pass#print(age)
        return "少儿" # 7-12
    elif len(re.findall("^((?:1[3-7])[周多]?岁)|^([七八九]年级)|^([初高][中一二三])", age))>0:
        return "青少年" # 13-17
    elif len(re.findall("^(1[8-9]|[234][0-9]|4[0-5])[周多]?岁", age))>0:
        return "青年" # 18-45
    elif len(re.findall("^(4[0-6]|[56][0-9])[周多]?岁", age))>0:
        return "中年" # 46-69
    elif len(re.findall("^[789]\d[周多]?岁", age))>0:
        return "老年" # >69
    else:
        return "未查询到年龄段"

def idAnalysis(idnum):
    dat = idnum[6:10]
    age = 2020-int(dat)
    pass#print(age)
    return age2group(str(age)+"岁")

def phone2loc(phone_num):
    """ 手机转地址 """
    rec_phone_num = str(phone_num)[:6]
    return PHONE2LOC_DCT.get(rec_phone_num, "未查到手机号归属地")

def time_format(_time_):
    """ 时间格式化 """
    #localtime = time.localtime(_time_)
    #print ("格式化时间为 :", localtime)
    a = "Sat Mar 28 22:24:24 2016"
    #print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
    return time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

if __name__ == "__main__":
    phone_num = "17109696934"
    """
    print(
    phone2loc(phone_num),
    age2group("87岁"),
    idAnalysis("513821198306140191"),
    time_format("2020-01-01"),)
    """


