class SmartGrocery:
    def __init__(self):
        self.items = {}
        self.item_name = item_name = ""
        self.quantity = quantity = 0

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
                return True
            else:
                return False
        else:
            return False

    def check_item(self, item_name):
        return self.items.get(item_name, 0)

    def display_contents(self):
        print("Current groceries in stock: ")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")


groceries = SmartGrocery()

while True:
    print("\nSmart Grocery menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check item quantity")
    print("4. Display contents")
    print("5. Exit")

    selection = input("Enter your choice: ")

    if selection == "1":
        item_name = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        groceries.add_item(item_name, quantity)
        print(f"{item_name} has bee added to refrigerator/pantry.")
        
    elif selection == "2":
        item_name = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        if groceries.remove_item(item_name, quantity):
            print(f"{quantity} of {item_name} has been removed from refrigerator/pantry.")
        else:
            print(f"Not enough {item_name} to remove.")
            
    elif selection == "3":
        input("Enter item: ")
        quantity = groceries.check_item(item_name)
        print(f"The current amount of {item_name} is {quantity}.")

    elif selection == "4":
        groceries.display_contents()

    elif selection == "5":
        print("Exiting the Smart Grocery menu. See you soon!")
        break

    else:
        print("Invalid selection. Please choose valid option.")






