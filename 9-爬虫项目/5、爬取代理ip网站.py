# 爬取代理ip数据

import requests
from lxml import etree

# 定义请求地址
url = 'https://www.xicidaili.com/nn/'
# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

# 发起请求
res = requests.get(url,headers=headers)

# 判断请求状态
if res.status_code == 200:
    # 获取响应数据
    response = res.content.decode('utf-8')
    # 使用XPATH解析html数据
    res_html = etree.HTML(response)
    ips = res_html.xpath('//table[@id="ip_list"]//tr/td[2]//text()')
    ports = res_html.xpath('//table[@id="ip_list"]//tr/td[3]//text()')
    data = list(zip(ips,ports))
    print(data)