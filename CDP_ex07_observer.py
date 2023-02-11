# Title:CDP_ex07_observer
# Purpose : To implement the observer pattern so that many clients can attach
# Instructions : An Energy meter is represented by an EnergyMeter class, the class
#                  and supporting code has partially started to implement the
#                  observer pattern. Review the code and implement the pattern
#                  so that you can attach a client called local_server that will
#                  recieve a notification that an instance of EnergyMeter has had
#                  an update to its usage

import abc

class EnergyMeter:
    def __init__(self, identity, start_value):
        self._identity = identity
        self._use = start_value
        # TODO implement observer pattern
        # self._observers = set()

    def attach(self, observer):
        #TODO implement attach
        pass

    def detach(self, observer):
        #TODO implement detach
        pass

    def _notify(self):
        #TODO imlement notify
        pass


    @property
    def current_recorded_use(self):
        return self._use

    @current_recorded_use.setter
    def update_new_reading(self, value):
        self._use += value



class Observer(metaclass=abc.ABCMeta):
    def __init__(self):

        self._energy_meter = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, value):
        pass


class ConcreteObserver(Observer):
    #TODO implement concrete observer, should implement the Observer
    def __init__(self):
        pass


#code to observe the pattern working
energy_meter = EnergyMeter('1xxidi1', 0)
local_server = ConcreteObserver()
energy_meter.attach(local_server)
energy_meter.update_new_reading = 100
print(local_server.get_state()==100)
energy_meter.update_new_reading = 10
print(local_server.get_state()==110)


