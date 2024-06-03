from dataclasses import dataclass
from typing import Optional
from Product.Product import Product
from Client.Client import Client
import Sale
from utils.GeneratorId import CreatorID

class Basket:
    products: Optional[list[Product]]
    totalPriceProduct: int
    priceDelivery: int
    sale: Sale
    owner: Client

    def __init__(self):
        self.id = CreatorID.generate_id()

    def add_product(self, product: Product):
        self.products.append(product)

    def clear_one_product(self, product: Product):
        self.products.remove(product)
        
    def clear_all_product(self):
        self.products.clear()