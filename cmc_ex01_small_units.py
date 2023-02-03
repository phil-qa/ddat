# Title: cmc_ex01_small_units
# Purpose : Exercise 1 write small units
# Instructions : do a  code review of the code below. What can be altered
#               Having done an initial refactor, show how your approach can extend the functionality by
#               extending this to take into account doors and windows (should not paint them
#               EXTENSION - can you extend this further to build out a quote for a house (multiple rooms)

# decorators calculator
import math

area_of_wall = int(input("How high is the wall ")) * int(input("How long is the wall "))

coverage_of_tin_of_paint = int(input("how much in square meters will a single tin cover"))

cost_of_tin = float(input("How much is a tin of paint £"))

total_number_of_tins = math.ceil(area_of_wall/coverage_of_tin_of_paint)

total_cost = total_number_of_tins *  cost_of_tin

print(f"The total cost of the paint is £{total_cost:.2f}")