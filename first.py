# -*- coding: utf-8 -*-

# base study

print("hello word!!")
# name = input('please enter your name: ')
# print('hello ', name + '!!')
print(r'''line1/\/\\\\///
line2
line3''')
print(3 < 2)
print(3 > 2)
age = 18
if age > 18:
    print('%d > 18' % age)
else:
    print("%d <= 18" % age)
    print("age = %d" % age)
age = 'age'
print(age)
print('%d-%03d' % (678, 1))
print('%.2f' % 3.1415926)
num = [1, 2, 3]
print('数组：', num)
print('num[0]:', num[0])
print('num[-1]', num[-1])
print('length:', len(num))
print('pop:', num.pop())
print('数组：', num)
print('pop(0)', num.pop(0))
print('数组：', num)
num.insert(0, 1)
print("insert 0", num)
num.append(3)
print("append 3", num)
for n in num:
    print(n)
su = 0
for n in range(101):
    su += n
print('sum = ', su)
print(hex(num[0]))
print(hex(su))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print('my_abs(-50) = ', my_abs(-50))


def power(a, b=2):
    r = 1
    while b > 0:
        r = r * a
        b -= 1
    return r


print('5^2 = ', power(5))
print('5^5 = ', power(5, 5))

print('num[0:2]', num[0:2])
print(num)
print('num[-2:]', num[-2:])
