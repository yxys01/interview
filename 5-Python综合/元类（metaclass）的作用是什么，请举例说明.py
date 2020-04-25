'''
metaclass：元类，类似于创建类的模板，所有的类都是通过他来创建的，可以自由控制类的创建过程

单例模式、ORM模式

'''
# 元类（创建过程类似创建类）
class Singleton(type):
    def __init__(self,*args,**kwargs):
        print('in __init__')
        # 声明一个成员变量
        self.__instance = None
        # 传入参数
        super(Singleton,self).__init__(*args,**kwargs)

    # 创建类的实例时，自动调用
    def __call__(self, *args, **kwargs):
        print('in __call__')
        # 为空创建类的实例；不为空返回类的实例
        if self.__instance is None:
            # 创建实例；通过调用__call__，调用了类的实例;通过Singleton这个元类来修饰了类的本身
            self.__instance = super(Singleton,self).__call__(*args,**kwargs)
            print(type(self.__instance))
        return self.__instance

class MyClass(metaclass=Singleton):
    pass

# 调用MyClass()时，自动调用__call__来创建实例；__call__实际上是MyClass()这个动作的拦截器
my1 = MyClass()
my2 = MyClass() #已经创建实例了，只返回实例，即只调用'in __call__'

# my1和my2 是同一个实例，也就是单例模式
print(my1 is my2)
