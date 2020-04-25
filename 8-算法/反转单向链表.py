'''


'''
# 创建一个类，这个类表示链表里的节点
class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# 创建链表
def reverseLinked(header):
    # 节点或者next为空，直接返回
    if not header or not header.next:
        return header

    # 前一个节点
    pre = None
    # 当前节点
    curNode = header
    # 对当前节点进行循环，直到当前节点为空，即直到当前节点跑到最后一个节点的next中
    while curNode:
        # 保存当前节点的next
        # 临时保存下一个节点
        tmp = curNode.next
        # 要反转就要将后一个节点变成前一个节点
        # 即当前节点的next是前一个节点的pre
        curNode.next = pre # 将前一个节点赋给当前节点的next
        pre = curNode # 将当前节点变成前一个节点，继续向后移
        curNode = tmp # 把当前节点向后移一位
    return pre
# 头节点
header = LinkedNode(0)
node1 = LinkedNode(1)
header.next = node1 # 现在有两个节点
node2 = LinkedNode(2)
node1.next = node2
node3 = LinkedNode(3)
node2.next = node3

# 用于输出整个链表
def printLinked(header):
    p = header
    while p:
        print(p.val, end=' ')
        p = p.next
    print()
printLinked(header)
# 反转
header = reverseLinked(header)
printLinked(header)
