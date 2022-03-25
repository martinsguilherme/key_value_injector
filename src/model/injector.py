import random

# defines the header injector
class Injector:

    # constructor
    def __init__(self):
        self.key = 1
        self.value = random.random()

    # sums 1 to key
    def set_key(self):
        self.key+=1

    # sums random number to value
    def set_value(self):
        self.value+=random.random()

    # return key
    def get_key(self):
        return self.key

    # return value
    def get_value(self):
        return self.value

    # return formatted key value (key:value)
    def get_key_value(self):
        self.set_key()
        self.set_value()
        key = self.get_key()
        value = self.get_value()
        return "" + str(key) + ":" + str(value)
