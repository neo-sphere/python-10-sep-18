# simple function
# def greet():
#     pass # do nothing

# def greet():
#     print('Hello world!') #statement

# function with argument
# def greet(name):
#     print('Hello {}!'.format(name))

# function with default argument
# def greet(name='santosh'):
#     print('Hello {}!'.format(name))
#
# greet()
# greet('aryan')


# def add(x, y):return x+y
# print(add(4,5))

# x is required positional argument
# y is optional positional argument
# def add_one(x, y=1): return x+y
# print(add_one(5))
# print(add_one(7))
# print(add_one(3, 7))

# def add(x=0, y=0): print(x,y);return(x+y)
# print(add())
# print(add(3))
# print(add(4, 7))
# print(add(y=4, x=7))
# print(add(5, y=6))
print(__name__)

def hello(name, age):
    print('hey {}'.format(name))

if __name__ == "__main__":
    hello('santosh', 44)
