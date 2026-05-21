import math 

#addition
def add(a,b):
    return a + b 

#subtraction
def subtract (a,b):
    return a - b 

#multiply
def multiply (a,b):
    return a * b 

#division
def divide (a,b):
    if b == 0:
        return "error: Division by zero"
    return a/b

#power
def power (a,b):
    return a ** b 

#square root
def square_root(a):
    return math.sqrt (a)
    