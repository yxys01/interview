# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:08:41 2019

@author: Single
"""

import requests
import urllib
import base64
import time
import re
import json
import rsa
import binascii
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.packages.urllib3.connectionpool import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://weibo.com/?sudaref=www.baidu.com&display=0&retcode=6102',
    'Connection': 'keep-alive'
}


class Login(object):
    session = requests.session()
    user_name = "17526922476"
    pass_word = "zhuyilong"

    def get_username(self):
        # request.su = sinaSSOEncoder.base64.encode(urlencode(username));
        return base64.b64encode(urllib.parse.quote(self.user_name).encode("utf-8")).decode("utf-8")

    def get_pre_login(self):
        # 取servertime, nonce,pubkey
        # int(time.time() * 1000)
        params = {
            "entry": "weibo",
            "callback": "sinaSSOController.preloginCallBack",
            "su": self.get_username(),
            "rsakt": "mod",
            "checkpin": "1",
            "client": "ssologin.js(v1.4.19)",
            "_": int(time.time() * 1000)
        }
        try:
            response = self.session.post("https://login.sina.com.cn/sso/prelogin.php", params=params, headers=header,
                                         verify=False)
            return json.loads(re.search(r"\((?P<data>.*)\)", response.text).group("data"))
        except:
            print("获取公钥失败")
            return 0

    def get_password(self):
        # RSAKey.setPublic(me.rsaPubkey, "10001");
        # password = RSAKey.encrypt([me.servertime, me.nonce].join("\t") + "\n" + password)
        public_key = rsa.PublicKey(int(self.get_pre_login()["pubkey"], 16), int("10001", 16))
        password_string = str(self.get_pre_login()["servertime"]) + '\t' + str(
            self.get_pre_login()["nonce"]) + '\n' + self.pass_word
        return binascii.b2a_hex(rsa.encrypt(password_string.encode("utf-8"), public_key)).decode("utf-8")

    def login(self):

        post_data = {
            "entry": "weibo",
            "gateway": "1",
            "from": "",
            "savestate": "7",
            "qrcode_flag": "false",
            "useticket": "1",
            "vsnf": "1",
            "su": self.get_username(),
            "service": "miniblog",
            "servertime": self.get_pre_login()["servertime"],
            "nonce": self.get_pre_login()["nonce"],
            "pwencode": "rsa2",
            "rsakv": self.get_pre_login()["rsakv"],
            "sp": self.get_password(),
            "sr": "1536*864",
            "encoding": "UTF-8",
            "prelt": "529",
            "url": "https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
            "returntype": "TEXT"
        }

        login_data = self.session.post("https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)",
                                       data=post_data, headers=header, verify=False)
        params = {
            "ticket": login_data.json()['ticket'],
            "ssosavestate": int(time.time()),
            "callback": "sinaSSOController.doCrossDomainCallBack",
            "scriptId": "ssoscript0",
            "client": "ssologin.js(v1.4.19)",
            "_": int(time.time() * 1000)
        }
        self.session.post("https://passport.weibo.com/wbsso/login", params=params, verify=False, headers=header)
        return self.session


login = Login()
session = login.login()


def get_page_session(date):
    time.sleep(2)
    return session.post(
        "https://s.weibo.com/weibo/?q=%E6%9C%B1%E4%B8%80%E9%BE%99&typeall=1&suball=1×cope=custom:2019-07-01-4:2019-07-01-5&Refer=g&page=1",
        verify=False, headers=header)


def get_data_session(date, page):
    time.sleep(2)
    return session.post(
        "https://s.weibo.com/weibo/?q=%E6%9C%B1%E4%B8%80%E9%BE%99&typeall=1&suball=1×cope=custom:2019-07-01-4:2019-07-01-5&Refer=g&page=2",
        verify=False, headers=header)


def get_page_res(date):
    try:
        return get_page_session(date)
    except:
        try:
            return get_page_session(date)
        except:
            print("获取页码信息失败", date)
            return 0


def get_data_res(date, page):
    try:
        return get_data_session(date, page)
    except:
        try:
            return get_data_session(date, page)
        except:
            print("获取页码信息失败", date, page)
            return 0


def get_page(date):
    response = get_page_res(date)
    if response:
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            pages = soup.find("ul", "s-scroll").find_all("li")
            return len(pages)
        except:
            print("获取页码失败", date)
            return 0


def get_data(date, page):
    response = get_data_res(date, page)
    data = list()
    if response:
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            infos = soup.find_all('div', "content")
            records = soup.find_all("div", "card-act")
            for info, record in zip(infos[0:], records[0:]):
                times = "".join(info.find('p', 'from').text)
                data.append("".join(times.split()[0]))
                data.append("".join(times.split()[1]))

                user = info.find('a', "name")
                data.append("".join(user.text))

                content = info.find('p', "txt")
                data.append("".join(content.text.strip().replace(' \u200b', '')))

                recs = record.find_all('li')
                data.append("".join(re.findall(r'转发 (.+?)', recs[1].text, re.S)))
                data.append("".join(re.findall(r'评论 (.+?)', recs[2].text, re.S)))
                data.append("".join(recs[3].text.split()))
        except:
            pass
    return data


def save_data_to_csv(data):
    data = np.array(data).reshape(-1, 7)
    result_weibo = pd.DataFrame(data)
    result_weibo.to_csv(data_file_name, mode='a', index=False, encoding='gb18030', header=False)


data_file_name = "./朱一龙.csv"
column = pd.DataFrame({}, columns=['日期', '时间', '用户', '内容', '转发', '评论', '点赞'])
column.to_csv(data_file_name, index=False, encoding='gb18030')
save_data_to_csv(get_data(2019, 5))