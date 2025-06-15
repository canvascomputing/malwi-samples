#!coding=utf-8
"""
rules for ner& text-classify
struct of rules like this

RULE ==> class rule ==> pos/neg rule ==> rules

this is for quick bug location of algorithm of NLP
examples:
"""

__all__ = ["RegularRules", "RegularRulesNer", "ValidTool", "myconfig"]

import os
from collections import defaultdict
import json
import re
from .myconfig import logger
from .myconfig import rule_fname
import pdb
import fcntl
import threading
import time
import threading,time
import queue
import traceback

_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))
q = queue.Queue(maxsize=50)#在里面设置队列的大小

class RegularRules(object):
    """
    all regular of rules is be combine and construct here, to fit check the result and find the wrong quick
    基类,所有规则类的基类
    """

    def __init__(self):
        _ = os.path.dirname(__file__)
        print(_)
        self.build(os.path.join(_, "rule.regular"))
        self.filter_dct = {}

    def add_regs(self, classify, ifpos, regs):
        tmp_dct = self.RULES.get(classify,{})
        tmp_lst = tmp_dct.get(ifpos, [])
        tmp_lst.append(regs)
        tmp_dct[ifpos] = tmp_lst
        self.RULES[classify] = tmp_dct

    def del_regs(self, classify, ifpos, regs):
        temp = self.RULES[classify].get(ifpos, [])
        for reg in regs:
            if reg in temp:
                temp.remove(reg)
        self.RULES[classify][ifpos] = temp

    def get_regs(self, classify, ifpos):
        return self.RULES.get(classify, {}).get(ifpos, [])

    def build(self, name, issave=True):
        pass#print('导入规则的文件', name)
        self.RULES = {}
        '''从RULES_CLASS.txt添加规则'''
        with open(name, "r") as g:
            for line in g.readlines():
                try:
                    if len(line.strip())<4:
                        continue
                    if not "\t" in line:
                        continue
                    assert len(line.split("\t")) == 3
                    _cls, _is, _reg = line.split("\t")
                    #_reg = re.compile(_reg)
                    _reg = _reg[:-1]
                    self.add_regs(_cls, _is, _reg)
                    #print(_cls, _is, _reg)
                except AssertionError:
                    pass#print('assert error: ', line)
                    pass#print(line.split("\t"))
                    continue
                except:
                    traceback.print_exc()
                    pass#print('warning: reg ', line)
                    continue

    def show_all(self):
        '''打印信息'''
        pass
        #logger.info(type(self.RULES))
        #logger.info(self.RULES)
        #logger.info(self.filter_dict)

    def run_all(self, sentences):
        '''预测句子集'''
        filter_dict = defaultdict(dict)
        for sentence in sentences:
            for key in self.RULES:
                for reg in self.RULES[key].get("YES",[]):
                    #logger.info("%s, %s, %s"%(key, reg, self.RULES[key]))
                    #print(list(sentences))

                    filter_res = re.findall(reg, sentence)
                    if len(filter_res)>0:
                        pass#print(">>>YES\n",key,"\nreg:",reg,"\nsent:",sentence,"\nres:", filter_res,"\n")
                        #pdb.set_trace()
                        temp = filter_dict[key].get("YES",[])
                        temp.append(sentence+"\t"+reg)
                        filter_dict[key]["YES"] = list(set(temp))
                for reg in self.RULES[key].get("NO",[]):
                    #logger.info("%s, %s, %s"%(key, reg, self.RULES[key]))
                    filter_res = re.findall(reg, sentence)
                    if len(filter_res)>0:
                        #print(">>>NO\n",key,"\nreg:",reg,"\nsent:",sentence,"\nres:", filter_res,"\n")
                        #pdb.set_trace()
                        temp = filter_dict[key].get("NO",[])
                        temp.append(sentence)
                        filter_dict[key]["NO"] = list(set(temp))
        return filter_dict

    def predict(self, sentences):
        '''预测句子集,外部接口'''
        filter_dct = self.run_all(sentences)
        #logger.info("filter_dct")
        #logger.info(filter_dct)
        return filter_dct

class RegularRulesNer(RegularRules):
    '''
    rewrite the run_all function to surfer RegularRulesNer
    '''
    def run_all(self, sentences):
        '''预测句子集'''
        filter_dict = defaultdict(dict)
        for sentence in sentences:
            for key in self.RULES:
                for reg in self.RULES[key].get("PICK",[]):
                    #logger.info("%s, %s, %s"%(key, reg, self.RULES[key]))
                    #print(list(sentences))
                    filter_res = re.findall(reg, sentence)
                    if len(filter_res)>0:
                        #print(">>>YES\n",key,"\nreg:",reg,"\nsent:",sentence,"\nres:", filter_res,"\n")
                        #pdb.set_trace()
                        temp = filter_dict[key].get("PICK",[])
                        _vi_ = ""
                        for ii in filter_res:
                            if ii in ["",None]:
                                continue
                            if type(ii) == tuple:
                                for iii in list(ii):
                                    if iii in ["",None]:
                                        continue
                                    _vi_+=","
                                    _vi_+=iii
                            elif type(ii) == str:
                                _vi_+=","
                                _vi_+=ii
                            else:
                                pass#print(">>> error: ",ii)
                                pass
                            #_vi_+=";"
                        temp.append(_vi_[1:])
                        filter_dict[key]["PICK"] = list(set(temp))
        return filter_dict

    def predict(self, sentences):
        filter_dct = self.run_all(sentences)
        return filter_dct

class ValidTool(object):
    """验证工具集"""
    def __init__(self):
        pass

    def calcu_acc(self, sentences, labels, pred):
        right = 0
        #print(pred.get("贩毒",{}).get("YES", []))
        for sent,label in zip(sentences,labels):
            labels = label.split(",")
            for lb in labels:
              if sent in pred.get(lb, {}).get("YES",[]):
                right+=1
        #logger.info("right: %s"%right)
        return right

    def format_output(self, sentences, labels, pred):
        response = defaultdict(str)
        #print(pred.get("贩毒",{}).get("YES", []))
        for key in pred:
            sents = pred[key]["YES"]
            for sent in sents:
                temp = response[sent]
                temp+=",%s"%key
                response[sent] = key
        return response

if __name__ == "__main__":
    pass
