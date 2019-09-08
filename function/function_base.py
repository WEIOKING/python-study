import math
# 函数的基础用法


def my_abs(x):
    """
    求输入值的绝对值
    :param x:
    :return:
    """
    # 使用isinstance方法对参数类型进行检测，类型错误则返回异常
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print("my_abs(-123) :", my_abs(-123))


# 多参数和默认参数：
#   默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#   一是必选参数在前，默认参数在后，否则Python的解释器会报错；
#   二是如何设置默认参数。
#   当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#   定义默认参数要牢记一点：默认参数必须指向不变对象！不能指定默认参数为数组等，否则在函数中向数组添加、删除等操作会被
# 保存，使默认参数发生改变

# 坐标点移位函数
def move(x, y, step=1, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


#  函数有默认参数时，默认参数可以不输入，默认使用默认值
print("move(2, 3):", move(2, 3))
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数
xn, yn = move(2, 3, 3)
print("nx, ny:", xn, yn)
#   Python的函数返回多值是返回一个tuple，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置
# 赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
t = move(2, 3, 3, 2)
print("move(2, 3, 3, 2)", t)
# 当函数存在多个默认参数时，当不按顺序提供部分默认参数时，需要把参数名写上
print("move(2, 3, angle=1)", move(2, 3, angle=1))


# 可变参数：
# 参数个数不确定的函数，可以用可变参数来接受参数
# 在参数前加‘*’声明这是一个可变参数
# 在函数内部，可变接收到的是一个tuple

# 多数求和函数
def sums(*nums):
    total = 0
    for n in nums:
        total += n
    return total


# 直接传入多个参数
print("sums(1, 2, 3, 4, 5):", sums(1, 2, 3, 4, 5))
# 如果已经有一个list或者tuple，可以直接在list或tuple前加‘*’，把集合中所有参数当做可变参数传入函数
numbers = [1, 2, 3, 4, 5]
print("sums[*numbers]:", sums(*numbers))


# 关键字参数：
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 在参数前加‘**’声明这是一个关键字参数

# 打印信息函数
def person(name, age, **other):
    print("name:", name, "age:", age, "other:", other)


# 只传入必选参数
person("张三", 22)
# 传入关键字参数
person("张三", 22, city="成都")
# 已经存在一个字典，将字典转换为关键字参数传入函数，在字典前加“**”
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("张三", 22, **extra)


# 命名关键字参数:
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 命名关键字参数必须传入参数名
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *args, city="ChengDu", job):
    print("name:", name, "age:", age, "args:", args, "city:", city, "job:", job)


person("张三", 22, "arg1", "arg2", job="Engineer")


# 参数组合：
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

