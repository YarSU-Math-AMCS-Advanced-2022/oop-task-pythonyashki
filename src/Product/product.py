from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """
    Product class:

    Attributes:
    id : int
        product id
    name : string
        product name
    isHasSale:
        flag: whether the product is discounted 
    price : int
        product price
    isHightAge : boolean
        flag: whether the product is expired
    count : int
        amount of product
    weith : int
        weith of product

    """
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[int] = None
    isHasSale: Optional[bool] = None
    isHightAge: Optional[bool] = None
    count: Optional[int] = None
    weight: Optional[int] = None

    def __str__(self) -> str:
        return f'Id: {self.id}, Name: {self.name},'\
               f'Price: {self.price}, Has sale: {self.isHasSale}'\
               f'Hight age: {self.isHightAge}, Count: {self.count}'\
               f'Weight: {self.weight}'