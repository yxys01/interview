from xml.etree.ElementTree import parse
# parse解析xml文档
doc = parse('files/products.xml')
print(type(doc))
# iterfind 输入节点的层次
for item in doc.iterfind('products/product'):
    id = item.findtext('id')
    name = item.findtext('name')
    price = item.findtext('price')
    uuid = item.get('uuid')
    print('uuid', '=', uuid)
    print('id', '=', id)
    print('name', '=', name)
    print('price', '=', price)
    print('-------------')