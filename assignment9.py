class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.a / self.b
    
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

