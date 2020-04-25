'''
[1,2,3]
个数为奇数，中位数为中间的那个数 2
[1,2,3,4]
个数为偶数，中位数为中间两个数之和除以2 （2+3）/2
'''
# 都放到一个类中
class Median:
    # 初始化一个列表
    def __init__(self):
        self.data = []
    # 插入数据
    def insert(self,num):
        self.data.append(num)
        # 排序
        self.data.sort()
    def getMedian(self):
        # 数组长度
        length = len(self.data)
        # 是否为奇数
        if length % 2 == 1:
            # length // 2整除
            return self.data[length // 2]
        return (self.data[length // 2] + self.data[length // 2 -1]) /2.0

median = Median()
median.insert(20)
median.insert(10)
median.insert(30)
print(median.getMedian())
median.insert(15)
print(median.getMedian()) # (10+15)/2
