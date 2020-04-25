# 2、 fstring（大括号中可以直接使用各种Python变量）

name = 'Bill'
age = 20

def getAge():
    return 21

s = f"我是{name}，我今年{age}岁，明年{getAge()}岁" # 将变量放到{}中；不仅能放变量也能放函数

print(s)

class Person:
    def __init__(self):
        self.name = 'Mike'
        self.age1 = 40
    def getAge(self):
        return 41

person = Person()

s1 = f"我是{person.name}，我今年{person.age1}岁，明年{person.getAge()}岁"
print(s1)