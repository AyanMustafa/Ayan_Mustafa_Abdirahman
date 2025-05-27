#exercise
#Submit your work on github for method overloading
#two real world examples of the above
from multipledispatch import dispatch

class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        z = a + b
        print(f"Adding two integers: {a} + {b} = {z}")

    @dispatch(float, float, float)
    def add(self, a, b, c):
        z = a + b + c
        print(f"Adding three floats: {a} + {b} + {c} = {z}")
        
    @dispatch(int, float)
    def add(self, a, b):
        z = a + b
        print(f"Adding an integer and a float: {a} + {b} = {z}")
        
# Example usage
calc = Calculator()
calc.add(5, 10)          # Adding two integers
calc.add(2.5, 3.5, 4.0)  # Adding three floats
calc.add(5, 2.5)        # Adding an integer and a float

