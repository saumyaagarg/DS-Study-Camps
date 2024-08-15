# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. 

class Item:
    def __init__(self, name, price, quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Rs.{self.price:.2f} x {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        # Check if the item is already in the cart
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                print(f"Updated {name} quantity to {item.quantity}.")
                return
        # If the item is not in the cart, add it as a new item
        self.items.append(Item(name, price, quantity))
        print(f"Added {quantity} x {name} to the cart.")

    def remove_item(self, name, quantity=1):
        for item in self.items:
            if item.name == name:
                if item.quantity > quantity:
                    item.quantity -= quantity
                    print(f"Removed {quantity} x {name}. Remaining: {item.quantity}")
                elif item.quantity == quantity:
                    self.items.remove(item)
                    print(f"Removed {name} completely from the cart.")
                else:
                    print(f"Cannot remove {quantity} x {name}. Only {item.quantity} available.")
                return
        print(f"{name} not found in the cart.")

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def show_cart(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(item)
            print(f"Total Price: Rs.{self.calculate_total():.2f}")

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 15, 3)
cart.add_item("Banana", 10, 5)
cart.add_item("Orange", 20, 2)
cart.show_cart()
print()

cart.remove_item("Banana", 2)
cart.show_cart()
print()

cart.remove_item("Apple", 3)
cart.show_cart()