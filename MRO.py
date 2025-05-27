#method resolution order (MRO)
# A shopping cart system where you can add items of different types (e.g., books, electronics)
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart.")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class Electronics:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"Electronics: {self.name} by {self.brand}"
class BookCart(ShoppingCart):
    def add_item(self, book):
        if isinstance(book, Book):# Checking if the item is a Book instance
            super().add_item(book)
        else:
            print("Only books can be added to the book cart.")
class ElectronicsCart(ShoppingCart):
    def add_item(self, electronics):
        if isinstance(electronics, Electronics):
            super().add_item(electronics)
        else:
            print("Only electronics can be added to the electronics cart.")
# Example usage
book_cart = BookCart()
book_cart.add_item(Book("1984", "George Orwell"))
book_cart.add_item(Electronics("Smartphone", "BrandX"))  # Should print an error message
electronics_cart = ElectronicsCart()
electronics_cart.add_item(Electronics("Laptop", "BrandY"))
    
    
    
    
    