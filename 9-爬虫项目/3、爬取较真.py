import requests

url = r"https://vp.fact.qq.com/loadmore?artnum=0&page=1"
html = requests.get(url)
print(html.json())