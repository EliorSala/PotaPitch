from machine import ADC

from Core.SensorBase import Sensor


class EcSensor(Sensor):
    def __init__(self, ec_pin: ADC, ec_min: float):
        self.ec_pin: ADC = ec_pin
        self.ec_min = ec_min
        self.last_values = [0] * 100
        self.last_values_index = 0

    def read_value(self):
        # Read raw analog value from the sensor (0 to 65535 for 16-bit resolution)
        raw_value = self.ec_pin.read_u16()

        # Convert to voltage (Assuming 3.3V reference voltage)
        voltage = (raw_value / 65535.0) * 3.3

        self.last_values[self.last_values_index] = voltage
        self.last_values_index += 1
        if self.last_values_index >= len(self.last_values):
            self.last_values_index = 0

        mean_voltage: float
        try:
            mean_values = list(filter(lambda value: value != 0, sorted(self.last_values)[2:-2]))
            mean_voltage = sum(mean_values) / len(mean_values)
        except ZeroDivisionError:
            mean_values = list(filter(lambda value: value != 0, sorted(self.last_values)))
            mean_voltage = sum(mean_values) / len(mean_values)

        conductivity = mean_voltage * 100

        return conductivity

    def is_valid_value(self, value):
        return value > self.ec_min

    def get_lcd_string(self, ec_value):
        return (f"Ec range: {self.ec_min} <" +
                f"Ec value: {ec_value}\n")
