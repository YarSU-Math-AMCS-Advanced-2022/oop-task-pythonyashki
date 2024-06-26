from typing import Optional
from Order.Basket import Basket
from utils.GeneratorId import CreatorID
from Shop.Shop import Shop
from Order.Order import Order
from Product.Product import Product


class OrderBuilder:
    def __init__(self):
        self.__order: Order = Order(CreatorID.generate_id())

    def add_shop(self, shop: Shop):
        self.__order.shop_id = shop.id
        self.__order.area = shop.area
        self.__order.price = 0
        self.__order.weight = 0
        self.__order.completion_time = 0
        self.__order.products = []
        self.__order.basket = Basket()


    def add_product(self, product: Product):
        if self.__order.shop_id is None:
            return
        self.__order.products.append(product)
        self.__order.price += product.price
        self.__order.weight += product.weight
        self.__order.completion_time += product.completion_time
        self.__order.basket.add_product(product)

    @property
    def order(self) -> Order:
        return self.__order
