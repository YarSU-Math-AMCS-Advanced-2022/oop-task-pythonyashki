import Courier
import Order
import Address
from Transport.transport import TransportEnum
from Transport.transport import TranSpeedEnum
from Address.address import DistrictEnum
from Address.address import dist

class CourierManager:
    base: [Courier]
    
    # функция которая по заказу определяет курьера, который будет доставлять этот заказ, или определяет
    # что такого нет. От заказа нужно: откуда, куда, как долго можно ехать(в часах), вес(кг), объем(литры).
    # коды ошибок 
    # 0 - все хорошо
    # 1 - не успеем доехать
    # 2 - слишком тяжёлый заказ
    # 3 - слишком объемный заказ
    # 4 - нет свободных курьеров
    def choose_courier(self, order: Order) -> (Courier, int):
        
        # проверяем что есть активные курьеры
        found_active_cour = False
        for cour in self.base:
            if cour.active:
                found_active_cour = True
                break            
        if not found_active_cour:
            return (0, 4)
        
        if order.weight > 7.0 or order.volume > 5.0:
            # считаем, что для большего веса или объема нужна машина
            
            # проверяем что успеем доехать
            if dist(order.start, order.end) / TranSpeedEnum[CAR] > order.time_limit:
                return (0, 1)
            
            for cour in self.base:
                if cour.transport == CAR and cour.active == True:
                    cour.take_order(order)
                    return (cour, 0)
                
            if order.weight > 7.0:
                return (0, 2)
            else:
                return (0, 3)
        
        # вес меньше 7, объем меньше 5
        # проверяем что есть курьеры, которые смогут доставить за требуемое время
        for cour in self.base:
            if cour.active and dist(order.start, order.end) / TranSpeedEnum[cour.transport] <= order.time_limit:
                return (cour, 0)
        
        # иначе говорим, что не успеваем доехать
        return (0, 1)

    # функция возвращает все заказы, доставляемые в данный момент
    # если заказа не в списке, значит он был доставлен
    def get_active_orders()->[Order]:
        active_orders = []
        for cour in base:
            if cour.active == False:
                active_orders.append(cour.order)
        return active_orders
    
    # добавление нового курьеры в базу
    def add_courier(self, 
                 name: str,
                 phone_number: str,
                 age: int,
                 living_address: Address,
                 area: DistrictEnum,
                 transport: TransportEnum,
                 salary: int,
                 registration_time: int) -> None:
        cour = Courier(name, phone_number, age, living_address, area, transport, salary, registration_time)
        self.base.append(cour)