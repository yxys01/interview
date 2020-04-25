'''
当频繁请求一个网站时，对方会认为攻击或者盗取数据，禁用ip是反制的有效手段
如何破解这个问题？
爬虫请求不要过快过多

1、推荐方案 就是降低爬虫请求的频率，不要对别人的服务器造成压力
2、使用代理IP

'''
import requests
# from fake_useragent import UserAgent

# ua = UserAgent()

# 定义请求的url
url = 'http://httpbin.org/get'

# headers = {
#     'User-Agent': 'ua.google'
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 定义代理ip
proxies = {
    'http': '171.35.168.113:9999',
    'https': '171.35.168.113:9999'
}

try:
    # 发起get请求
    # res = requests.get(url, headers=headers, proxies=proxies,timeout=5)
    res = requests.get(url, headers=headers)
    # 检测请求状态
    if res.status_code == 200:
        # 获取响应内容
        data = res.json()
        print(data['origin'].split(',')[0])
        print(data)
except:
    print('请求失败')
