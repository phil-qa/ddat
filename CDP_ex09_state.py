# Title: CDP_ex09_state
# Purpose : Create a pattern to switch classes on a state change
# Instructions : Below is code that switches an energy source based on
#               what is initially requested and then on subsequent change requests
#               express this in a strategy pattern that responds to being initialised
#               then changing as required



class GasState:
    def report(self):
        print("Switch request for Gas")

class ElectricityState:
    def report(self):
        print ("Switch request for Electricity")


class SupplySwitcher:
    #TODO implement a class to initialise off a supply type and switch
    #TODO implement a switch
    #TODO implement a method for reporting class change
    def __init__(self):
        pass


