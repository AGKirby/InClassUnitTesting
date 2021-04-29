def addition(a, b):
    try: #check input types
        num1 = int(a)
        num2 = int(b)
    except:
        return None
    return num1 + num2

def subtraction(a, b):
    try: #check input types
        num1 = int(a)
        num2 = int(b)
    except:
        return None
    return num1 - num2

def multiplication(a, b):
    try: #check input types
        num1 = int(a)
        num2 = int(b)
    except:
        return None
    return num1 * num2

def division(a, b):
    try: #check input types
        num1 = int(a)
        num2 = int(b)
    except:
        return None
    if(b == 0): #divide by zero
        return None
    return num1 / num2