# -*- encoding: utf-8 -*-
"""
@Name        :file_read_write.py
@Author      : ply
@Description :
@Date        :created in 2019/9/7
@ModifiedBy  :
"""
filename = 'testFile.txt'

# 写入模式打开文件，如果文件已存在，写入的内容会覆盖原内容
with open(filename, 'w') as file_obj:
    file_obj.write("first line!\n")
    file_obj.write("second line!\n")
    file_obj.write("threed line!\n")


def print_file(file_name):
    """打印文件每一行内容"""
    with open(file_name) as file_obj:
        print(file_obj.read())
        for line in file_obj:
            print(line)


print_file(filename)
# 附加模式打开文件，会在问价后追加新增内容
with open(filename, 'a') as file_obj:
    file_obj.write("fourth line!")

print_file(filename)
