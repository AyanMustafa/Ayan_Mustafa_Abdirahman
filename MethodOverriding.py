# Method Overriding Exercise
# A banking application where you can deposit money using different methods
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        
class SavingsAccount(BankAccount):
    # Overriding the deposit method to add interest
    def deposit(self, amount):
        
        interest = amount * 0.02  
        total_amount = amount + interest
        self.balance += total_amount
        print(f"Deposited {amount} with interest {interest}. New balance: {self.balance}")
        
class CheckingAccount(BankAccount):
    
    # Overriding the deposit method to add a fixed fee
    def deposit(self, amount):
        
        fee = 1.00  ##this amount is removed from the deposit
        if amount < fee:
            print("Deposit amount must be greater than the fee.")
            return
        total_amount = amount - fee
        self.balance += total_amount
        print(f"Deposited {amount} with a fee of {fee}. New balance: {self.balance}")


savings = SavingsAccount(100)
savings.deposit(50) 
checking = CheckingAccount(200)
checking.deposit(50)  


