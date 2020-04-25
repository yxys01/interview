'''
共同点：
都是用来声明静态方法的。类名.方法名（不需要实例化，类就可以调用的方法）

1.@staticemethod 不需要表示自身对象的self和自身类的cls参数，就像普通函数一样定义
2.@classmethod 也不需要self参数，但第2个参数需要是表示自身的cls参数。避免硬编码。

'''

class MyClass:
    bar = 1 # 静态变量
    # 成员（实例）变量，需要实例化才能使用
    def __init__(self):
        self.count = 20

    # 普通方法，必须要加入self，表示自身对象；可以直接引用成员变量
    def process(self):
        print('process:',self.count)
    # 静态方法；不需要传入参数；引用静态变量需要引用类名.变量名
    @staticmethod
    def static_process():
        print('static_process')
        print(MyClass.bar)# 硬编码；如果类名发生改变，这里也必须改变

    # 引用静态变量只用cls.变量名；防止硬编码（MyClass.bar）一旦类名发生改变，cls不需要改变
    @classmethod
    def class_process(cls):
        print('cls_process')
        print(cls.bar)
        print(cls) # cls就是类本身 <class '__main__.MyClass'>
        cls().process() # 实例化
        print(cls().count)

print(MyClass.bar) # 1
MyClass.static_process()
MyClass.class_process()
MyClass.bar = 123
MyClass.static_process()