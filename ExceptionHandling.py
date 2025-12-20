try:
    age = int(input("Enter Your Age: "))
except ValueError:
    print(ValueError)
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print(f"Your Age is {age}")

def sumTwoNumber():
    try:
        num1 = int(input("Enter The First Number: "))
        num2 = int(input("Enter The Second Number: "))
        result = num1 / num2
        print(result)
    except (ValueError,ZeroDivisionError) as error:
        print(error) 
    finally:
        print("Process completed")

sumTwoNumber()   
