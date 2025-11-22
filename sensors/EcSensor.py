from machine import ADC

from Core.SensorBase import Sensor


class EcSensor(Sensor):
    def __init__(self, ec_pin: ADC, ec_min: float, avg_array_size: int):
        super().__init__(avg_array_size)
        self.ec_pin: ADC = ec_pin
        self.ec_min = ec_min

    def read_value(self):
        # Read raw analog value from the sensor (0 to 65535 for 16-bit resolution)
        raw_value = self.ec_pin.read_u16()

        # Convert to voltage (Assuming 3.3V reference voltage)
        voltage = (raw_value / 65535.0) * 3.3

        self.last_values[self.last_values_index] = voltage
        self.last_values_index += 1
        if self.last_values_index >= len(self.last_values):
            self.last_values_index = 0

        mean_voltage: float = self.calculate_mean()

        conductivity = self.get_conductivity(mean_voltage)  # mean_voltage * 10185 - 27056
        return conductivity

    def is_valid_value(self, value):
        return value > self.ec_min

    def get_lcd_string(self, ec_value):
        return (f"Ec range: {self.ec_min} <" +
                f"Ec value: {ec_value}\n")

    @staticmethod
    def get_conductivity(voltage):
        ec = (69.26 * voltage ** 3 + 401.45 * voltage - 18.68)
        return ec