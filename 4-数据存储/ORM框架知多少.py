'''
q1:
SQLAlchemy:偏向于SQL，可以灵活地提交SQL语句
SQLObject:更加面向对象，无法自由使用原生的SQL语句

pip install sqlobject
'''
from sqlobject import *
from sqlobject.mysql import builder
import json

mysql = 'mysql://root:ff960206@localhost:3306/csdndb?charset=utf8'

sqlhub.processConnection = connectionForURI(mysql,driver='pymysql')

# 将表映射为python对象
class Person(SQLObject):
    class sqlmeta:
        table = 't_persons'
    # 定义表的类型
    name = StringCol(length = 30)
    age = IntCol()
    address = StringCol(length = 30)
    salary = FloatCol

try:
    # 每次先删除，保证新建表
    Person.dropTable()
except:
    pass
Person.createTable()
print('成功创建了t_persons表')
# 每个Person对象，就是一条记录
# 每生成一个对象，就插入一条记录
# 插入记录
person1 = Person(name = 'Bill', age = 55, address = '地球',salary = 1234)
person2 = Person(name = 'Mike', age = 65, address = '月球',salary = 4321)
person3 = Person(name = 'John', age = 15, address = '火星',salary = 4000)
print('成功插入3条记录')

# 修改
person2.name = '李宁'
person3.address = '木星'

# 查询表数据
persons = Person.selectBy(name = 'Bill')
print(persons[0])
print(persons[0].id)
print(persons[0].name)
print(persons[0].age)
print(persons[0].address)

# 删除数据
persons[0].destroySelf()
