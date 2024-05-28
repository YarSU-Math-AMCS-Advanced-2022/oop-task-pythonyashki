import Person
from Address.address import DistrictEnum
from Transport.transport import TransportEnum
import Order
import Address

class Courier(Person):
    # район, в котором курьер работает
    area: DistrictEnum
    transport: TransportEnum
    salary: int
    registration_time: int
    active: bool
    order: Order
    marks: list[float] # оценка курьера
    taken_orders: int # количество доставленных заказов
        
    def __init__(self, name: str,
                 phone_number: str,
                 age: int,
                 living_address: Address,
                 area: DistrictEnum,
                 transport: TransportEnum,
                 salary: int,
                 registration_time: int):
        # конструктор родительского класса
        super().__init__(self, name, phone_number, age, living_address)
        self.area = area
        self.transport = transport
        self.salary = salary
        self.registration_time = registration_time
        self.active = True
        self.order = 0 # пустой(несуществующий) заказ
        self.mark = []
        
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