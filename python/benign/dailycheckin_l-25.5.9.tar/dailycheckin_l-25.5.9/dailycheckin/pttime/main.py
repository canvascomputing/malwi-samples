
import requests
import os
import json
import re

from bs4 import BeautifulSoup

from dailycheckin import CheckIn

class PTTime(CheckIn):
    name = "PTTime"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    def sign(self, headers, uid):
        url = "https://www.pttime.org/attendance.php?type=sign&uid={uid}"
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return self.parse_sign_result(response.text)
        else:
            return f"签到失败，状态码: {response.status_code}"

    # 解析签到的html结果
    def parse_sign_result(self, sign_result):

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(sign_result, 'html.parser')

        # 提取用户信息
        user_info = soup.find('span', class_='medium left').text.strip()
        user_name = soup.find('a', class_='PowerUser_Name').text.strip()
        user_id = soup.find('a', class_='PowerUser_Name')['href'].split('=')[-1]

        # 提取用户等级
        # 使用正则表达式提取等级
        pattern = r'\[UID=\d+\]\[(.*?)\]'
        match = re.search(pattern, user_info)

        if match:
            user_level = match.group(1)
        else:
            user_level = 'UNKnow'

        # 提取签到记录
        attendance_info = soup.find('table', class_='mainouter mt5').findChild("td", class_="embedded")

        # 初始化变量
        first_checkin = ''
        days_since_first_checkin = ''
        current_consecutive_start = ''

        for span in attendance_info:
            text = span.text.strip()
            if '第一次签到：' in text:
                first_checkin = text.split('：')[1]
            elif '距今：' in text:
                days_since_first_checkin = text.split('：')[1]
            elif '本次连续签到开始时间：' in text:
                current_consecutive_start = text.split('：')[1]

        # 解析签到记录
        checkin_result = attendance_info.find('p').text
        if '今日签到成功' == checkin_result:
            current_checkin_info = attendance_info.find('ul').find('li').findAll('b')
            total_days = current_checkin_info[0].text
            consecutive_days = current_checkin_info[1].text
            magic_points = current_checkin_info[2].text
            checkin_level = attendance_info.find('span', class_='ml10').find('b').text
            msg = [
                {"name": "用户名", "value": user_name},
                {"name": "用户ID", "value": user_id},
                {"name": "用户等级", "value": user_level},
                {"name": "签到结果", "value": checkin_result},
                {"name": "本次获取魔力", "value": magic_points},
                {"name": "总签到天数", "value": total_days},
                {"name": "连续签到天数", "value": consecutive_days},
                {"name": "第一次签到", "value": first_checkin},
                {"name": "距今", "value": days_since_first_checkin},
                {"name": "本次连续签到开始时间", "value": current_consecutive_start},
                {"name": "签到等级", "value": checkin_level},
            ]
        else:
            msg = [
                {"name": "用户名", "value": user_name},
                {"name": "用户ID", "value": user_id},
                {"name": "用户等级", "value": user_level},
                {"name": "签到结果", "value": "请勿重复签到"},
                {"name": "第一次签到", "value": first_checkin},
            ]
        return msg

    def main(self):
        cookie = self.check_item.get("cookie")
        uid = self.check_item.get("uid")
        headers = {
            "Host": "www.pttime.org",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": cookie,
            "Priority": "u=0, i",
            "Referer": "https://www.pttime.org/",
            "Sec-Ch-Ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        sign_result = self.sign(headers, uid)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in sign_result])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("PTTime", [])[0]
    print(PTTime(check_item=_check_item).main())