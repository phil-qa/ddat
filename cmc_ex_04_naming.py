# Title:cmc_ex_04_naming
# Purpose : TO review the naming approaches
# Instructions : Review the code below and determine what
# (if anything) could be improved
import datetime
import math

yyyymmddasstring = str(datetime.datetime.now().date())

user_accounts_list = []

class CustomerProfilePersonalInformationManagementSystem:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Helper:
    def multiply_list(self, list):
        return math.prod(list)

    def sum_list(self, list):
        return sum(list)

class controller:
    def __init__(self, name, make, max, stopping):
        self.name = name
        self.make = make
        self.max = max
        self.stopping = stopping
        self.speed = 0

    def accelerate(self, rate, time):
        self.speed += rate * time

    def brake(self, time):
        self.speed -= self.stopping*time
        if self.speed <0:
            self.speed = 0