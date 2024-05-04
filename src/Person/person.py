from random import randint

class Person:
    iden: int
    name: str
    phone_number: str
    age: int
    living_address: Address    
        
    def __init__(self,name: str,
                 phone_number: str,
                 age: int,
                 living_address: Address):
        self.iden = randint(1000000000)
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.living_address = living_address