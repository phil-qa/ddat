# Title: CDP_ex04_adapter
# Purpose : To take on new functionality that is not compatible through the use of an adapter pattern
# Instructions : The code presented currently takes only electricity readings in KWh
#               Implement an adapter pattern to allow gas readings to be added converting from
#               m3(cubic meters) to Kwh. The calculation for such a conversion:
#               <volume>M3 * <calorific value>default 40 * 1.02226 / 3.6

class EnergyReading:
    """
    An EnergyReading is a Kwh value from a given source
    """

    def request(self, reading) -> str:
        '''
        returns a formatted reading in KWh
        :param reading: float reading value
        :return: formatted string with reading in KWh
        '''
        return f"Reading {reading:.2f} KWh"


class GasReading:
    """
    GasReading operates in the M^3 domain
    """

    def gas_request(self, reading) -> str:
        '''
        takes a reading and returns the formatted value in a string
        :param reading: float value of reaing
        :return: string with formatted message
        '''
        return f"Reading {reading:.2f} M\u00b3"


class Adapter(EnergyReading, GasReading):
    """
    The Adapter makes the Adaptee's interface compatible with the EnergyReading's
    interface via multiple inheritance.
    """

    def request(self, reading) -> str:
        '''
        request in the adapter converts to KWh using the volume * calorific value (default 40) *1.02264 / 3.6
        :param reading: float
        :return: string converted to KWh
        '''
        reading_value = float(self.gas_request(reading).split(' ')[1])
        converted_value = (reading_value * 40 * 1.02264)/3.6
        return f"Reading {converted_value:.2f}"


def client_code(target: "EnergyReading", reading) -> None:
    """
    The client code supports all classes that follow the EnergyReading interface.
    """

    print(target.request(reading), end="")


if __name__ == "__main__":
    print("Using the standard interface for electricity :")
    target = EnergyReading()
    client_code(target, 100.2)
    print('\n')

    gas_reading = GasReading()
    print("The gas reading is not a standardised value :")
    print(gas_reading.gas_request(10002) + "\n")

    adapter = Adapter()

    print("Client can work with the value through the adapter")
    adapter = Adapter()
    client_code(adapter,1000)
