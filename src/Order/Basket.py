from dataclasses import dataclass
from typing import Optional
from Product.Product import Product
from Client.Client import Client
import Sale

class Basket:
    products: Optional[Product]
    totalPriceProduct: int
    priceDelivery: int
    sale: Sale
    owner: Client