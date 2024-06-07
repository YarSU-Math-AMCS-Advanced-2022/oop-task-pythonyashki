from random import randint

from Address.Address import Address
from utils.GeneratorId import CreatorID

class Person:
    iden: str
    name: str
    phone_number: str
    age: int
    living_address: Address    
        
    def __init__(self,name: str,
                 phone_number: str,
                 age: int,
                 living_address: Address):
        self.iden = CreatorID.generate_id()
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.living_address = living_address