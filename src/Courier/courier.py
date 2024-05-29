from Person.person import Person
from Order.Order import Order
from Address.address import Address
import time
from Address.address import DistrictEnum
from Transport.transport import TransportEnum



class Courier(Person):
    id: tuple[str]
    area: DistrictEnum
    transport: TransportEnum
    salary: int
    registration_time: int
    active: bool
    order: Order
    order_time: float
    order_id: str
    marks: list[float] 
    taken_orders: int 
    time_start: float
        
    def __init__(self, 
                 name: str,
                 phone_number: str,
                 age: int,
                 living_address: Address,
                 area: DistrictEnum,
                 transport: TransportEnum,
                 salary: int,
                 registration_time: int,
                 ):
        
        super().__init__(self, name, phone_number, age, living_address)
        self.area = area
        self.transport = transport
        self.salary = salary
        self.registration_time = registration_time
        self.active = True
        self.order = 0 
        self.mark = []
        self.time_start = 0

    @property
    def is_free(self) -> bool:
        return self.current_order is False

    @property
    def time_left(self) -> float:
        return self.order_time - (time.time() - self.time_start)

    @property
    def timer_start(self, road_length: float, order_id: str):
        self.order_id = order_id
        self.time_start = time.time()
        self.order_time = road_length / TransportEnum[self.transport].value


    def tick(self) -> None:
        if time.time() - self.time_start >= self.order_time:
            self.current_order = False


    def take_order(self, order: Order) -> None:
        self.active = False
        self.order = order
    
    
    def finish_order(self, order: Order) -> None:
        self.active = True
        self.order = 0
        
    def mark_cour(self, mark: int) -> None:
        if 1 <= mark and mark <= 5:
            self.marks.append(float(mark))
            
    def get_mark(self) -> float:
        return sum(self.marks) / len(self.marks)