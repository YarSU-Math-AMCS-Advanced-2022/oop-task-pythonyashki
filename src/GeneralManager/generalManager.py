import json
import random
import time

from utils.MetaSingleton import MetaSingleton
from Shop.ShopManager import ShopManager
from Shop.shop import Shop
from CourierManager.courier_manager import CourierManager
class GeneralManager(metaclass=MetaSingleton):
    def __init__(self, file_path: str):
        self.__courier_manager: CourierManager = CourierManager()
        self.__shop: Shop = Shop()

    def __load_retailers(self, file_path: str):
        with open(file_path, 'r') as file:
            data = json.load(file)
        for retailer in data:
            self.__courier_manager.add_courier()

        