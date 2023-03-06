# Title: cmc_ex02_duplication
# Purpose : Exercise 2 isolating duplication
# Instructions : Perform a code review on the code below. Determine and correct any issues you see.
# Therm price is about 109.2 per therm as at 01.2023
import datetime
import os

from logos import gas_logo


class GasReading:
    def __init__(self, volume_unit, volume_reading, time_stamp, period):
        self.volume_unit = volume_unit
        self.volume_reading = volume_reading
        self.timestamp = time_stamp
        self.period = period


class Setup:
    def __init__(self):
        self.file_name = None
        self.units = None
        self.cost_per_therm = None
        self.set_values()

    def set_values(self):
        self.file_name = input('What is the reading file path :')
        self.units = input("Are the readings in m\u00B3 or ft\u00B3  (m/f) :")
        self.cost_per_therm = float(input("What is the cost per therm "))


class Converter:
    @staticmethod
    def standardise_timestamp(original):
        time_format = "%Y-%m-%d %H:%M:%S"
        return datetime.datetime.strptime(original, time_format)

    @staticmethod
    def convert_volume_to_feet(volume_in_meters):
        return int(volume_in_meters) * 35.3146667


def read_file(setup):
    if not os.path.exists(setup.file_name):
        return None

    readings = []
    with open(setup.file_name) as operating_file:
        for entry in operating_file.readlines():
            delimited_line = entry.split(',')
            reading = delimited_line[0]
            timestamp = Converter.standardise_timestamp(delimited_line[1])
            period = delimited_line[2]
            readings.append(
                GasReading(volume_unit=setup.units, volume_reading=reading, time_stamp=timestamp, period=period))

    return readings


def cost_for_use(readings, settings):
    record_of_costs = []
    for reading in readings:
        volume = reading.volume_reading
        if reading.volume_unit == 'm':
            volume = Converter.convert_volume_to_feet(volume)
        record_of_costs.append(int(volume) * settings.cost_per_therm)
    return sum(record_of_costs)


def main():
    print(gas_logo)
    parameters = Setup()
    readings = read_file(parameters)
    if readings == None:
        print("Error finding the file")
        return None
    print(f"Cost of energy £{cost_for_use(readings,parameters):.2f}")


if __name__ == '__main__':
    main()
