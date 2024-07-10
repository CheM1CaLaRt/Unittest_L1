def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def modulo(a, b):
   if b == 0:
      return Raise(ZeroDivisionError, 'division by zero')
   return a % b
