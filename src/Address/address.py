from enum import Enum
from typing import Dict, Optional

# from Courier.courier import Courier
# from Order.Order import Order

class DistrictEnum(Enum):
    UNDEFINE = 0
    BRAGINO = 1
    ZAVOLGA = 2
    KIROVSKYI = 3
    LENINSKYI = 4
    FRUNZENSKYI = 5
    KRASNOPEREKOPSKYI = 6

class Address:
    country: str
    city: str
    district: DistrictEnum
    street: str
    house_number: int
    apart_number: int
        
    def __init__(self, country: str,
                 city: str,
                 district: DistrictEnum,
                 street: str,
                 house_number: int,
                 apart_number: int):
        self.country = country
        self.city = city
        self.district = district
        self.street = street
        self.house_number = house_number
        self.apart_number = apart_number

def dist(adrs1: Address, adrs2: Address) -> float:
    return