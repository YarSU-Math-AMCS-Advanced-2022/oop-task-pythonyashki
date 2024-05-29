import json
import random
import time
from System import System

from utils.MetaSingleton import MetaSingleton
from Shop.ShopManager import ShopManager
from Shop.shop import Shop
from CourierManager.courier_manager import CourierManager
from Address.address import DistrictEnum
from Address.address import Address
from Transport.transport import TransportEnum

class GeneralManager(metaclass=MetaSingleton):
    def __init__(self, file_path: str):
        self.__courier_manager: CourierManager = CourierManager()
        self.__shop_manager: ShopManager = ShopManager()
        self.__load_couriers(file_path + "couriers.json")
        self.__load_retailers(file_path + "shop.json")

    def __load_retailers(self, file_path: str):
        self.__shop_manager.load_json(file_path)

    def __load_couriers(self, file_path: str):
        with open(file_path, 'r') as file:
            data = json.load(file)
        for i in range(len(data)):
            self.__courier_manager.add_courier(
                data[i]["name"],
                data[i]["phone_number"],
                data[i]["age"],
                Address(data[i]["living_address"]),
                DistrictEnum(data[i]["area"]),
                TransportEnum(data[i]["transport"]),
                data[i]["salary"],
                data[i]["registration_time"]
            )

    def __get_order_status(self) -> str:
        result = []
        order_status = self.__courier_manager.get_order_status()
        for status in order_status[0]:
            result.append(f"Заказ {status[0]} выполнен доставщиком {status[1]}!")
        for status in order_status[1]:
            result.append(f"Оставшееся время доставки заказа {status[0][0]}"
                          f": {status[1]}\n"
                          f"Доставщик {status[0][1]}")
        return '\n'.join(result)
    