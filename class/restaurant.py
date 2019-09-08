# -*- encoding: utf-8 -*-
"""
@Name        :restaurant.py
@Author      : ply
@Description : 餐厅类
@Date        :created in 2019/9/7
@ModifiedBy  :
"""


class Restaurant:
    def __init__(self, name, type):
        """初始化餐厅名称、餐厅类型、就餐人数默认0"""
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐厅信息"""
        print("restaurant name:" + self.name
              + "\nrestaurant type:" + self.type
              + "\nnumber served:" + str(self.number_served))

    def set_number_served(self, num):
        """设置餐厅接待过的人数"""
        if num < self.number_served:
            print("就餐人数不能小于原有人数！")
        else:
            self.number_served = num

    def increment_number_served(self, num):
        """增加餐厅接待过的人数"""
        if num < 0:
            print("就餐人数不能负增长！")
        else:
            self.number_served += num


yan_yan_restaurant = Restaurant("yan-yan", "Kawana")
yan_yan_restaurant.describe_restaurant()
yan_yan_restaurant.set_number_served(-23)
yan_yan_restaurant.increment_number_served(5)
yan_yan_restaurant.describe_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors

    def ice_flavors(self):
        print(self.flavors)


ice_cream_stand = IceCreamStand("Ice", "Ice Cream", ["Coffee", "Mango"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.ice_flavors()
