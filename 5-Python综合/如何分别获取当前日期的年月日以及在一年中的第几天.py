import time

localtime = time.localtime(time.time())
print(localtime)
print(type(localtime))

print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
print(localtime.tm_hour)
# 一年的第几天
print(localtime.tm_yday)
# tm_yday
print(localtime[7])