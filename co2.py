
from CO2Meter import *
import time
sensor = CO2Meter("/dev/hidraw0")
while True:
    time.sleep(1)
    data = sensor.get_data()
    if 'temperature' in data and 'co2' in data:
        f = open('/dev/shm/co2', 'w')
        f.write(str(data['co2']))
        f.close()

        f = open('/dev/shm/temperature', 'w')
        f.write(str(data['temperature']))
        f.close()


