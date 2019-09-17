# -*- encoding: utf-8 -*-
"""
@Name        :list.py
@Author      : ply
@Description : 列表
@Date        :created in 2019/9/17
@ModifiedBy  :
"""
l = list(range(1, 11))
print('l :', l)
#   切片：
print('l[2:5] :', l[2:5])
print('l[::2] :', l[::2])
print('l[1:5:2] :', l[1:5:2])
print('l[::-2] :', l[::-2])

l[2:3] = [33]
print('l[2:3] = [33]')
print('l :', l)
del l[1:3]
print('del l[1:3]')
print('l :', l)

#   切片对象 slice(start, stop, step)
s = slice(0, 2)
print('l[s]  :', l[s])

#   序列使用 + *
print('l + l :', l + l)
print('3 * l :', 3 * l)
