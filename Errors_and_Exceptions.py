#Syntax Errors: When there is a syntax error, the program will not execute even if that part of code is not used.

if True print("Hello") # SyntaxError: invalid syntax




#Exceptions: Division Example  Input given by the user is not within expected values.

def divide(a, b):  
    return  a / b        

divide(5, 0)        # Output is: ZeroDivisionError: division by zero








#Raising Exceptions:

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

print(divide(10, 0))  # ValueError: Cannot divide by zero






#Handling Exceptions: Exceptions can be handled with try-except block. 
def divide(x, y):
    try:
        result = x / y
    except TypeError:
        return "Invalid input"
    return result
print(divide(10, 5)) # 2.0
print(divide(10, "a"))  # Invalid input






#Handling Specific Exceptions
try:  
    result = 5/0
    print(result)  
except ZeroDivisionError:  
    print("Denominator can't be 0")  
except:  
    print("Unhandled Exception")
  
# Output is: Denominator can't be 0








#Handling Multiple Exceptions:

try:  
    result = 12/"a"
    print(result)  
except ZeroDivisionError:  
    print("Denominator can't be 0")  
except ValueError:  
    print("Input should be an integer")  
except:  
    print("Something went wrong")
  
# Output is: Denominator can't be 0
