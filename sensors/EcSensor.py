from machine import ADC

from sensors.SensorBase import Sensor


class EcSensor(Sensor):
    def __init__(self, ec_pin: ADC, ec_min: float):
        self.ec_pin: ADC = ec_pin
        self.ec_min = ec_min

    def read_value(self):
        # Read raw analog value from the sensor (0 to 65535 for 16-bit resolution)
        raw_value = self.ec_pin.read_u16()

        # Convert to voltage (Assuming 3.3V reference voltage)
        voltage = (raw_value / 65535.0) * 2.3

        # Placeholder formula to convert voltage to conductivity
        # (You will need the sensor's datasheet to apply the correct conversion)
        conductivity = voltage * 1000  # Replace with actual conversion formula

        return conductivity

    def is_valid_value(self, value):
        return value > self.ec_min

    def get_lcd_string(self, ec_value):
        return (f"Ec threshold: {self.ec_min} <\n" +
                f"Ec value: {ec_value}\n")
