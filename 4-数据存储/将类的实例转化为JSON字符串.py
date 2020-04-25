#q1
import json

class Product:
    def __init__(self,name,price,count):
        self.name = name
        self.price = price
        self.count = count

product = Product('特斯拉',1000000,20)
# 设置转换函数
def product2Dict(obj):
    return {
        'name':obj.name,
        'price':obj.price,
        'count':obj.count
    }
#ensure_ascii 默认为ascii码；False显示中文
jsonStr = json.dumps(product,default=product2Dict,ensure_ascii=False)
print(jsonStr)

f = open('files/products.json','r',encoding='utf-8')
jsonStr = f.read()

class Product:
    def __init__(self,d):
        self.__dict__ = d
# 先转化成对象的列表
products = json.loads(jsonStr,object_hook=Product)
print(products) # 对象列表

for product in products:
    print(product.name)

# 转换函数
json.dumps(products,default=product2Dict,ensure_ascii=False)
print(jsonStr)
print(type(jsonStr))
