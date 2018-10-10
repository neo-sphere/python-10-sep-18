a = None
def greet(*args):
    # global a = args[:] # invalid syntax
    # global a
    nonlocal a
    a = args[:]
    # print(args)

greet('hello')
print(a)
