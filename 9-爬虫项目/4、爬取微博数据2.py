import requests
import re
import time

import pandas as pd

from tqdm import tqdm

Cookie = {'Cookie':'_T_WM=56227564299; WEIBOCN_FROM=1110006030; MLOGIN=0; XSRF-TOKEN=e04b20; M_WEIBOCN_PARAMS=oid%3D4494414712038803%26luicode%3D20000061%26lfid%3D4494414712038803%26uicode%3D20000174'}
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0'

for j in tqdm(range(1,10)):
    # 这里地址有点问题
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp={}'.format(j)
    # url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E4%B8%AA%E7%A8%8E%26t%3D0&page_type=searchall&page={}'.format(j)

    time.sleep(4)
    html = requests.get(url,headers = head, cookies = Cookie)

    for i in html.json()['data']['cards']:
        blog = i['mblog']
        ID = blog['id']
        date = blog['created_at']
        text = blog['text']
        text = ''.join(re.findall('[\u4e00-\u9fa5]]',text))
        name = blog['user']['screen_name']
        gender = blog['user']['gender']
        zhuanfa = blog['reposts_count']
        comment = blog['comments_count']
        attitudes = blog['attitudes_count']
        print(ID,date,text,name,gender,zhuanfa,comment,attitudes)