'''
Module for placing and tracking the orders.
'''

from typing import List
from random import randint

class Item:
    '''
    Represents the information about the item of the order
    containing item name and its price
    '''
    def __init__(self, name: str, price: float):
        '''
        Initialize the item with name and price
        >>> Item('book',110).name
        'book'
        >>> Item('book',110).price
        110
        '''
        self.name = name
        self.price = price

    def __str__(self):
        '''
        Returns representation of the item
        print(Item('book',110))
        book price is 110 UAH.
        '''
        return f"{self.name} price is {self.price} UAH."

class Vehicle:
    '''
    Represents the information about vehicles and their availability
    '''
    def __init__(self, vehicle_no: int, is_available: bool):
        '''
        Initialize the vehicle with its number and availability
        >>> Vehicle(1, True).vehicle_no
        1
        >>> Vehicle(1, True).is_available
        True
        '''
        self.vehicle_no = vehicle_no
        self.is_available = is_available

class Location:
    '''
    Represents the destination of the order.
    city: where the order is headed to
    postoffice: the post office where the order will be delivered
    '''
    def __init__(self, city: str, postoffice: int):
        '''
        Initialize the location
        >>> Location('Kyiv', 1).city
        'Kyiv'
        >>> Location('Kyiv', 1).postoffice
        1
        '''
        self.city = city
        self.postoffice = postoffice

class Order:
    '''
    Represents the information about the order
    user_name: name of the person completing the order
    city: destination of the order
    postoffice: the post office where the order will be delivered
    items: list of items from which the order consists of
    '''
    def __init__(self, user_name: str, city: str, postoffice: int, items: List[Item], vehicle=None):
        '''
        Initialize the order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> my_order.total_price
        154
        >>> my_order.location.city
        'Lviv'
        >>> my_order.user_name
        'Oleg'
        '''
        self.order_id = randint(100000000, 999999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.total_price = sum([item.price for item in self.items])

    def __str__(self):
        '''
        Returns the string representation of an order with his id
        '''
        return f'Your order number is {self.order_id}'

    def calculate_amount(self):
        '''
        Returns the number of items in an order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> my_order.calculate_amount()
        2
        '''
        return len(self.items)

    def assign_vehicle(self, vehicle: Vehicle):
        '''
        Assigns the vehicle to the order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> vehicle = (1, True)
        >>> my_order.assign_vehicle(vehicle)
        >>> my_order.vehicle
        (1, True)
        '''
        self.vehicle = vehicle


class LogisticSystem:
    '''
    Logistic system of trackig and placing the orders
    '''
    def __init__(self, vehicles: List[Vehicle]):
        '''
        Initialize logistic system with a list of vehicles
        >>> log_syst = LogisticSystem([(1, True)])
        >>> log_syst.vehicles
        [(1, True)]
        >>> log_syst.orders
        []
        '''
        self.orders = []
        self.vehicles = vehicles

    def _assign_available_vehicle(self):
        '''
        Finds one of the available vehicles
        >>> log_syst = LogisticSystem([Vehicle(1, True)])
        >>> log_syst._assign_available_vehicle().vehicle_no
        1
        >>> log_syst = LogisticSystem([Vehicle(1, False)])
        >>> log_syst._assign_available_vehicle()
        False
        '''
        for vehicle in self.vehicles:
            if vehicle.is_available:
                return vehicle
        return False

    def place_order(self, order: Order):
        '''
        Adds the order to the list of orders and assigns the vehicle to the order.
        Returns the error message if all the vehicles are unavailable.
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> vehicles = [Vehicle(1, False)]
        >>> log_syst = LogisticSystem(vehicles)
        >>> log_syst.place_order(my_order)
        'There is no available vehicle to deliver an order.'
        '''
        vehicle = self._assign_available_vehicle()
        if vehicle:
            order.assign_vehicle(vehicle)
            vehicle.is_available = False
            self.orders.append(order)
        else:
            return 'There is no available vehicle to deliver an order.'

    def _find_order(self, order_id: int):
        '''
        Finds the order by its order id
        '''
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return False

    def track_order(self, order_id: int):
        '''
        Returns information about order by its id
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> vehicles = [Vehicle(1, True)]
        >>> log_syst = LogisticSystem(vehicles)
        >>> log_syst.track_order(my_order.order_id)
        'No such order.'
        '''
        order = self._find_order(order_id)
        if order:
            return f'Your order #{order.order_id} is sent to {order.location.city}.\
 Total price {order.total_price} UAH.'
        return 'No such order.'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
