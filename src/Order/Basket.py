from dataclasses import dataclass
from typing import Optional
from Product.product import Product
from Client.client import Client
import Sale

class Basket:
    products: Optional[Product]
    totalPriceProduct: int
    priceDelivery: int
    sale: Sale
    owner: Client