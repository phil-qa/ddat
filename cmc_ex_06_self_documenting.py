# Title: cmc_ex_06_self_documenting
# Purpose : To review the processes involved with self documenting code
# Instructions : The following code is from cmc_ex_04. Review the naming and add appropriate
#                commentrary using comments and doctrings. If cmc_ex_04 was modified you may use it here
import math
from datetime import datetime

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