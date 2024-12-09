from Components.PumpsSwitch import PumpsSwitch
from Core.PumpBase import PumpBase
from Core.ModuleBase import ModuleBase
from Core.StirSwitchBase import StirSwitchBase
from Libraries.i2c_lcd import I2cLcd
from Core.SensorBase import Sensor


class SensorModule(ModuleBase):
    def __init__(self, sensor, lcd, pump, led, stir_switch, pump_switch):
        self._sensor: Sensor = sensor
        self._lcd: I2cLcd = lcd
        self._pump: PumpBase = pump
        self._led = led
        self._stir_switch: StirSwitchBase = stir_switch
        self._pump_switch: PumpsSwitch = pump_switch

    def run_module(self):
        value = self._sensor.read_value()
        lcd_str = self._sensor.get_lcd_string(value)
        self._lcd.putstr(lcd_str)

        if not self._sensor.is_valid_value(value):
            if self._pump_switch.should_run_pumps():
                self._stir_switch.activate_stir()
                self._pump.activate_pump()
            self._led.on()
        else:
            self._led.off()
