from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer - must be Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee - must be Coffee instance")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all_orders.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @property
    def price(self) -> float:
        return self._price