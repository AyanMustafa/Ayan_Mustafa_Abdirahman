#Assignment 1: find the factorial of the number 5(five), 5!
for i in range(1, 6):
    if i == 1:
        factorial = 1
    else:
        factorial *= i
print(f"The factorial of 5 is: {factorial}")