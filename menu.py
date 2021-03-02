import sys
from logistic_system import Item, Vehicle, Order, Location, LogisticSystem

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.log_syst = LogisticSystem(vehicles=[])
        self.items = []
        self.choices = {
                "1": self.add_vehicle,
                "2": self.add_item,
                "3": self.complete_order,
                "4": self.trackOrder,
                "5": self.quit
                
}
    def display_menu(self):
        print("""
Logistic System Menu
1. Add Vehicles
2. Add Item To The Cart
3. Complete The Order
4. Track The Order
5. Quit """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            option = input('Please, input one of the option: ')
            action = self.choices.get(option)
            if action:
                action()
            else:
                print(f'{option} is an invalid option.')
    
    def add_vehicle(self):
        vehicle_No = int(input('Please, enter the number of the vehicle: '))
        vehicle = Vehicle(vehicle_No, True)
        self.log_syst.vehicles.append(vehicle)
    
    def add_item(self):
        item_name = input('Please, input the name of the item: ')
        try:
            item_price = float(input(f'Please, input the price of the {item_name}: '))
            item = Item(item_name, item_price)
            self.items.append(item)
        except ValueError:
            print('Something went wrong, please, try again.')


    def complete_order(self):
        user_name = input('Please, input your name: ')
        city = input('Please, input your city: ')
        postoffice = input('Please, input postoffice to deliver: ')
        order = Order(user_name, city, postoffice, self.items)
        print(order)
        self.log_syst.place_order(order)

    def trackOrder(self):
        flag = input('If you want to go through all the orders, type "Yes": ')
        if flag == 'Yes':
            for order in self.log_syst.orders:
                print(self.log_syst.track_order(order.order_id))
        else: 
            try:
                order_id = int(input('So you want to get specific order. \
Please, input the id of the order you want to track: '))
            except ValueError:
                print('Something went wrong. Please, try again.')
            print(self.log_syst.track_order(order_id))

    def quit(self):
        print("Thank you for using the logistic system today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

        
