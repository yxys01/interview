import requests
import parsel # 数据解析模块

# 1、分析目标网页，确定爬取的url路径，headers参数
base_url = 'https://www.kuaidaili.com/free/inha/2/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

print(base_url)
# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
response = requests.get(base_url, headers=headers)
print(response.request.headers)

# 获取url对应的HTML的文内内容 html字符串
data = response.text
# IP格式 {"协议类型":"ip:端口"}
# 3、解析数据 -- parsel 转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
# 转换数据类型
html_data = parsel.Selector(data)
# 数据解析
parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

proxies_list = []
# 循环遍历
for tr in parse_list:
    dict_proxies = {}
    # td为同级标签，具有索引，从1开始
    # ip
    ip_num = tr.xpath('./td[1]/text()').extract_first()
    # port
    ip_port = tr.xpath('./td[2]/text()').extract_first()
    # 协议类型
    http_type = tr.xpath('./td[4]/text()').extract_first()
    # print(ip_num,ip_port,http_type)
    # 构建ip字典
    dict_proxies[http_type] = ip_num + ':' + ip_port
    proxies_list.append(dict_proxies)

print(proxies_list)
print(len(proxies_list))