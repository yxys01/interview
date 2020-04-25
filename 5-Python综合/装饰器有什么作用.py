# q1
'''

装饰器是一个函数
（可以不含任何代码，起装饰作用）
他们是修改其他函数的功能的函数

使用场景
授权(Authorization)
日志(Logging)

'''
from functools import wraps
# 函数嵌套函数
def log(flag):
    def decorate(func):
        @wraps(func)
        def _wrap(*args,**kwargs):
            try:
                if flag:
                    func(*args,**kwargs) # 调用add()函数；可以用于控制函数是否调用
                print('name',func.__name__)
            except Exception as e:
                print(e.args)
        return _wrap
    return decorate # 注意这里不要调用，就返回函数本身

# True 就是前面log()方法中的参数值；func就是add();
# 这里可以控制是否调用add()方法
@log(True)
def add(a,b,c):
    print('sum','=',a+b+c)

add(1,2,3)