from dataclasses import dataclass
from typing import Optional
from Product.product import Product
from utils.enums import Area

@dataclass
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
    def is_empty_products(self) -> bool:
        return len(self.products) != 0
