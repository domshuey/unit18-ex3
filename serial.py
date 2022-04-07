"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        '''initialize start num'''
        self.start = start
        # this is will increase by 1 after every time .generate() is called
        self.counter = 0
        

    def generate(self):
        '''add 1 and print generated num'''
        print(self.start + self.counter)
        self.counter += 1
        return
    
    def reset(self):
        '''reset counter to initial start value'''
        self.counter = 0

    

    