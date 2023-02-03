#gas_manager
#functions for managing a gas supply
#Includes test data
from datetime import datetime, timedelta
import random

gas_readings = []

class GasReading:
    def __init__(self, volume, time_stamp, period):
        '''
        GasReading - class containing a single gas reading
        :param volume: M2
        :param time_stamp: reading time
        :param period: time period in minutes
        '''

        self._volume = volume
        self._time_stamp = time_stamp
        self._period = period

    def get_volume(self):
        return self._volume

    def get_time_stamp(self):
        return self._time_stamp

    def get_period(self):
        return self._period

def get_test_data():
    readings = []
    now = datetime.now()
    readings.append(GasReading(random.randint(0,100), now,30))
    readings.append(GasReading(random.randint(0,100), now-timedelta(minutes=15),30))
    readings.append(GasReading(random.randint(0, 100), now - timedelta(minutes=30), 30))
    return readings

def add_reading(volume=0, time_stamp=datetime.now(), period=30):
    '''
    add_reading, creates an instance of GasRecord and stored it into the local array
    :param volume: integer m2
    :param time_stamp: string date/time
    :param period: integer minutes
    '''
    gas_readings.append(GasReading(volume, time_stamp, period))