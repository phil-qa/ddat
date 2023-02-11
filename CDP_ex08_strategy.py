# Title:CDP_ex08_strategy
# Purpose : Create an interface to implement the Electricity and Gas classes as a strategy
# Instructions : Currently there are two classes that support an implementation
#                cost for that energy type. It would make better sense if that
#                implementation were expressed as a strategy, allowing for greater
#                flexibility should other Types be introduced
#                Implement an Energy Interface and add use it with Electricity and Gas
#                Verify that they return solid values, can you add another class to
#                support wind with the same algorithm, extend the functionality to
#                a CostManager class that  will give the result of the estimation

import abc

class Energy(abc.ABC):
    '''
    Energy interface
    '''
    #TODO implement an interface to support the functionality
    pass


class Electricity:
    def __init__(self, local_cost):
        self._local_cost = local_cost

    def implementation_cost(self, distance_from_source):
        return self._local_cost * distance_from_source


class Gas:
    def __init__(self, local_cost):
        self._local_cost = local_cost

    def implementation_cost(self, distance_from_source):
        return (self._local_cost * distance_from_source)



class CostManager:
    def __init__(self, Energy):
        self._energy = Energy

    #TODO implement cost_estimate


'''Example of calling the functionality
maresfield_gas_installation = Gas(120)
job_cost = CostManager(maresfield_gas_installation)

print(f'Cost for gas installation in Maresfield £{job_cost.cost_estimate(110)}')

'''


