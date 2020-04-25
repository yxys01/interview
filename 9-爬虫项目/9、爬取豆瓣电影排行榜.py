# 爬取豆瓣电影
import time
import requests
import json
from lxml import etree


def getPage(url):
    '''请求页面数据'''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        # 发起请求
        res = requests.get(url,headers=headers)
        # 判断响应状态
        if res.status_code == 200:
            return res.text
        else:
            return None
    except:
        return None

def parsePage(html):
    '''解析页面数据'''
    html = etree.HTML(html)
    items = html.xpath('//div[@class="item"]')
    # 遍历封装数据并返回
    for item in items:
        res = {
            'index':item.xpath('.//div/em[@class=""]/text()'),
            'image':item.xpath('.//img[@width="100"]/@src'),
            'title':item.xpath('.//span[@class="title"]/text()'),
            'actor':item.xpath('.//p[@class=""]/text()'),
            'score':item.xpath('.//span[@class="rating_num"]/text()')
        }
        yield res

def writeFile(item):
    '''写入数据'''
    with open('./douban.json', 'a', encoding='utf-8') as fp:
        fp.write(json.dumps(item, ensure_ascii=False))
        fp.write('\n')

def main(offset):
    '''主程序函数，负责调度爬虫程序'''
    url = f'https://movie.douban.com/top250?start={offset}'
    # 调用函数进行页面的爬取
    html = getPage(url)
    print(f'正在解析url:{url}')
    if html:
        # 解析页面数据 parsePage(html)
        print(parsePage(html))
        for item in parsePage(html):
            print(f'正在写入数据{item["title"]}')
            # 写入数据 writeFile(item)
            writeFile(item)


if __name__ == '__main__':
    # main(0)
    for i in range(10):
        main(offset=i*25)
        time.sleep(2)


'''
拓展作业：完成一个使用多线程的爬虫程序
'''