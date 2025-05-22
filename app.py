#create and inventory management - Use loops to display or update a list of stock items
products = [
    {"name": "rice", "quantity": 10, "price": 399.99},{"name":"beans", "quantity": 20, "price": 199.99},
    {"name": "sugar", "quantity": 15, "price": 299.99},{"name":"salt", "quantity": 25, "price": 99.99},]

def display_products():
    print("Current Inventory:")
    print("Name\tQuantity\tPrice")
    for product in products:
        print(f"{product['name']}\t{product['quantity']}\t\t{product['price']}")
        
def update_product(name, quantity):
    for product in products:
        if product["name"] == name:
            product["quantity"] += quantity
            print(f"Updated {name} quantity to {product['quantity']}")
            return
    print(f"Product {name} not found in inventory.")
    
def make_order(name,quantity):
    for product in products:
        if product["name"] == name:
            if product["quantity"] >= quantity:
                product["quantity"] -= quantity
                print(f"Order placed for {quantity} of {name}. Remaining stock: {product['quantity']}")
                return
            else:
                print(f"Not enough stock for {name}. Available: {product['quantity']}")
                return
    print(f"Product {name} not found in inventory.")
    
def main():
    while True:
        print("\nInventory Management")
        print("1. Update Product Quantity")
        print("2. Make Order")
        print("3. Exit")
        choice = input("Enter your choice: ")
            
        if choice == "1":
            display_products()
            print("Available products for update:")
            name = input("Enter product name to update: ")
            quantity = int(input("Enter quantity to add: "))
            update_product(name, quantity)
        elif choice == "2":
            display_products()
            print("Available products for order:")
            name = input("Enter product name to order: ")
            quantity = int(input("Enter quantity to order: "))
            make_order(name, quantity)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    