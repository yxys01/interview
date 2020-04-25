a = [i for i in range(10)]
print(a)
print(type(a))
b = (i for i in range(10))
print(b)
print(type(b))

for i in a:
    print(i)

for i in b:
    print(i * i)

# 正常情况下，将方括号变为圆括号，是由列表变成元组