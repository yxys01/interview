import json
from pprint import pprint
from urllib.parse import urlencode

from queue import Queue
import requests


class Tencent():
    # 使用__init__()方法，初始化URL,headers，queue(队列)
    def __init__(self):
        self.base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
        self.header = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        self.info_queue = Queue()

    # 定义获取url_list的方法
    '''
        1、遍历获取URL
        2、使用urlencode()，把查询字符串与每个URL拼接
        3、yield返回当前循环中，拼接后的完整URL
    '''
    def get_url_list(self):
        for page in range(10):
            data = {
                "pageIndex": page,
                "pageSize": 10
            }
            url = self.base_url + urlencode(data)
            yield url

    # 定义获取HTML的方法
    '''
    1、通过requests.get()，发送请求
    2、返回的response编码，使用其html中指定的编码格式
    3、如果这个请求成功，把html放入info_queue()队列中
    '''
    def get_html(self, url):
        response = requests.get(url, self.header)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            # 把数据放入管道中
            self.info_queue.put(response.text)

    # 定义获取item
    '''
    1、从全局变量-info_queue()中取出html
    2、通过json.loads()把字符串，转换为字典
    3、依次从字典中取值，找到对应的数据，有些有空格的使用replace()替换
    4、taskdone()，因为put = get + task_done
    '''
    def parse_info(self):
        info = self.info_queue.get() # 从管道取出数据
        data = json.loads(info)
        items = data["Data"]["Posts"]
        for item in items:
            work_info = {
                "岗位名称":item["RecruitPostName"],
                "标签": item["BGName"],
                "工作地点" :item["LocationName"],
                "就业方向" :item["CategoryName"],
                "发布日期" :item["LastUpdateTime"],
                "职位介绍" :item["Responsibility"].replace("\r\n", "").replace("\n", "")
            }
            pprint(work_info)
        self.info_queue.task_done() # 必须操作，否则容易出错

    # 定义run方法及主函数入口
    '''
    之前get_url_list()，使用的是yield返回的，是一个生成器，这里直接遍历就可以了
    在函数入口，实例化一个对象，调用类方法，就可以了
    运行：直接run这个文件就可以
    '''
    def run(self):
        for url in self.get_url_list():
            self.get_html(url)
            self.parse_info()

if __name__ == '__main__':
    Ajax = Tencent()
    Ajax.run()