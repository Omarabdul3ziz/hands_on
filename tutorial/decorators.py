

def smart_div(func):
    """make our func smarter by apply some logic on it"""
    def inner_func(a,b):
        if b>a:
            a,b = b,a
        return func(a,b)
    return inner_func

@smart_div #or you can declare the connection before def the func
def div(a,b):
    """a simple function print the result of division to two numbers ONLY WORK WHILE a>b"""
    return (a/b)


#div = smart_div(div) #connect the smartness

#and ACTION!!!

print (div(2,4))

#IT WORKS !!!