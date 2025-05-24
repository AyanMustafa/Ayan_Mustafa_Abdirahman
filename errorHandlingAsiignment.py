#write a program to handle errors, the programm should ask for two number using input and then divides them. use an infinite loop to keep asking until a valid input is provided.
try:
    while True:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  
except ValueError:
    print("Invalid input! Please enter valid numbers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed. Please enter a non-zero denominator.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division completed successfully.")
finally:
    print("Thank you for testing the program.")
    
    
    