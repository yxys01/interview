'''
q1:
NoSQL = Not Only SQL
包括非关系数据库外的所有数据库

1.键值（Key-Value）数据库

Redis、Riak、Memcached

适用场景：用来存储用户信息，比如会员、配置文件、参数、购物车等。

2.文档（Document-Oriented）数据库

MongoDB、CouchDB、RavenDB

使用场景：日志、分析数据

3.列存储数据库
HBase、Cassandra

适用场景：日志、博客平台（eg:标签可以存储到一列、类别可以存储到另一列、文章可以存储在另外一列）

4.图数据库
Neo4J、OrientDB

适用场景：
（1）在一些关系型强的数据库可以使用
（2）推荐引擎
'''
'''
q2
pip install pymongo
'''

from pymongo import *
# 创建一个Mongo客户端
Client = MongoClient()
# 相当于数据库本身
db = Client.data
# 获得一个表（实际是一个文档）
products = db.products
# 这里先删除价格大于0的数据（条件，这里没有直接用>而是HTML转义）
# delete_one()即删除第一条符合条件的数据
# delete_many()即删除所有符合条件的数据，返回结果是DeleteResult类型
products.delete_many({'price':{'$gt':0}})

import xmltodict
# 读取xml
f = open('files/products.xml','rt',encoding='utf-8')
xml = f.read()

f.close()
print(xml)
# 解析xml
d = xmltodict.parse(xml)
# 取产品列表
productList = d['root']['products']['product']
print(productList)

# 每迭代一次，插入到MongoDB中
for product in productList:
    product['price'] = int(product['price'])
    # 插入一行；返回插入Id
    productId = products.insert_one(product).inserted_id
    print(productId)

# 从MongoDB中查询；products相当于一个表
for product in products.find({'price':{'$gt':10000}}): # 查询大于10000
    print(product)
