from machine import ADC

from sensors.SensorBase import Sensor


class PhSensor(Sensor):
    def __init__(self, ph_pin: ADC, ph_max: float, ph_min: float):
        self.ph_pin: ADC = ph_pin
        self.ph_max = ph_max
        self.ph_min = ph_min

    def read_value(self):
        # Read raw analog value from the sensor (0 to 65535 for 16-bit resolution)
        raw_value = self.ph_pin.read_u16()

        # Convert to voltage (Assuming 3.3V reference voltage)
        voltage = (raw_value / 65535.0) * 3.3
        print(voltage)

        # Convert voltage to pH value (assuming 0V -> pH 0 and 3V -> pH 14)
        ph_value = (voltage / 0.72) * 14
        return ph_value

    def is_valid_value(self, value):
        return self.ph_max > value > self.ph_min

    def get_lcd_string(self, ph_value):
        return (f"Ph threshold: {self.ph_min} - {self.ph_max}\n" +
                f"Ph value: {ph_value}\n")
