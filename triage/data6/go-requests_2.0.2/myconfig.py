#!encoding=utf-8
import logging
import os

#PRJ_PATH = os.environ["PRJ_PATH"]

logger = logging.getLogger(__name__)
#logger.debug("Do something")
#logger.info("Finish")
#logger.info("Start print log")
#logger.warning("Something maybe fail.")
#logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

rule_fname = os.path.join(os.path.abspath(os.path.curdir), "rule.regular")
print(rule_fname)
#rule_fname = os.path.join(PRJ_PATH, "rule.regular")

kvs = {}
kvs["上学证明材料等"] = 97
kvs["办理入学诈骗"] = 97
kvs["咨询上学交通"] = 97
kvs["咨询开学时间"] = 97
kvs["子女上学纠纷"] = 97
kvs["上学问题"] = 96

kvs["网络投资平台"] = 95

kvs["举报复工"] = 97
kvs["无法复工"] = 97
kvs["复工咨询"] = 98
kvs["证明材料"] = 97
kvs["复工问题"] = 96

kvs["乞讨"] = 0
kvs["人力中介纠纷"] = 61
kvs["其他"] = 0
kvs["求助"] = 0
kvs["诈骗"] = 0

kvs["感情纠葛"] = 98
kvs["其他原因自杀"] = 97
kvs["其他噪音影响学习"] = 95

kvs["冒充亲朋好友"] = 98
kvs["冒充国家工作人员"] = 98
kvs["冒充客服"] = 97

kvs["噪声影响学习"] = 97
kvs["培训网课扰民"] = 97
kvs["装修影响学习"] = 97
kvs["麻将影响学习"] = 97

kvs["培训退费"] = 97
kvs["培训退费纠纷"] = 97

kvs["失联失踪"] = 97

kvs["挪车"] = 97

kvs["家庭教育纠纷"] = 96
kvs["家庭纠纷(教育)"] = 95
kvs["家庭纠纷(非教育)"] = 95

kvs["小孩误拨打"] = 97

kvs["密闭空间"] = 21
kvs["广场舞影响学习"] = 98
kvs["广场舞扰民"] = 98
kvs["开房"] = 0
kvs["意外伤害"] = 1
kvs["意外受伤"] = 50
kvs["成年人"] = 0
kvs["扰民"] = 0
kvs["施工影响学习"] = 10
kvs["施工扰民"] = 10
kvs["景区购物纠纷"] = 60

kvs["租房纠纷"] = 97

kvs["未成年"] = 0
kvs["未成年自杀"] = 99
kvs["未成年开房"] = 98
kvs["未成年饮酒"] = 97

kvs["机动车与机动车"] = 98
kvs["机动车与行人"] = 97
kvs["机动车与非机动车"] = 97
kvs["非机动车与行人"] = 97
kvs["非机动车与非机动车"] = 97

kvs["殡葬扫墓问题"] = 95

kvs["涉犬类纠纷"] = 0

kvs["涉劳务"] = 98
kvs["涉盗抢骗"] = 98
kvs["涉经济"] = 98
kvs["涉经营"] = 98
kvs["涉贷款"] = 98
kvs["涉饮酒"] = 98
kvs["涉黄赌毒"] = 98
kvs["疾病（精神类）"] = 98
kvs["疾病（非精神类）"] = 98

kvs["居住地不让住（租户）"] = 97
kvs["居住地不让住（非租户）"] = 97

kvs["盗窃车内财物"] = 98
kvs["聚众赌博"] = 97

kvs["薪资纠纷"] = 97
kvs["辞退纠纷"] = 98

kvs["玩耍打闹扰民"] = 10
kvs["玩闹扰民"] = 10
kvs["离家出走"] = 63

kvs["网课诈骗"] = 97

kvs["网课扰民"] = 10
kvs["网贷"] = 0
kvs["自杀"] = 0
kvs["装修扰民"] = 10
kvs["裸聊"] = 0
kvs["误拨打"] = 10
kvs["负样本"] = 1

kvs["贩卖额温枪诈骗"] = 99
kvs["贩卖口罩诈骗"] = 99

kvs["转账打赏"] = 60

kvs["食药环"] = 20
kvs["饮酒"] = 0
kvs["麻将扰民"] = 1
kvs["咨询"] = 0
kvs["纠纷"] = 0
kvs["返沪未隔离"] = 0

