import math
def quadratic(a, b, c):
    #数据类型检查可以用内置函数isinstance()实现
    #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    #isinstance() 与 type() 区别：
        #type() 不会认为子类是一种父类类型，不考虑继承关系。
        #isinstance() 会认为子类是一种父类类型，考虑继承关系。
    #如果要判断两个类型是否相同推荐使用 isinstance()。

    if not isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    delta = b**2 - 4*a*c
    if delta < 0:
        print('没有实数根')
    elif delta == 0:
        x = -b/2/a
        print('只有一个实数根')
        return x
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print('有两个实数根')
        return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
