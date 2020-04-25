# 分页数据爬取
import time
import requests
from lxml import etree

# 页面请求函数
def getPage(url):
    # 请求指定的url，返回请求的页面
    # 定义请求地址
    url = 'https://www.xicidaili.com/nn/'
    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

    # 发起请求
    res = requests.get(url, headers=headers)

    # 判断请求状态
    if res.status_code == 200:
        # 获取响应数据
        response = res.content.decode('utf-8')
        return response
    else:
        return False

# 解析页面html
def parseHTML(html):
    try:
        # 使用XPATH解析html数据
        res_html = etree.HTML(html)
        ips = res_html.xpath('//table[@id="ip_list"]//tr/td[2]//text()')
        ports = res_html.xpath('//table[@id="ip_list"]//tr/td[3]//text()')
        data = list(zip(ips, ports))
        return data
    except:
        return False
# 测试ip是否好用
def testIP(ip):
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
        'http': f'{ip[0]}:{ip[1]}',
        'https': f'{ip[0]}:{ip[1]}'
    }
    try:
        # 发起get请求
        res = requests.get(url, headers=headers, proxies=proxies,timeout=5)
        # res = requests.get(url, headers=headers)
        # 检测请求状态
        if res.status_code == 200:
            # 获取响应内容
            data = res.json()
            print(data['origin'].split(',')[0])
            print(data)
    except:
        print('请求失败')

# 主程序
def main(num):
    # 拼接url
    url = f'https://www.xicidaili.com/nn/{num}'
    # 调用请求页面的程序
    html = getPage(url)
    if html:
        # 调用解析html的方法
        alist = parseHTML(html)
        if alist:
            # 把返回的解析的数据，去发请求测试是否好用
            oklist = testIP(alist)
            # 把返回的好用的ip数据写入文件

# 如果当前这个脚本是作为主程序使用，那么__name__的结果就是__main__
# 也有可能作为导入包使用，那时不执行主程序
if __name__ == '__main__':
    for i in range(1,11):
        print(f'当前正在爬取第{i}页')
        main(i)
        # 每爬取一个页面后，停顿2秒
        time.sleep(2)