'''
Python支持多继承

'''
class Calculator:
    def calculate(self,expression):
        # 动态？？
        self.value = eval(expression)
        return self.value
    def printResult(self):
        print('result:{}'.format(self.value))

class MyPrint:
    def print(self,msg):
        print('msg:',msg)
    def printResult(self):
        print('计算结果:{}'.format(self.value))
# 多继承
class MyCalculator1(Calculator,MyPrint):
    pass
class MyCalculator2(MyPrint,Calculator):
    pass
my1 = MyCalculator1()
print(my1.calculate("1+3 *5"))
my1.print("hello")

my1.printResult() # 优先调用Calculator的同名方法

my2 = MyCalculator2()
print(my2.calculate("3+5*3"))
my2.print('world')
my2.printResult() # 优先调用MyPrint的同名方法

'''
如果多个父类存在冲突的成员，那么会使用最先遇到的成员
'''