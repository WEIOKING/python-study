# -*- encoding: utf-8 -*-
"""
@Name        :test_function_base.py
@Author      : ply
@Description :function_base.py 测试
@Date        :created in 2019/9/8
@ModifiedBy  :
"""
import unittest
from function.function_base import my_abs


class FunctionBaseTestCase(unittest.TestCase):
    def test_my_abs(self):
        """测试my_abs函数"""
        self.assertEqual(20, my_abs(-20))
        self.assertEqual(20, my_abs(20))
        self.assertEqual(0, my_abs(0))


