from Sale import Sale
from typing import Optional
from abc import ABC, abstractmethod
from enum import Enum
from utils.enums import EventsSales

class SubscriberSale(ABC):
    @abstractmethod
    def update(event: str): pass


class SalePublisher:
    _owner_shop_id: str
    sales: list
    subscribers: list[SubscriberSale]
    
    def subscribe(self, client_id: str):
        self.subscribe.insert(client_id)
    
    def unsubscribe(self, client_id: str):
        self.subscribe.remove(client_id)

    def notify_subs(self, event: EventsSales, message: str):
        for i in len(self.subscribers):
            self.subscribers[i].update(event, message)


    
        