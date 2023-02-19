# Title: CDP_ex14_dip
# Purpose : To refactor code so that it meets dependency inverson principle
# Instructions : Review the code below that transforms a voltage supply and
#                ensure that the code meets dependency inversion principle



class ElectricitySupply:
    def __init__(self, voltage):
        self.base_voltage = voltage

class Transformer:
    def __init__(self, ratio, ElectricitySupply):
        self.ratio = ratio
        self.electricity_supply = ElectricitySupply

    def transform(self)->int:
        return self.electricity_supply.base_voltage / self.ratio

class MatchedSupply:
    def __init__(self, ratio):
        self.supply_voltage = None
        self.ratio = ratio

    def match(self, electricity_supply: ElectricitySupply):
        transformer = Transformer(self.ratio, electricity_supply)
        self.supply_voltage = transformer.transform()


def main():
    supply_voltage = ElectricitySupply(240)
    matched_supply = MatchedSupply(2)
    matched_supply.match(supply_voltage)
    print(matched_supply.supply_voltage == supply_voltage.base_voltage/2)


if __name__ == '__main__':
    main()
