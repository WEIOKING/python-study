# 列表生成器

# 0开始依次生成数字到5结束，5除外
print(list(range(5)))
# 2开始依次生成数字到11,11除外
print(list(range(2, 11)))
# 生成1到10的平方
print([x * x for x in list(range(1, 11))])
# 生成1到10中偶数的平方
print([x * x for x in list(range(1, 11)) if x % 2 == 0])
# 生成1到5与5到10中每个数字求和
print([x + y for x in list(range(1, 6)) for y in list(range(6, 11))])
# 生成1到5中的偶数与5到10中每个数字求和
print([x + y for x in list(range(1, 6)) if x % 2 == 0 for y in list(range(6, 11))])
# 字典生成列表
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
# 将列表中的字符串转化为小写，并过滤掉不为字符串的对象，保证程序正确运行
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])
