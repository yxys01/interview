'''
Exception

'''

class MyException(Exception):
    pass

# 控制是否抛出异常
num = 12
try:
    if num >= 10:
        # raise主动抛出异常；文本为对异常的描述（如果不用try的时候，会报文本内容的异常错误）
        raise MyException('抛出异常')
    print('正常执行代码')
except MyException:
    print('发生了异常')