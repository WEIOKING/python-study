# -*- encoding: utf-8 -*-
"""
@Name        :tuple.py
@Author      : ply
@Description : 元组
@Date        :created in 2019/9/15
@ModifiedBy  :
"""

#   元组拆包：
#   元组拆包可运用于任何可迭代对象，唯一的硬性要求是，被可迭代对象中的数量必须要跟接受这些元素的元组的空档数一致。
# 除非用‘*’处理多余的字符
from collections import namedtuple

cheng_du = ('成都', '2000', 1000)
name, year, pop = cheng_du
print(name, year, pop)

# * 处理多余字符
name, *info = cheng_du
print(name, info)

# 嵌套元祖拆包
name, *info, (x, y) = ('成都', '2000', 1000, (12, 21))
print(name, info, x, y)

name, *info = ('成都', '2000', 1000, (12, 21))
print(name, info)

#   具名元祖：
#   创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者
# 可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
Vector = namedtuple('Vector', 'x y')
v1 = Vector(1, 2)
#   你可以通过字段名或者位置来获取一个字段的信息。
print(v1, v1.x, v1[1])
v2 = Vector(1, (1, 2))
print(v2)
#   除了从普通元组那里继承来的属性之外，具名元组还有一些自己专有的属性。
#   _fields 属性是一个包含这个类所有字段名称的元组。
print(Vector._fields)
#   用 _make() 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data) 是一样的。
print(Vector._make([12, 34]))
#   _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。
print(v1._asdict())
