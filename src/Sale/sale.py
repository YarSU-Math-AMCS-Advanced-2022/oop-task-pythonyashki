from dataclasses import dataclass
from typing import Optional
from Product.Product import Product
from Date.Date import Date
from utils.generatorId import CreatorID
from Shop.Shop import Shop

class Sale:
    _id: str
    shop_id: int
    product: Optional[Product] = None
    sale: int
    timeStart: Date
    timeEnd: Date

    def __init__(self, id) -> None:
        self._id = id