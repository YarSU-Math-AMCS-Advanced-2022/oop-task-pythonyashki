from dataclasses import dataclass
from typing import Optional
from Product.Product import Product
from utils.Enums import Area

# @dataclass
class Order:
    __id: str
    shop_id: Optional[str] = None
    area: Optional[Area] = None
    products: Optional[list[Product]] = None
    weight: Optional[int] = None
    completion_time: Optional[int] = None
    price: Optional[float] = None
    
    @property
    def get_id(self) -> str:
        return self.__id
    

    @property
    def get_products_name(self) -> str:
        result = []
        for product in self.products:
            result.append(product.name)
        return ', '.join(result)
    
    @property
    def is_valid(self) -> bool:
        return not self.is_any_none and len(self.products) != 0
    
    @property
    def is_any_none(self) -> bool:
        return self.shop_id is None or self.area is None or \
            self.products is None or \
            self.price is None

    @property
    def is_empty_products(self) -> bool:
        return len(self.products) != 0
