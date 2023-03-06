# Title: cmc_ex01_small_units
# Purpose : Exercise 1 write small units
# Instructions : do a  code review of the code below. What can be altered
#               Having done an initial refactor, show how your approach can extend the functionality by
#               extending this to take into account doors and windows (should not paint them
#               EXTENSION - can you extend this further to build out a quote for a house (multiple rooms)

# decorators calculator
import math


def area(first_dimension, second_dimension):
    '''
    a function that takes two numeric parameters and multipies them to return an area
    :param first_dimension: int
    :param second_dimension: int
    :return: int
    '''
    return first_dimension * second_dimension


def get_spatial_object(name):
    '''
    a function that asks for and returns the dimensions of a named object
    :param name: string, name of the object
    :return: dictionary of dimensions
    '''
    dimensions = {}
    dimensions['height'] = int(input(f"How high is the {name}"))
    dimensions['width'] = int(input(f"how wide is the {name}"))
    return dimensions


def get_null_space_area():
    number_of_null_space_objects = int(input("How many doors and windows :"))
    null_space_objects = []
    for ob in range(number_of_null_space_objects):
        dimensions = get_spatial_object('window/door')
        null_space_objects.append(area(dimensions['height'], dimensions['width']))
    total_area = sum(null_space_objects)
    return total_area


class PaintParameters:
    '''
    class to hold parameters associated with the current properties of pain
    '''

    def __init__(self):
        self.coverage = 0
        self.cost = 0
        self.update()

    def update(self):
        self.coverage = float(input('What is the coverage for a tin of paint :'))
        self.cost = float(input("What is the cost of a tin £"))


class WorkAreaParameters:
    '''
    class for holding the work surface parameters    :return: dictionary of parameters
    '''

    def __init__(self):
        self.wall_area = 0
        self.null_space_area = 0
        self.update()

    def update(self):
        wall_dims = get_spatial_object('wall')
        self.wall_area = area(wall_dims['height'], wall_dims['width'])
        self.null_space_area = get_null_space_area()

def number_of_tins(wallspace_parameters, paint_parameters):
    '''
    function to determine the number of tins that would cover a given area
    :param wallspace_parameters: instance of WorkAreaParameters
    :return: number of tins
    '''
    area_to_cover = wallspace_parameters.wall_area - wallspace_parameters.null_space_area
    tins = math.ceil(area_to_cover / paint_parameters.coverage)
    return tins


def cost(work_area_parameters, paint_parameters):
    '''
    function to return the cost of the number of tins based on the job parameters
    :param job_parameters: dictionary of job parameters
    :return: cost
    '''
    return number_of_tins(work_area_parameters, paint_parameters) * paint_parameters.cost


def main():
    while True:
        print("Decorators calculator ")
        response = input("Yould you like a quote (y/n)?")
        if response.lower() == 'y':
            work_area = WorkAreaParameters()
            paint_parameters = PaintParameters()
            job_cost = cost(work_area,paint_parameters)
            print(f"The total cost of the paint is £{job_cost:.2f}")
        elif response.lower() == 'n':
            break
        else:
            print("UNKNOWN RESPONSE")


if __name__ == '__main__':
    main()
