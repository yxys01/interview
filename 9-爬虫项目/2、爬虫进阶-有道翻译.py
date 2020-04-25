# 有道翻译

'''
Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
Request Method: POST

data = {
    'i':'需要翻译的内容',
    'doctype':'json'  # 返回格式
}
'''
import requests

# 函数的封装

# 定义请求的url
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# 注意：访问http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 抛出错误码50
# 将地址中_o删掉即正常访问；百度出来的
# 定义请求的参数
data = {
    'i': '你好',
    'doctype': 'json'
}

# 发起请求 post
res = requests.post(url,data=data)

# 查看请求结果
code = res.status_code
# print(code)
if code == 200:
    # 解析数据
    # print(res.content)
    # print(res.json()) # 如果返回的是json数据，可以直接解析
    resdata = res.json()
    if resdata['errorCode'] == 0:
        # 请求成功
        print(resdata['translateResult'][0][0]['tgt'])