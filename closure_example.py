def transmit_to_space(message):
    """This is the enclosing function"""
    print(message)
    def data_transmitter():
        """The nested function"""
        nonlocal message
        message = None
        print(message)
        message = 'hello wold'
        print(message)
    data_transmitter()
    print(message)

transmit_to_space("Test message")
# data_transmitter() can't call in outside scope
