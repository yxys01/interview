import requests

# 定义请求的url
url = 'https://www.lmonkey.com/my/order'

# 定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'cookie':''
}

# 发起get请求
res = requests.get(url,headers=headers)

# 获取响应状态码
code = res.status_code
print(code)

# 响应成功后把响应的内容写入文件中
if code == 200:
    with open('./text.html','w') as fp:
        fp.write(res.text)