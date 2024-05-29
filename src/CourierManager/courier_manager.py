import random
from typing import Optional
from Courier.courier import Courier
import Order
import Address
from Transport.transport import TransportEnum
from Transport.transport import TranSpeedEnum
from Address.address import DistrictEnum
from Address.address import dist
from Area.Area import Area

class CourierManager:
    base: Optional[Courier] 
    
    def __init__(self) -> None:
        self.__areas: list[Area] = [Area() for _ in range(3)]
        self.__matrix_areas_location: list[list[int]] = [[2], [2], [0, 1]]
    # функция которая по заказу определяет курьера, который будет доставлять этот заказ, или определяет
    # что такого нет. От заказа нужно: откуда, куда, как долго можно ехать(в часах), вес(кг), объем(литры).
    # коды ошибок 
    # 0 - все хорошо
    # 1 - не успеем доехать
    # 2 - слишком тяжёлый заказ
    # 3 - слишком объемный заказ
    # 4 - нет свободных курьеров
    def __find_courier(self, order: Order) -> Optional[tuple[Courier, int]]:
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
            if dist(order.start, order.end) / TranSpeedEnum.CAR > order.time_limit:
                return (0, 1)
            
            for cour in self.base:
                if cour.transport == TransportEnum.CAR and cour.active == True:
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
        
        return (0, 1)
    
    def __find_courier(
            self, order: Order, road_length: float
    ) -> Optional[Courier]:
        self.tick()
        courier = self.__areas[order.area].__find_courier(road_length,
                                                                order)
        idx: int = 0
        is_another_area: bool = False
        while idx != len(self.__matrix_areas_location[order.area]) and \
                not isinstance(courier, Courier):
            courier = self.__areas[
                self.__matrix_areas_location[order.area][idx]
            ].__find_courier(road_length, order)
            is_another_area = True
            idx += 1
        if isinstance(courier, Courier):
            courier.current_order = True
            if not is_another_area:
                courier.timer_start(road_length, order.id[0])
            else:
                courier.timer_start(
                    road_length + random.randint(0, 2000), order.id[0]
                )
        return courier
    # функция возвращает все заказы, доставляемые в данный момент
    # если заказа не в списке, значит он был доставлен
    def get_active_orders(self)->Optional[Courier]:
        active_orders = []
        for cour in self.base:
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

    def add_courier(self, courier: Courier):
        self.__areas[courier.area].add_courier(courier)

    
    def tick(self):
        for area in self.__areas:
            area.tick()

    def accept_order(self, order: Order, road_length: float) -> bool:
        self.tick()
        return isinstance(self.__find_courier(order, road_length),
                          Courier)
    
    def get_orders_status(
            self
    ) -> tuple[list[tuple[str, str]], list[tuple[tuple[str, str], int]]]:
        result_orders = [], []
        for area in self.__areas:
            orders = area.get_orders_status()
            result_orders[0].extend(orders[0])
            result_orders[1].extend(orders[1])
        return result_orders