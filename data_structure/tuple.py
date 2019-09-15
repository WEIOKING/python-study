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
cheng_du = ('成都', '2000', 1000)
name, year, pop = cheng_du
print(name, year, pop)

