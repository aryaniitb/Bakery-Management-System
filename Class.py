Products = []
import time
class Item:
    @classmethod
    def add_item(cls, name, price, stock):
        product = {
            "name": name,
            "Price": price,
            "Stock": stock
        }
        Products.append(product)

    @classmethod
    def display_products(cls):
        print("{:<20s}{:>10s}{:>10s}".format("Product Name", "Price", "Stock"))
        print("-" * 50)
        for product in Products:
            print("{:<20s}{:>10.2f}{:>10d}".format(product.get("name"), product.get("Price"), product.get("Stock")))
        print("-" * 50)

class Customer:
    def __init__(self, naam):
        self.naam = naam
        self.your_order = {}
        print(f"Welcome to the Brijrvl Bakery, {self.naam}")

    def place_your_order(self):
        while True:
            Item.display_products()
            name = input("Enter the name of the product you want to order (or 'quit' to stop the process): ").lower()
            if name == "quit":
                break
            found = False
            for product in Products:
                if product.get("name").lower() == name:
                    quantity = int(input("Enter the quantity you want to order: "))
                    if quantity <= 0:
                        print("Invalid quantity. Please enter a positive integer.")
                        continue
                    if product.get("Stock") >= quantity:
                        confirm = input(f"Confirm order of {quantity} {name}(s) (yes/no): ").lower()
                        if confirm != 'yes':
                            print("Order not confirmed.")
                            continue
                        if name in self.your_order:
                            self.your_order[name] += quantity
                        else:
                            self.your_order[name] = quantity
                        product['Stock'] -= quantity
                        print("Order placed successfully!")
                    else:
                        print("Insufficient stock. Please order less.")
                        continue
                    found = True
                    break
            if not found:
                print("Product not found.")
                continue
            print("-" * 50)
            print(f"Current order: {self.your_order}")
            print("-" * 50)

class OrderSummary:
    def __init__(self, your_order):
        self.your_order = your_order

    def display_order_summary(self):
        print("Order Summary:")
        print("-" * 50)
        for product, quantity in self.your_order.items():
            print("{:<20s}{:>10d}".format(product, quantity))
        print("-" * 50)

class Bill:
    def __init__(self, your_order):
        self.your_order = your_order

    def display_bill(self):
        total = 0
        print("-" * 50)
        print("Order Summary:")
        print("-" * 50)
        print("{:<20s}{:>10s}{:>10s}".format("Name", "Quantity", "Price"))
        print("-" * 50)
        for product_name, quantity in self.your_order.items():
            for product in Products:
                if product['name'].lower() == product_name.lower():
                    item_price = product['Price']
                    total += item_price * quantity
                    print("{:<20s}{:>10d}{:>10.2f}".format(product_name, quantity, item_price))
        print("-" * 50)
        print("{:<20s}{:>20.2f}".format("Total", total))
        print("-" * 50)


def main():
    
    Item.add_item("Bread", 5, 20)
    Item.add_item("Cupcakes", 10, 10)
    Item.add_item("Cookies", 5, 25)
    Item.add_item("Cakes", 50, 8)
    Item.add_item("Toast", 2, 20)

    name = input("Enter your name: ")
    customer2 = Customer(name)
    time.sleep(2)
    customer2.place_your_order()
    order_summary = OrderSummary(customer2.your_order)
    time.sleep(2)
    order_summary.display_order_summary()
    bill = Bill(customer2.your_order)
    time.sleep(2)
    bill.display_bill()


if __name__ == "__main__":
    main()
