# Title: cmc_ex02_duplication
# Purpose : Exercise 2 isolating duplication
# Instructions : Perform a code review on the code below. Determine and correct any issues you see.
# Therm price is about 109.2 per therm as at 01.2023
import datetime

import gas_manager
from logos import gas_logo

gas_readings = []

print(gas_logo)

file_target = input("what is the reading file name? ")
units = input("Are the readings in m\u00B3 or ft\u00B3  (m/f) :")

with open(file_target) as tf:
    for entry in tf.readlines():
        gas_readings.append(entry)
        elements = entry.split(',')
        time_format = "%Y-%m-%d %H:%M:%S"
        gas_manager.add_reading(int(elements[0]),
                                datetime.datetime.strptime(elements[1], time_format), int(elements[2]))

cost_per_therm = float(input("What is the cost per therm "))

total_cost = 0
for reading in gas_readings:
    if units == "m":
        #convert to cubic feet
        cubic_feet_convert = int(reading.split(',')[0])*35.3146667
        cost = cubic_feet_convert * cost_per_therm
        total_cost+=cost
    else:
        cost = int(reading.split(',')[0])
        total_cost += cost

print(f"The total cost for the use is £{total_cost:.2f}")
