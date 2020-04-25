import json

class Product:
    def __init__(self,d):
        self.__dict__ = d # 也可以一个一个的属性建立

f = open('files/product.json','r')
jsonStr = f.read()
print(jsonStr)
# JSON转化为字典
product = json.loads(jsonStr)
print(product)
print(type(product))
print(product['name'])

# JSON转化为对象
# 先创建字典对象jsonStr，然后将其作为参数d传入类Product，将key，value映射到Product中
product = json.loads(jsonStr,object_hook=Product)
print(type(product))
print(product.name)
print(product.price)

# 法2
def json2Product(d):
    return Product(d)

# 传入一个函数指针;object_hook即可传入类，也可传入一个转换函数
product1 = json.loads(jsonStr,object_hook=json2Product)
print(product1.name)
print(product1.price)