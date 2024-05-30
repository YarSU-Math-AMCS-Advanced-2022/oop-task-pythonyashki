import json
from typing import Optional
from Shop.shop import Shop
from Order.order import Order
from Order.orderBuilder import OrderBuilder
from Product.product import Product
from utils.System import System
from utils.MetaSingleton import MetaSingleton


class ShopManager(metaclass=MetaSingleton):
    """Class-manager of shops and restaurants"""
    def __init__(self):
        self.__shops: list[Shop] = []

    def __str__(self):
        return f'Спиѝок магазинов:\n' + '\n'.join(
            [str(item) for item in self.__shops])

    def add_shop(self, shop: Shop):
        """The method adds a new store or restaurant to the manager"""
        self.__shops.append(shop)

    def load_json(self, file_path: str):
        """The method loads information about stores from a file .json"""
        with open(file_path, 'r') as file:
            data = json.load(file)
        for shops in data:
            self.add_shop(
                Shop(
                    shops['name'],
                    self.__load_product_list(shops['menu']),
                    self.__load_product_list(shops['stop_list']),
                    shops['area']
                )
            )

    @staticmethod
    def __load_product_list(data: list[dict]) -> list[Product]:
        """The method loads a list of products"""
        result: list[Product] = []
        for product in data:
            result.append(
                Product(
                    name=product['name'],
                    price=product['price'],
                    weight=product['weight'],
                    composition=product['composition'],
                    time_cooking=product['time_cooking']
                )
            )
        return result

    def make_order(self) -> Order:
        """
        The method generates an order. Interaction with the user is carried out
        via the console
        """
        self.__update_shops()
        builder = OrderBuilder()
        shop_idx = self.__shop_selection_menu()
        System.clear_terminal()
        while shop_idx is not None:
            builder.add_shop(self.__shops[shop_idx])
            product_idx = self.__product_selection_menu(shop_idx)
            System.clear_terminal()
            while product_idx is not None:
                if product_idx == -1:
                    print('Ваша корзина: ',
                          builder.order.get_products_name, sep='\n')
                else:
                    builder.add_product(
                        self.__shops[shop_idx].menu[product_idx]
                    )
                print('Хотите выбрать что то еще?',
                      '1. Да',
                      '2. Нет, завершить ѝборку заказа', sep='\n')
                chose = System.validate_integer_in_range(1, 2)
                System.clear_terminal()
                if chose == 1:
                    product_idx = self.__product_selection_menu(shop_idx)
                    System.clear_terminal()
                elif chose == 2:
                    return builder.order
                if product_idx is None:
                    print('Еѝли вы выберите другое заведение, то текущий заказ '
                          'ѝброѝитѝѝ. Вы точно хотите ѝто ѝделать?',
                          '1. Да',
                          '2. Нет, вернутьѝѝ в меню заведениѝ', sep='\n')
                    chose = System.validate_integer_in_range(1, 2)
                    System.clear_terminal()
                    if chose == 2:
                        product_idx = self.__product_selection_menu(
                            shop_idx
                        )
            shop_idx = self.__shop_selection_menu()
            System.clear_terminal()
        return builder.order

    def __shop_selection_menu(self) -> Optional[int]:
        """
        The method displays a menu for selecting a store and accepts the response
        the user
        """
        shops_name = self.__get_shops_name_list()
        print(f'Выберите заведение, из которого будет оформлен заказ',
              shops_name,
              f'0. Назад', sep='\n')
        chose = System.validate_integer_in_range(0, len(self.__shops))
        if chose != 0:
            return chose - 1
        else:
            return None

    def __product_selection_menu(self, retailer_idx: int) -> Optional[int]:
        """
        The method displays a menu for selecting items in a store and accepts
        the user's response
        """
        print('Меню заведениѝ: ',
              '0. Перейти в корзину',
              self.__get_shops_menu(retailer_idx),
              f'{len(self.__shops[retailer_idx].menu) + 1}. Назад',
              sep='\n')
        print('Выберите номер')
        chose = System.validate_integer_in_range(
            0,
            len(self.__shops[retailer_idx].menu) + 1
        )
        System.clear_terminal()
        if chose < len(self.__shops[retailer_idx].menu) + 1:
            return chose - 1
        else:
            return None

    def __update_shops(self):
        """The method updates the menu in all shops"""
        for shop in self.__shops:
            shop.updating_menu()

    def __get_shops_name_list(self) -> str:
        """The method generates a list of all shops in the form of a string"""
        result = []
        for number, shop in enumerate(self.__shops):
            result.append(f'{number + 1}. {shop.name}')
        return '\n'.join(result)

    def __get_shops_menu(self, idx: int) -> str:
        """
        The method generates a list of all items in a store in the form
        lines
        """
        result = []
        for number, product in enumerate(self.__shops[idx].menu):
            result.append(f'{number + 1}. {product}')
        return '\n'.join(result)