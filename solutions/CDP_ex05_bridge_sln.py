# Title: CDP_ex05_bridge.py
# Purpose : To implement a bridge pattern
# Instructions : Providers of energy provide dual fuel, gas and electricity
#                 This can be provided for different markets, Commercial and Government
#               Using a bridge pattern solves a problem of writing classes for each possible scenario
#               The code below has two clients, Government and Commercial, for both gas and electricity,
#               The provider is acting as a bridge.
#               1. can you implement the Government class and test it with a
#               new provider Eorn which has the contract for supplying both gas and electriicity to Government
#               2. can you implement a new service 'wind' at units Kwh and add it to Eorns contract for the government

class EnergyClient:
    def government_client(self, items):
        pass

    def commercial_client(self, items):
        pass


class Electricity(EnergyClient):
    def government_client(self, volume):
        print(f"The government service monthly Kwh {volume} ")

    def commercial_client(self, volume):
        print(f"The commercial service monthly Kwh  {volume} ")


class Gas(EnergyClient):
    def government_client(self, volume):
        print(f"The government service monthly volume {volume} M\u00B3 ")

    def commercial_client(self, volume):
        print(f"The commercial service monthly volume {volume} M\u00B3  ")


class Provider:
    def __init__(self, EnergyClient):
        self.energy_carrier = EnergyClient

    def display_description(self):
        pass

    def add_usage(self):
        pass


class Commercial(Provider):
    def __init__(self, EnergyClient, use):
        super().__init__(EnergyClient)
        self.use = use

    def display_description(self):
        self.energy_carrier.commercial_client(self.use)

    def add_usage(self, new_use):
        self.use += new_use


class Government(Provider):
    def __init__(self, EnergyCarrier, use):
        super().__init__(EnergyCarrier)
        self.use = use

    def display_description(self):
        self.energy_carrier.government_client(self.use)

    def add_usage(self, new_use):
        self.use += new_use


commercial_gas = Gas()

edf_commercial = Commercial(commercial_gas, 1000)
edf_commercial.display_description()
edf_commercial.add_usage(100)
edf_commercial.display_description()

