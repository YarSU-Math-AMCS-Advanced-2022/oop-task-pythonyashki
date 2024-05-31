from random import randint
from Address.Address import Address
from utils.GeneratorId import CreatorID
from Product.Product import Product


class Shop:
    def __init__(
            self, name: str,
            menu: list[Product],
            stop_list: list[Product],
            area: Address
    ):
        self.__id: tuple[str] = CreatorID.generate_id()
        self.__name: str = name
        self.__menu: list[Product] = menu
        self.__stop_list: list[Product] = stop_list
        self.__area: Address = Address

    def __str__(self):
        return f'Имѝ: {self.__name}, ' \
               f'Меню: {[str(item) for item in self.__menu]}, ' \
               f'Стоп лиѝт: {self.__stop_list}'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> tuple[str]:
        return self.__id

    @property
    def menu(self) -> list[Product]:
        return self.__menu

    @property
    def stop_list(self) -> list[Product]:
        return self.__stop_list

    @property
    def area(self) -> Address:
        return self.__area

    # The method of randomly updating the menu so that it is not as boring as possible :)
    def updating_menu(self):
        temp = randint(0, 1)
        selected_product_stop_list = None
        if temp == 1:
            if len(self.__stop_list) != 0:
                selected_product_stop_list = self.__stop_list[
                    randint(0, len(self.__stop_list) - 1)]
                self.__stop_list.remove(selected_product_stop_list)
        temp = randint(0, 1)
        # Removing it from the menu
        if temp == 1 and len(self.__stop_list) < len(self.__menu):
            if len(self.__menu) != 0:
                selected_product_menu = self.__menu[
                    randint(0, len(self.__menu) - 1)]
                self.__stop_list.append(selected_product_menu)
                self.__menu.remove(selected_product_menu)
        # Return to the menu
        if selected_product_stop_list is not None:
            self.__menu.append(selected_product_stop_list)
        return self.__menu
