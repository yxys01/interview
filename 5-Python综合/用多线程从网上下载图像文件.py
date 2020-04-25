from urllib3 import *
import threading
# 初始化
http = PoolManager()
# 关闭警告
disable_warnings()

f = open('urls.txt','r')
urlList = []
while True:
    url = f.readline() # 每次读一行
    if url == '':
        break
    urlList.append(url.strip()) # url添加到urlList中

f.close()
print(urlList)

# 创建一个线程类，指定一个线程函数func，传入的参数args是一个元组类型
class DownloadThread(threading.Thread):
    def __init__(self,func,args):
        super().__init__(target=func,args=args)

# 要下载的url，要保存到本地 filename中
def download(filename,url):
    # 通过request向服务器发出GET请求，得到response
    response = http.request('GET',url)
    # 图像是二进制形式存在
    f = open(filename,'wb')
    # 通过data获取服务端的response
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成')

# 有多少个url，就开多少个线程
for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i) + '.jpg',urlList[i]))
    thread.start()