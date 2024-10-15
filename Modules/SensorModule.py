from Modules.ModuleBase import ModuleBase
from Libraries.i2c_lcd import I2cLcd
from sensors.SensorBase import Sensor


class SensorModule(ModuleBase):
    def __init__(self, sensor, lcd, led):
        self._sensor: Sensor = sensor
        self._lcd: I2cLcd = lcd
        self._led = led

    def run_module(self):
        value = self._sensor.read_value()
        lcd_str = self._sensor.get_lcd_string(value)
        self._lcd.putstr(lcd_str)

        if not self._sensor.is_valid_value(value):
            # TODO: implement pump action
            self._led.on()
        else:
            self._led.off()
