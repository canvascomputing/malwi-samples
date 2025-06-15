# -*- coding: utf-8 -*-

from pywe_decrypt import msg
from pywe_xml import xml_to_dict

from .baseticket import BaseComponentTicket


class ComponentTicket(BaseComponentTicket):
    def __init__(self, appid=None, secret=None, token=None, encodingaeskey=None, storage=None):
        super(ComponentTicket, self).__init__(appid=appid, secret=secret, token=token, encodingaeskey=encodingaeskey, storage=storage)
        # 授权流程技术说明, Refer: https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1453779503&token=&lang=zh_CN
        # 在第三方平台创建审核通过后，微信服务器会向其“授权事件接收URL”每隔10分钟定时推送component_verify_ticket。
        # 第三方平台方在收到ticket推送后也需进行解密（详细请见【消息加解密接入指引】），接收到后必须直接返回字符串success。

    def set_component_verify_ticket(self, appid=None, secret=None, token=None, encodingaeskey=None, post_data=None, encrypt=None, msg_signature=None, timestamp=None, nonce=None, storage=None):
        # Update Params
        self.update_params(appid=appid, secret=secret, token=token, encodingaeskey=encodingaeskey, storage=storage)
        decrypt_msg = msg.decrypt(self.appid, token=self.token, encodingaeskey=self.encodingaeskey, post_data=post_data, encrypt=encrypt, msg_signature=msg_signature, timestamp=timestamp, nonce=nonce)
        component_verify_ticket = xml_to_dict(decrypt_msg).get('ComponentVerifyTicket')
        return self.storage.set(self.component_verify_ticket_key, component_verify_ticket)

    def get_component_verify_ticket(self, appid=None, secret=None, token=None, encodingaeskey=None, storage=None):
        # Update Params
        self.update_params(appid=appid, secret=secret, token=token, encodingaeskey=encodingaeskey, storage=storage)
        return self.storage.get(self.component_verify_ticket_key)


ticketcls = ComponentTicket()
set_component_verify_ticket = ticketcls.set_component_verify_ticket
get_component_verify_ticket = ticketcls.get_component_verify_ticket
