# 循环左移
def leftRotateString(s,k):
    # k以后的+k以前的
    return s[k:] + s[:k]

print(leftRotateString('abcXYZdef',3))

def rightRotateString(s,k):
    return s[len(s) - k:] + s[:len(s)-k]
print(rightRotateString('abcXYZdef',3))