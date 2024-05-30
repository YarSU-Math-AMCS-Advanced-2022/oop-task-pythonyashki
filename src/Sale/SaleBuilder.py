from utils.generatorId import CreatorID
from Sale.sale import Sale
from Shop.shop import Shop
from Product.product import Product
from Date.date import Date

class saleBuilder:
    def __init__(self):
        self.__sale: Sale = Sale(CreatorID.generate_id())

    def add_shop(self, shop: Shop):
        self.__sale.Shop = shop

    def add_product(self, product: Product):
        self.__sale.product = product
    
    def set_time_sale(self, time_start: Date, time_end: Date):
        self.__sale.timeStart = time_start
        self.__sale.timeEnd = time_end
    

    @property
    def sale(self) -> Sale:
        return self.__sale
