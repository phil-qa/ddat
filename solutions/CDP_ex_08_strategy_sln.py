# Title:CDP_ex08_strategy
# Purpose : Create an interface to implement the Electricity and Gas classes as a strategy
# Instructions : Currently there are two classes that support an implementation
#                cost for that energy type. It would make better sense if that
#                implementation were expressed as a strategy, allowing for greater
#                flexibility should other Types be introduced
#                Implement an Energy Interface and add use it with Electricity and Gas
#                Verify that they return solid values, can you add another class to
#                support wind with the same algorithm

import abc

class Energy(abc.ABC):
    '''
    Energy interface
    '''

    @abc.abstractmethod
    def implementation_cost(self, distance_from_source):
        pass


class Electricity(Energy):
    def __init__(self, local_cost):
        self._local_cost = local_cost

    def implementation_cost(self, distance_from_source):
        return self._local_cost * distance_from_source


class Gas(Energy):
    def __init__(self, local_cost):
        self._local_cost = local_cost

    def implementation_cost(self, distance_from_source):
        return (self._local_cost * distance_from_source)



class CostManager:
    def __init__(self, Energy):
        self._energy = Energy

    def cost_estimate(self, distance_from_source_node):
        return self._energy.implementation_cost(distance_from_source_node)



maresfield_gas_installation = Gas(120)
job_cost = CostManager(maresfield_gas_installation)

print(f'Cost for gas installation in Maresfield £{job_cost.cost_estimate(110)}')

