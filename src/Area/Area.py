from typing import Dict, Optional
from Order.Order import Order
from Courier.Courier import Courier

DISTANCES: tuple = (850, 1700, 3000)


def define_initial_transport_idx(distance: float, order: Order) -> int:
    """
    AFOOT - 0
    BICYCLE - 1
    SCOOTER - 2
    CAR - 3
    """
    transport_idx: int = 0
    if order.weight < 15000:
        while distance > DISTANCES[transport_idx] and transport_idx < 3:
            transport_idx += 1
    else:
        transport_idx = 3
    return transport_idx


class Area:
    def __init__(self):
        self.area_courier: Dict[str, Dict[str, list[Courier]]] = \
            {'AFOOT': {'active': [],
                       'inactive': []},
             'BICYCLE': {'active': [],
                         'inactive': []},
             'SCOOTER': {'active': [],
                         'inactive': []},
             'CAR': {'active': [],
                     'inactive': []}
             }
        self.__courier_status: Dict[str, tuple[Order, Courier]]
        self.ready_orders: list[tuple[str, str]] = []

    def tick(self):
        for key in self.area_courier.keys():
            save_courier: list[Courier] = []
            for courier in self.area_courier[key]['active']:
                courier.tick()
                if courier.is_free:
                    self.area_courier[key]['inactive'].append(courier)
                    self.ready_orders.append(
                        (courier.order_id, courier.id[0])
                    )
                    self.__courier_status.pop(courier.order_id)
                else:
                    save_courier.append(courier)
            self.area_courier[key]['active'].clear()
            self.area_courier[key]['active'] = save_courier

    def get_orders_status(
            self
    ) -> tuple[list[tuple[str, str]], list[tuple[tuple[str, str], int]]]:
        ready_orders: list[tuple[str, str]] = self.ready_orders.copy()
        self.ready_orders.clear()
        active_orders: list[tuple[tuple[str, str], int]] = []
        for order_id in self.__courier_status.keys():
            active_orders.append((
                (order_id, self.__courier_status[order_id][1].id[0]),
                int(self.__courier_status[order_id][1].time_left)
            ))
        return ready_orders, active_orders

    def add_courier(self, courier: Courier):
        self.area_courier[courier.transport]['inactive'].append(
            courier
        )

    def find_deliveryman(
            self, road_length: float, order: Order
    ) -> Optional[Courier]:
        idx: int = define_initial_transport_idx(road_length, order)

        for key in list(self.area_courier.keys())[idx:]:
            if len(self.area_courier[key]['inactive']):
                courier = self.area_courier[key]['inactive'].pop()
                self.area_courier[key]['active'].append(courier)
                self.__courier_status[order.id[0]] = (order, courier)
                return courier
        return None
