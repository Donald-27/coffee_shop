# customer.py
from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None

        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        return max(customer_spending, key=customer_spending.get)
