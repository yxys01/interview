import requests

# 需要请求的URL
url = 'https://www.zmz2019/com/User/User'

# 登录请求的地址
# ajaxlogin需要在F12之后勾选preservelog之后才会出现
login_url = 'https://www.zmz2019/com/User/Login/ajaxLogin'

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'cookie':''
}

# 如果需要爬虫程序主动记录cookie并且携带cookie，那么在使用requests之前先调用session方法
# 并且使用session方法返回的对象发送请求即可
req = requests.session()


# 登录请求时的数据
data = {
    'account':'xxx@ddd.com',
    'password':'xxxxx',
    'remember':'1',
    'url_back':'https://www.zmz2019/com/User/User'


}

# 发起登录请求
res = req.post(url=login_url,headers=headers,data=data)

# 判断状态
code = res.status_code
print(code)

if code == 200:
    # 发起新的请求，去获取目标数据
    # 这里要用session返回的对象
    res = req.get(url=url,headers=headers)
    with open('rr.html','w',encoding='utf-8') as fp:
        fp.write(res.text)

