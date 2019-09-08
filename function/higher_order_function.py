# 导入functools文件的reduce函数
from functools import reduce


# 变量可以指向函数
f = abs
print('f = abs f(-11)', f(-11))


# 传入函数
#   既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, fun):
    """两值在函数处理后求和"""
    return fun(x) + fun(y)


print('add(-5, 6, abs)', add(-5, 6, abs))


# map/reduce
#   map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator
# 返回。
#   map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个
# 序列都计算出来并返回一个list。
def square(x):
    """求平方"""
    return x * x


# 1到5每个数的平方
print('list(map(square, list(range(1, 6))))', list(map(square, list(range(1, 6)))))


#   reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def fn(x, y):
    return x * 10 + y


# 1到 5转换为整数
print('reduce(fn, list(range(1, 6)))', reduce(fn, list(range(1, 6))))


# filter
#   filter()接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是
# 丢弃该元素。

def num_iter():
    """1到正无穷数的生成器"""
    n = 1
    while True:
        n = n + 1
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    it = num_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 10:
        print(n)
    else:
        break


# sorted
#   sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print('sorted([36, 5, -12, 9, -21], key=abs)', sorted([36, 5, -12, 9, -21], key=abs))
#   要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print('sorted([36, 5, -12, 9, -21], key=abs, reverse=True)', sorted([36, 5, -12, 9, -21], key=abs, reverse=True))

