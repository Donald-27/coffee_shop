class Order:
    all_orders = []
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, object):
            raise ValueError("Invalid customer")
        if not isinstance(coffee, object):
            raise ValueError("Invalid coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
