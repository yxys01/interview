# q1
f = open('./files/readme.txt','r')
print(type(f))
#print(f.read()) # 注意不能调用两次;第一次调用完，文件指针指到文件最后，再调用就什么都没有了

# q2:read、readline、readlines

# read：读取文件的全部内容
#print(f.read()) # 参数n；指定位置
#print(f.read(3)) # hel；如果指定参数n，会读取前n个字符

# 将文件指针移动到指定位置
f.seek(6)
print(f.read(2)) # 你好

f.close()

# readline
f = open('./files/readme.txt','r')
print('------------')
#print(f.readline()) # 只读取第一行
#print(f.readline()) # 再次读取就读取第二行
print(f.readline(3)) # hel;如果指定n，当n比当前行字符个数小，读取当前行前n个字符，如果超过当前行字符个数，那么最多读取当前行的内容
f.close()

# readlines
f = open('./files/readme.txt','r')
print('------------')
#print(f.readlines()) # 读取所有的内容，将每一行分成列表保存（多用于文本处理）
#print(f.readlines(3)) # 如果指定n，那么只会读取所有行字符个数之和大于n的行 （只读取第一行（第一行11个字符））
#print(f.readlines(12)) # 第二行+第一行个数超过11，所有读取第二行
print(f.readlines(24)) # 前两行加起来23个字符；读取前三行
# 注意读取后，文件指针将自动指向下一行开头，第二次使用readlines将会从第一次读取完的下一行开始读取
f.close()