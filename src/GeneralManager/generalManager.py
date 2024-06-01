import json
import random
import time
from utils.System import System

from utils.MetaSingleton import MetaSingleton
from Shop.ShopManager import ShopManager
from Shop.Shop import Shop
from CourierManager.Courier_manager import CourierManager
from Address.Address import DistrictEnum
from Address.Address import Address
from Transport.Transport import TransportEnum

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
            result.append(f"Заказ {status[0]} выполнен доcтавщиком {status[1]}!")
        for status in order_status[1]:
            result.append(f"Оѝтавшееѝѝ времѝ доcтавки заказа {status[0][0]}"
                          f": {status[1]}\n"
                          f"Доcтавщик {status[0][1]}")
        return '\n'.join(result)
    
    def start(self):
        while True:
            print('Меню:',
                  '1. Сделать новый заказ',
                  '2. Уточнить cтатуc заказов',
                  '3. Выйти', sep='\n')
            chose = System.validate_integer_in_range(1, 3)
            System.clear_terminal()
            if chose == 1:
                order = self.__shop_manager.make_order()
                if order.is_valid:
                    print(f'Заказ принят. Id заказа {order.id[0][-8:]}.\n'
                          f'Ищем доѝтавщика...')
                    length = random.randint(0, 1000)
                    if not self.__courier_manager.accept_order(
                            order,
                            length
                    ):
                        print('Свободных доставщиков в вашем районе пока нет, '
                              'идет поиск...')
                        while not self.__courier_manager.accept_order(
                                order,
                                length
                        ):
                            print(self.__get_order_status())
                            time.sleep(5)
                            self.__courier_manager.tick()
                    print('Доставщик найден!')
                    _ = input()
                    System.clear_terminal()
            elif chose == 2:
                print(self.__get_order_status())
                _ = input()
                System.clear_terminal()
            elif chose == 3:
                return
            self.__courier_manager.tick()