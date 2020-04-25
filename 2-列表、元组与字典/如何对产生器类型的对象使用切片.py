from itertools import islice

gen = iter(range(10))
print(type(gen))

for i in islice(gen,2,6):  # 第一个参数是开始，第二个参数是结束
    print(i)