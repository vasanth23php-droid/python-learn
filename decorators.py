def FirstDecorators(fun):
    def wrap_func(x, y):
        print(x * y)
        fun(x ,y)
        print(x - y)
    return wrap_func

@FirstDecorators
def sayHello(x, y):
    print(x+y)

sayHello(6,16)    
