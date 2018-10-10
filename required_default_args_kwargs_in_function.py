#  Variable length positional argument
def pos_info(*args):
    print(args)
    print(type(args)) # type -> tuple

# Variable length Keyword argument
def key_info(**kwargs):
    print(kwargs)
    print(type(kwargs)) # type -> dict

def pos_key_info(*args, **kwargs):
    print("args : ", args)
    print("kwargs : ", kwargs)

def info(name, *args, age=44 ,**kwargs):
    # name -> required positional argument
    # age -> default positional argument
    # args -> Variable length positional argument
    # kwargs -> Variable length Keyword argument
    print("Name: {} and age :{}".format(name, age))
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

if __name__ == "__main__":
    # pos_info() # can be called with no argument
    # pos_info('santosh', 33, 'ktm', 'Logpoint')
    # key_info(name='santosh', age=27, address='ktm', company='Logpoint')
    # pos_key_info('santosh', age=27, address='ktm', company='Logpoint')
    # info('santosh')
    # info('santosh', 21)
    # info('santosh', age=45)
    # info(name='santosh', age=33)
    # info(age=31, name='ram')
    # info('santosh', 'purbey', 'ktm', 'Logpoint', salary=45000, address="Dhapakhel")
    # info('santosh', 44, 'ktm', 'Logpoint', salary=45000, address="Dhapakhel") # got multiple value for age
    # info('santosh', 'purbey', 'ktm', 'Logpoint',age=33, salary=45000, address="Dhapakhel")
    # info('santosh', 'purbey', 'ktm', 'Logpoint', salary=45000, address="Dhapakhel", age=33)
    # info('santosh', 33)
    # info('santosh', age=33)
    # info('santosh', age=21, company='Logpoint')
    # info('santosh', 'purbey',age=21, company='Logpoint')
