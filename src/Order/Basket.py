from dataclasses import dataclass
from typing import Optional
from Product.product import product
from Client.client import Client
import Sale

class Basket:
    products: Optional[product]
    totalPriceProduct: int
    priceDelivery: int
    sale: Sale
    owner: Client