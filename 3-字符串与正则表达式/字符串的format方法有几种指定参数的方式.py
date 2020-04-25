# q1
# 默认方式（传入的参数与{}——对应）、命名参数和位置参数{2}

# q2
# 默认
s1 = 'Today is {},the temperature is {} degrees.'
print(s1.format('Saturday',24))
# 命名参数
s2 = 'Today is {day},the temperature is {degree} degrees.'
print(s2.format(degree=30,day='Sunday'))
# 混合使用
s3 = 'Today is {week},{}, the {} temperature is {degree} degrees.'
print(s3.format('abcd',12345,degree=24,week='Sunday'))
# 位置参数(可以改变默认顺序)
s4 = 'Today is {week},{1}, the {0} temperature is {degree} degrees.'
print(s4.format('abcd',1234,degree=45,week='Sunday'))

class Person:
    def __init__(self):
        self.age = 20
        self.name = 'Bill'
    def getName(self):
        return "Mike"

person = Person()

#s5 = "My name is {p.getName()}, my age is {p.age}." #只能访问属性 'Person' object has no attribute 'getName()'
s5 = "My name is {p.name}, my age is {p.age}."
print(s5.format(p=person))