class MyClass:
    # 方法
    def process(self):
        pass

def process():
    pass

print(type(MyClass().process))
print(type(process))

print(type(MyClass().process).__name__ == 'method')
print(type(process).__name__ == 'function')

from types import MethodType,FunctionType

print('MyClass.process:',isinstance(MyClass().process,FunctionType))
print('MyClass.process:',isinstance(MyClass().process,MethodType))

print('process:',isinstance(process,FunctionType))
print('process:',isinstance(process,MethodType))

