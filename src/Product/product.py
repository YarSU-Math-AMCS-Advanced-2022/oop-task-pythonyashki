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
    weight: Optional[int] = None
    composition: Optional[str] = None
    isHasSale: Optional[bool] = None
    isHightAge: Optional[bool] = None
    count: Optional[int] = None
    def __init__(self, id, name, price, weight, composition):
        print(id)
        id: Optional[int] = id
        name: Optional[str] = name
        price: Optional[int] = price
        weight: Optional[int] = weight
        composition: Optional[str] = composition
        isHasSale: Optional[bool] = None
        isHightAge: Optional[bool] = None
        count: Optional[int] = None

    def set_isHasSale(self, isSale: bool):
        self.isHasSale = isSale

    def set_isHeightAge(self, isHeightAge: bool):
        self.isHightAge = isHeightAge
    
    def set_count(self, count: int): 
        self.count = count


    def __str__(self) -> str:
        return f'Id: {self.id}, Name: {self.name},'\
               f'Price: {self.price}, Has sale: {self.isHasSale}'\
               f'???: {self.weight}, ??????: {self.composition}, ' \
               f'Hight age: {self.isHightAge}, Count: {self.count}'\
               f'Weight: {self.weight}'