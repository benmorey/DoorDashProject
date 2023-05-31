# Bayley Welsh, Donna Kim, Ken Hall, Mason Wooden, Ben Morey
# Door Dash
# Program that simulates orders at a fast food restaurant. Program tracks orders from a given set of customer names, then orders and displays this data

# Imports random module to enable generation of random numbers for number of burgers
import random

# Beginning of Order class. Generates random number of burgers for each order
class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    # Method that generates random number of burgers for each order, from 1 to 20
    def randomBurgers(self):
        return random.randint(1, 20)

# Beginning of Person class. Parent of Customer class 
class Person():
    def __init__(self):
        self.customer_name = self.randomName()
    
    # Method that accesses a list of customer names and randomly selects a name for each order
    def randomName(self):
        # List of customers
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Snowman", "Singing Bush"]
        return random.choice(asCustomers)

# Beginning of Customer class. Inherits Person class and creates an order for each customer.
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# Creates queue and dictionary to store customer info (name and number of burgers ordered) and history
# List will be used to record all orders, dictionary will be used to create a sum of the history
queueCustomers = []
customerInfo = {}

# FOR loop that generates and adds 100 orders to the list of orders in the queue. 
for customers in range(0, 99):
    # Creates customer object for each customer
    customerInQueue = Customer()
    # Adds customer to queue
    queueCustomers.append(customerInQueue)
   
# WHILE loop adds customer to dictionary if not already added, as well as keeps a running total of customers orders
while len(queueCustomers) > 0:
    # Removes first customer from queue to simulate a line in a restaurant, fuliflling the orders of each customer
    currentCustomer = queueCustomers.pop(0)

    # IF statement that adds customer (name and running total of burgers ordered) to dictionary if the customer has not already been recorded
    if currentCustomer.customer_name not in customerInfo:
        customerInfo[currentCustomer.customer_name] = currentCustomer.order.burger_count
    else:
        customerInfo[currentCustomer.customer_name] += currentCustomer.order.burger_count

# Sorts dictionary data into a list by number of burgers ordered (descending)
listSortedCustomers = sorted(customerInfo.items(), key=lambda x: x[1], reverse=True)

# FOR loop that prints formatted list of customer name and burgers ordered
for item in listSortedCustomers:
    # Formats output
    print(item[0].ljust(19) + str(item[1]))

