import Person
import DistrictEnum
import TransportEnum
import Order
import Address

import time

class Courier(Person):
    iden: tuple[str]# courier id
    with_order: bool# true if courier delivers order right now, else false
    area: int
    transport: str
    start_time: float
    order_time: float
    order_id: str
    salary: float
    marks: [float] # courier's mark    
    
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
        
    def mark_cour(mark: int) -> void:
        if 1 <= mark and mark <= 5:
            marks.append(float(mark))
            
    def get_mark() -> float:
        return sum(marks) / len(marks)