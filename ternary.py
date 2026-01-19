try:
    age = int(input('Enter your age: '))
except ValueError:
    print(ValueError)
else:
    pass_allowed = 'Allowed' if age > 18  else 'Not allowed'
    print(pass_allowed)
finally:
    print('The process completed')