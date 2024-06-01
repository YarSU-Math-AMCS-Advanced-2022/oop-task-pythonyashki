import Order
import Person

class Client:
    order: Order
    person: Person
    payCard: int

    def __init__(self, order, person, payCard):
        self.order = order
        self.person = person
        self.payCard = payCard

    # Placing orders that are saved in the order list.
    def place_order(self, order):
        self.orders.append(order)
        print(f"Заказ от {self.person.name} на сумму {order.price} руб. размещен успешно.")

    # Displays a list of orders
    def display_orders(self):
        if self.orders:
            print(f"Список заказов клиента {self.person.name}:")
            for order in self.orders:
                print(f"Заказ ID: {order.order_id}, Сумма: {order.price} руб.")
        else:
            print("У клиента пока нет заказов.")

    # Counting the total amount spent by the person
    def total_spent(self):
        total = sum(order.price for order in self.orders)
        print(f"Общая сумма потраченная клиентом {self.person.name}: {total} руб.")

    # Repeat an order by its ID
    def repeat_order(self, __id):
        for order in self.orders:
            if order.__id == __id:
                self.place_order(order[self.orders.find(order)])
                print(f"Заказ ID {__id} успешно повторен.")
                return
        print(f"Заказ ID {__id} не найден в списке заказов клиента.")
