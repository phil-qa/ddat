# Title: CDP_ex11_ocp
# Purpose : To exercise refactoring to introduce Open closed principle
# Instructions : The code below generates a cost report for multiple energy
#               services based on thier unit cost, standing charge, and use.
#               Adding a new service such as fiber would either require
#               adding it into the EnergyServiceCostCalculator as an option
#               or refactoring the code to make it OCP compliant.
#               Review the code and using an abstract class to define an interface
#               to return a value can you add the fiber service that has a granular
#               calculation where there is a morning service rate and an afternoon
#               service rate

class EnergyService:
    def __init__(self, service_name, cost_per_unit, standing_charge, service_use):
        self.service_name = service_name
        self.cost_per_unit = cost_per_unit
        self.standing_charge = standing_charge
        self.service_use = service_use


class EnergyServiceCostCalculator:
    def calculate_monthly_cost(services):
        total = 0
        for service in services:
            total += (service.cost_per_unit * service.service_use) + service.standing_charge
        return total


hospital_electricity = EnergyService("electricity", 10, 252, 1300)
hospital_gas = EnergyService("gas", 3.5, 500, 14000)

all_services = [hospital_electricity, hospital_gas]

print(f"Cost of all services on a monthly basis £{EnergyServiceCostCalculator.calculate_monthly_cost(all_services)}")