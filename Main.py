
import time
your_order = {}

def display_products(Products):
    
        print("-" * 50)
        print("Available Bakery Items:")
        print("-" * 50)
        
        print("{:<20s}{:>10s}{:>10s}".format("Name", "Price", "Stock"))
        print("-" * 50)
        for i in range(len(Products)):
          
          print("{:<20s}{:>10.2f}{:>10d}".format(Products[i].get("name"), Products[i].get("Price"), Products[i].get("Stock"))) #Capital S in 'Stock'
        print("-" * 50)

def place_your_order(products):
    while True:
        display_products(products)
        name = input("Enter the name of the product you want to order (or 'quit' to stop the process): ").lower()
        if name == "quit":
            break
        found = False
        for i in range(len(products)):
            product = products[i]
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
                    if name in your_order:
                        your_order[name] += quantity
                    else:
                        your_order[name] = quantity
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
        display_order_summary(your_order)
        print("-" * 50)

def order_now(products):
    wait = 0
    while True:
        display_products(products)
        name = input("Enter the name of the product you want to order (or 'quit' to stop the process): ").lower()
        if name == "quit":
            break
        found = False
        for i in range(len(products)):
            product = products[i]
            if product.get("name").lower() == name:
                quantity = int(input("Enter the quantity you want to order: "))
                wait += product.get("time")*quantity
                print(f"you have to wait for {wait} seconds")
                confirm = input(f"Confirm order of {quantity} {name}(s) (yes/no): ").lower()
                if confirm != 'yes':
                    print("Order not confirmed.")
                    continue
                if name in your_order:
                    your_order[name] += quantity
                else:
                    your_order[name] = quantity
                found = True
    print("-" * 50)
    display_order_summary(your_order)
    print(f"please wait for around {wait}")
    print("-" * 50)
        
    return wait
def display_order_summary(order):
    print("Order Summary:")
    print("-" * 50)
    for product, quantity in order.items():
        print("{:<20s}{:>10d}".format(product, quantity))
    print("-" * 50)

def bill(your_order, products):
    total = 0
    print("-" * 50)
    print("Order Summary:")
    print("-" * 50)
    print("{:<20s}{:>10s}{:>10s}".format("Name", "Quantity", "Price"))
    print("-" * 50)
    for product_name, quantity in your_order.items():
        for product in products:
            if product['name'].lower() == product_name.lower():
                item_price = product['Price']
                total += item_price * quantity
                print("{:<20s}{:>10d}{:>10.2f}".format(product_name, quantity, item_price))

    print("-" * 50)
    print("{:<20s}{:>20.2f}".format("Total", total))
    print("-" * 50)

def main():
    user_name = input("Enter your name: ")
    Products = [{'name': 'Toast', 'Price': 2, 'Stock': 0,'time': 20},
    {'name': 'cupcakes', 'Price': 10, 'Stock': 0, 'time': 30},
    {'name': 'Cookies', 'Price': 5, 'Stock': 0, 'time': 10},
    {'name': 'Cakes', 'Price': 50, 'Stock': 0, 'time': 25},
    {'name': 'Bread', 'Price': 5, 'Stock': 0,'time': 10}]
    print(f"Welcome to the Brijrvl bakery, {user_name}")
    time.sleep(2)
    print("please order!")
    time.sleep(1)
    wait = order_now(Products)
    time.sleep(wait)
    print(f"Thank you {user_name}, Here is you bill")
    bill(your_order,Products)



if __name__ == "__main__":
    main()



