from dataclasses import dataclass
from typing import Optional
#id: number
#name: string
#isHasSale: boolean
#price: number:
#isHightAge: boolean
#count: number
#weight: number

@dataclass
class Product:
    """
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