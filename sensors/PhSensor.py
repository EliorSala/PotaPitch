from machine import ADC

from Core.SensorBase import Sensor


class PhSensor(Sensor):
    def __init__(self, ph_pin: ADC, ph_max: float, ph_min: float):
        self.ph_pin: ADC = ph_pin
        self.ph_max = ph_max
        self.ph_min = ph_min
        self.last_values = [0] * 100
        self.last_values_index = 0

    def read_value(self):
        # Read raw analog value from the sensor (0 to 65535 for 16-bit resolution)
        raw_value = self.ph_pin.read_u16()

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

        # Convert voltage to pH value (assuming 0V -> pH 0 and 3V -> pH 14)
        ph_value = round(mean_voltage * -9.28 + 29.7, 2)

        return ph_value

    def is_valid_value(self, value):
        return self.ph_max > value > self.ph_min

    def get_lcd_string(self, ph_value):
        return (f"Ph range: {self.ph_min} - {self.ph_max}\n" +
                f"Ph value: {ph_value}\n")
