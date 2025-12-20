try:
    age = int(input("Enter Your Age: "))
    if age < 18:
        raise ZeroDivisionError('Your not adult')
except (ValueError,ZeroDivisionError) as error:
    print(error)
finally:
    print(f"Finally done your age is {age}")
