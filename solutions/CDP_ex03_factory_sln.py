# Title: CDP_ex03_factory
# Purpose : To exercise the process of applying the factory pattern
# Instructions : Data containing meter readings for gas and electricity may arrive in
#               either json or xml format. Review the code below and implement a factory response
#               for json, this is tested in CPD_ex03_test.py
import json
import xml.etree.ElementTree as etree

class MeterReading:
    def __init__(self, meter_id, time_stamp,meter_type, reading):
        self.meter_id = meter_id
        self.time_stamp = time_stamp
        self.meter_type = meter_type
        self.reading = reading

class MeterSerializer:
    def serialize(self, reading, format):
        if format == 'XML':
            formatted_reading = etree.Element('reading', attrib={'meter': reading.meter_id})
            time_stamp = etree.SubElement(formatted_reading, 'time_stamp')
            time_stamp.text = reading.time_stamp
            meter_type = etree.SubElement(formatted_reading, 'meter_type')
            meter_type.text = reading.meter_type
            meter_reading = etree.SubElement(formatted_reading, 'reading')
            meter_reading.text = reading.reading
            return etree.tostring(formatted_reading, encoding='unicode')
        elif format == 'JSON':
            formatted_reading = {
                'meter_id' : reading.meter_id,
                'meter_type' : reading.meter_type,
                'time_stamp' : reading.time_stamp,
                'meter_reading' : reading.reading
            }
            return json.dumps(formatted_reading)
        else:
            raise ValueError(format)