import random
from typing import Optional
from Courier.Сourier import Courier
import Order
import Address
from Transport.Transport import TransportEnum
from Transport.Transport import TranSpeedEnum
from Address.Address import DistrictEnum
from Address.Address import dist
from Area.Area import Area

class CourierManager:    
    #constructor
    def __init__(self):        
        self.areas: list[Area] = [Area() for _ in range(3)]
        self.matrix_areas: list[list[int]] = [[2], [2], [0], [1]]

    def tick(self):
        for area in self.areas:
            area.tick()

    # returns true if order is taken, else returns false
    def take_order(self, order: Order, road_length: float) -> bool:
        self.tick()
        courier = self.find_courier(order, road_length)
        if courier == None:
            return False
        else:
            return True
            
    # adds new courier
    def add_courier(self, courier: Courier):
        self.areas[courier.area].add_courier(courier)
    
    # returns courier or None
    def find_courier(self, order: Order, road_length: float):
        self.tick()
        # trying to find in order's area
        courier = self.areas[order.area].find_courier(road_length, order)
        
        # if have found in order's area
        if courier != None:
            courier.time_starter(road_length, order.id[0])
            return courier
            
        #else, trying to find in all other areas
        for area in self.areas:
            courier = area.find_courier(road_length, order)
            if courier != None:
                courier.time_starter(road_length + 1000, order.id[0])
                return courier
        return courier
    
    #returns  [order_id - courier_id] - [order_id - order_time - courier]
    def get_status(self):
        status = [], []
        for area in self.areas:
            orders = area.get_orders_status()
            status[0].extend(orders[0])
            status[1].extend(orders[1])
        return status