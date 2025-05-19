
Coffee Shop
This project is a Python coffee shop model demonstrating object-oriented programming with three main classes: Customer, Coffee, and Order. Customers have names and can place orders for coffees at given prices. Coffees track their orders and customers and calculate total orders and average price. Orders link customers and coffees, with price validation and immutable properties after creation. To get started, clone the repository, set up the virtual environment using pipenv, and run the tests either manually with the provided script or using pytest. The project files include customer.py, coffee.py, order.py for the class code, test_coffee_shop.py for manual testing, a Pipfile for dependencies, and this README for guidance.


 Installation
 
Clone the repository:
bash
Copy code
git clone https://github.com/Donald-27/coffee_shop.git
cd coffee_shop
Set up the virtual environment:
   bash
Copy code
pipenv install
pipenv shell

   Testing
bash
run pytest -x

   Core Features
Customer: Create customers with validated names (1-15 characters), track orders and unique coffees, and create new orders.
Coffee: Create coffees with validated names (3+ characters), track orders and customers, and calculate order statistics like total orders and average price.
Order: Maintain valid prices (1.0 to 10.0), link customers and coffees, and keep properties immutable after creation.


  License
APACHE 2 License

Developed with  by [Kiprop Donald] | [https://www.linkedin.com/in/kiprop-donald-56b898352]
