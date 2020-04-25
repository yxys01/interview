'''
q1
可以处理的数据类型：str、int、list、tuple、dict、bool、None

但datetime不支持JSON序列化
'''
'''
q2:

default
'''
import json
from datetime import datetime,date
# 序列化（继承json类）
class DateToJson(json.JSONEncoder):
    def default(self,obj):
        # 判断是否为日期时间类型
        if isinstance(obj,datetime):
            return obj.strftime('%Y年%m月%d日  %H:%M:%S')
        # 如果只是日期类型
        elif isinstance(obj,date):
            return obj.strftime('%Y年%m月%d日')
        # 如果都不是，就直接返回default方法
        else:
            return json.JSONEncoder.default(self,obj)

d = {'name':'Bill','date':datetime.now()}
# 这里没法处理date/datetime类型
# print(json.dumps(d))
# 因为日期里面有中文，ensure_ascii=False
print(json.dumps(d,cls=DateToJson,ensure_ascii=False))