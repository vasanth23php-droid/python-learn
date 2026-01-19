def callfunction(*args):
    print(*args)
    return sum(args)
print(callfunction(1,2,3,4,5,6))
def callmember(**kargs):
    return f"your send the following arguments {kargs}"
print(callmember(name='vasanthakumar',age=41))
print(callmember(name='vasanthakumar',birth='vaganagar',native='Thiruthurai Poondai',college='Thanjavur',work='Chennai'))
print(callmember(name='vasanthakumar',marrage_status='Single'))
    