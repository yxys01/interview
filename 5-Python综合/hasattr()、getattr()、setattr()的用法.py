'''
python反射机制
hasattr：可以判断一个对象是否包含某个属性
getattr：可以获取对象中某一个属性的值
setattr：可以设置对象中某一个属性的值

检测属性同样能检测方法，在Python中方法和属性没有本质区别
'''

class Person():
    def __init__(self):
        self.name = 'lining'
        self.age = 12
    def show(self):
        print(self.name)
        print(self.age)

if hasattr(Person,'show'):
    print('存在show方法')

person = Person()
setattr(person,'sex','男')
setattr(person,'age',21)

print(getattr(person,'sex'))
print(getattr(person,'age'))
print(getattr(person,'name'))

person.show()