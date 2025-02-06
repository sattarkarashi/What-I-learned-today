import sys
print(sys.path)
class Calculator:
    def add(self, x: float, y: float) -> float:
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y