with open('files/readme.txt','r') as f:
    data = f.read()

print(data)

'''
key:在文本文件中出现的字符
value：int类型，表示key指定的字符出现的总次数

d:出现的频率
maxChar:表示当前统计出现频率最高的字符

'''
d = {}
maxChar = ''
for c in data:
    # 排除空格
    if c.isspace():
        continue
    # 如果c前面没有出现；d[c]=1;如果c已经出现，d[c]+=1；
    if d.get(c) is None:
        d[c] = 1
        if maxChar == '':
            maxChar = c
    else:
        d[c] += 1
        # 保证maxChar一定是出现次数最多的
        if d[maxChar] < d[c]:
            maxChar = c

print(maxChar)
print(d[maxChar])