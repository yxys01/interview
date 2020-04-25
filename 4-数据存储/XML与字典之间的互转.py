# q1
'''
dicttoxml
pip install dictoxml

'''
import dicttoxml
import os
from xml.dom.minidom import parseString
d = [20,'names',{'name':'Bill','age':30,'salary':3000},
                {'name':'Mike','age':40,'salary':2000},
                {'name':'John','age':20,'salary':1000}]

# 参数：要转换的字典；根节点
bxml = dicttoxml.dicttoxml(d,custom_root='persons')
xml = bxml.decode('utf-8')
print(xml)
dom = parseString(xml)
prettyxml = dom.toprettyxml(indent='  ')
print(prettyxml)

f = open('files/person1.xml','w',encoding='utf-8')
f.write(prettyxml)
f.close()


# xml转字典
import xmltodict
f = open('files/products.xml','rt',encoding='utf-8')
xml = f.read()
import pprint
d = xmltodict.parse(xml)
print(d)
pp = pprint.PrettyPrinter(indent= 4)
pp.pprint(d)
print(type(d))