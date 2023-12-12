import pyfiglet

def print_figlet_with_border(text):
    figlet_text = pyfiglet.figlet_format(text)
    border = '*' * (len(figlet_text.split('\n')[0]) + 4)

    print(border)
    for line in figlet_text.split('\n'):
        print(f'* {line} *')
    print(border)

# Example usage:
text_to_print = "Vending Mechine"
print_figlet_with_border(text_to_print)

import pandas as pd

categories = {
    "Chocolates": {
        "Kitkat bar": {"code": "A", "price": 1.95, "stock": 5},
        "M&M's": {"code": "B", "price": 4.25, "stock": 2},
        "Reese's Peanut Butter Cups": {"code": "C", "price": 5.8, "stock": 4},
    },
    "Soft drinks": {
        "Coca Cola": {"code": "D", "price": 2.5, "stock": 9},
        "Dr. Pepper": {"code": "E", "price": 7.5, "stock": 4},
        "Fanta": {"code": "F", "price": 3.75, "stock": 5},
    },
    "Snacks": {
       "Chips": {"code": "G", "price": 1.99, "stock": 10},
       "Pretzels": {"code": "H", "price": 3.25, "stock": 6},
       "Popcorn": {"code": "I", "price": 4.0, "stock": 7},
    }
}

from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define the column names
table.field_names = ["Product", "Code", "Price", "Stock"]

# Add rows to the table for the "Chocolates" category
chocolates_data = {
    "Kitkat bar": {"code": "A", "price": 1.95, "stock": 5},
    "M&M's": {"code": "B", "price": 4.25, "stock": 2},
    "Reese's Peanut Butter Cups": {"code": "C", "price": 5.8, "stock": 4},
}

for product, details in chocolates_data.items():
    table.add_row([product, details["code"], details["price"], details["stock"]])

# Print the table
print("chocolates")
print(table)

from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define the column names
table.field_names = ["Product", "Code", "Price", "Stock"]

# Add rows to the table
table.add_row(["Coca Cola", "D", 2.5, 9])
table.add_row(["Dr. Pepper", "E", 7.5, 4])
table.add_row(["Fanta", "F", 3.75, 5])

# Print the table
print("Soft drinks")
print(table)

from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define the column names
table.field_names = ["Product", "Code", "Price", "Stock"]

# Add rows to the table for the "Snacks" category
snacks_data = {
    "Chips": {"code": "G", "price": 1.99, "stock": 10},
    "Pretzels": {"code": "H", "price": 3.25, "stock": 6},
    "Popcorn": {"code": "I", "price": 4.0, "stock": 7},
}

for product, details in snacks_data.items():
    table.add_row([product, details["code"], details["price"], details["stock"]])

# Print the table
print("Snacks")
print(table)

def print_categories():
        for category, items in categories.items():
            (f"\nCategory: {category}")
        for item, details in items.items():
            (f"Item Name: {item} | Code: {details['code']} | Price: ${details['price']} | Stock: {details['stock']}")

def display_items():
    print("\nAvailable items:")
    print_categories()

class VendingMachine:
    def __init__(self, categories):
        self.categories = categories
        self.balance = 0.0

    def print_categories(self):
        for category, items in self.categories.items():
            (f"\nCategory: {category}")
            for item, details in items.items():
                (f"Item Name: {item} | Code: {details['code']} | Price: ${details['price']} | Stock: {details['stock']}")

    def accept_money(self):
        while True:
            try:
                money = float(input("Insert money (enter 0 to cancel): $"))
                if money == 0:
                    print("Transaction canceled. Returning money.")
                    return 0
                elif money < 0:
                    print("Invalid amount. Please enter a positive amount.")
                else:
                    return money
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def select_item(self):
        while True:
            selection = input("Enter the code of the item you want to purchase: ").upper()
            for category, items in self.categories.items():
                if selection in [details['code'] for details in items.values()]:
                    return selection
            print("Invalid selection. Please choose a valid item code.")

    def process_transaction(self, item_code, money):
        for category, items in self.categories.items():
            for item, details in items.items():
                if item_code == details['code']:
                    if details['stock'] > 0:
                        if money >= details['price']:
                            change = money - details['price']
                            print(f"Dispensing {item} from category {category}.\nYour change: ${change:.2f}")
                            details['stock'] -= 1
                            self.balance += details['price']
                            return True
                        else:
                            print(f"Insufficient funds. Please insert more money.")
                            return False
                    else:
                        print(f"Sorry, {item} is out of stock. Please choose another item.")
                        return False


    def run(self):
        while True:
            self.print_categories()
            item_code = self.select_item()
            if item_code == '0':
                break
            money = self.accept_money()
            if money == 0:
                continue
            if self.process_transaction(item_code, money):
                while True:
                    buy_more = input("Do you want to buy more items? (yes/no): ").lower()
                    if buy_more == 'yes':
                        break
                    elif buy_more == 'no':
                        print("Thank you for using our vending machine. Have a great day!")
                        return False
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    vending_machine = VendingMachine(categories)
    vending_machine.run()



