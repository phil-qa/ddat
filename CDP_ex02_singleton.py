# Title: CDP_ex02_singleton
# Purpose : Create a singleton
# Instructions : Review the class below. Currently it does not implement the pattern for singleton, but by making the
#               innner class private and instancing it in the constructor and thereafter accessing it is through the
#               __getattr__() method that redirects it to the inner class, it cannot be directly accessed
#               .can you modify the code so that only one instance is created


class singleThing:
    class __singleThing:
        def __init__(self, thing_name):
            self.name = thing_name
        def __str__(self):
            return  repr(self) + self.name

    this_instance = None
    def __init__(self, name):
        if not singleThing.this_instance:
            singleThing.this_instance = singleThing.__singleThing(name)
        else:
            singleThing.this_instance.name = name
        def __getattr__(self, name):
            return getattr(self.this_instance, name)

cake_thing=singleThing("cake")
bike_thing=singleThing("bike")

print(cake_thing.this_instance)
print(bike_thing.this_instance)