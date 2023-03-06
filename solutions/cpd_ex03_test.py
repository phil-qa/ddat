import CDP_ex03_factory_sln as ser

new_reading = ser.MeterReading('e101','01-01-2023', 'electricity', '100')

serializer = ser.MeterSerializer()

print(serializer.serialize(new_reading, 'XML') )

print(serializer.serialize(new_reading, 'JSON'))