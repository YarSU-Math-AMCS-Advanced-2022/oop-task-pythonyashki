from dataclasses import dataclass
from Person.Person import Person
from Order.Order import Order
from Address.Address import Address
import time
from Address.Address import DistrictEnum
from Transport.Transport import TranSpeedEnum, TransportEnum

import time

@dataclass
class Courier(Person):
    id: tuple[str]
    area: int
    current_order: bool
    transport: str
    order_time: float
    order_id: str
    time_start: float
    marks: list[float]
    salary: float


    def __init__(self, id, area, current_order, transport, order_time, order_id, time_start): 
        self.id: tuple[str] = id
        self.area: int = area
        self.current_order: bool = current_order
        self.transport: str = transport
        self.order_time: float = order_time
        self.order_id: str = order_id
        self.time_start: float = time_start

    def set_marks(self, marks: list[float]):
        self.marks = marks

    def set_salary(self, salary):
        self.salary = salary
    
    def set_with_order(self, with_order):
        self.with_order = with_order

    #returns true if courier can take the order, else false
    def is_free(self) -> bool:
        if self.with_order:
            return False
        else:
            return True
    
    #returns time needed to finish the order
    def order_time_left(self) -> float:
        return self.order_time - (time.time() - self.start_time)
        
    def time_starter(self, road_length: float, order_id: str) -> None:
        self.order_id = order_id
        self.start_time = time.time()
        self.order_time = road_length / TranSpeedEnum[self.transport]
        
    def tick(self):
        if time.time() - self.start_time >= self.order_time:
            self.with_order = False
        
    def mark_cour(self, mark: int) -> None:
        if 1 <= mark and mark <= 5:
            self.marks.append(float(mark))
            
    def get_mark(self) -> float:
        return sum(self.marks) / len(self.marks)