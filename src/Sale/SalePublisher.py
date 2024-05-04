from Sale import Sale
from typing import Optional
from abc import ABC, abstractmethod

class SubscriberSale(ABC):
    @abstractmethod
    def update(event: str): pass
        

class SalePublisher:
    sales: list
    subscribers: list[SubscriberSale]
    
    def subscribe(self, client_id: str):
        self.subscribe.insert(client_id)
    
    def unsubscribe(self, client_id: str):
        self.subscribe.remove(client_id)

    def notify_subs(self, event):
        for i in len(self.subscribers):
            self.subscribers[i].update(event)
    
        