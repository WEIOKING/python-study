# -*- encoding: utf-8 -*-
"""
@Name        :vector.py
@Author      : ply
@Description : 向量
@Date        :created in 2019/9/15
@ModifiedBy  :
"""
from math import hypot


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #   通过实现特殊方法，自定义数据类型可以表现得跟内置类型一样，从而让我们写出更具表
    # 达力的代码——或者说，更具 Python 风格的代码；
    #   add sub 方法使对象能使用加减法
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        # hypot  返回欧几里德范数 sqrt(x*x + y*y)
        return hypot(self.x, self.y)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)


v1 = Vector(3, 4)
v2 = Vector(-4, 5)
print('v1 + v2 =', v1 + v2)
print('abs(v1) =', abs(v1))
