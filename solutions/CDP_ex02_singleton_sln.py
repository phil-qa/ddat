# Title: CDP_ex02_singleton
# Purpose : Understand the implementation of singleton
# Instructions : Review the class below. Currently it does not implement the pattern for singleton, but by making the
#               inner class private and instancing it in the constructor and thereafter accessing it is through the
#               __getattr__() method that redirects it to the inner class, it cannot be directly accessed
#               .Can you implement singleton and as an extension modify the code so that only one instance is created


class SuperSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls]=instance
        return cls._instances[cls]


class SingleThing(metaclass=SuperSingleton):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        return getattr(self.this_instance, name)

cake_thing=SingleThing("cake")
print(cake_thing.name)
bike_thing=SingleThing("bike")
print(id(cake_thing) == id(bike_thing))



print(bike_thing.name)