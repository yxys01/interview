import requests

url = r"https://m.weibo.cn/api/statuses/repostTimeline?id=4494414712038803&page=1"
html = requests.get(url)
print(html.json()['data']['data'])