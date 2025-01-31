from Common import consts
from Common.ModuleSharedCache import ModuleSharedCache
from Components.PumpsSwitch import PumpsSwitch
from Core.PumpBase import PumpBase
from Core.ModuleBase import ModuleBase
from Core.StirSwitchBase import StirSwitchBase
from Libraries.i2c_lcd import I2cLcd
from Core.SensorBase import Sensor
from logger import Logger


class SensorModule(ModuleBase):
    def __init__(self, sensor, lcd, pump, led, stir_switch, pump_switch, skip_count, logger):
        self._sensor: Sensor = sensor
        self._lcd: I2cLcd = lcd
        self._pump: PumpBase = pump
        self._led = led
        self._stir_switch: StirSwitchBase = stir_switch
        self._pump_switch: PumpsSwitch = pump_switch
        self._skip_count = skip_count
        self._count = 0
        self._logger: Logger = logger

    def run_module(self, module_shared_cache: ModuleSharedCache):
        value = self._sensor.read_value()
        lcd_str = self._sensor.get_lcd_string(value)

        self._lcd.putstr(lcd_str)
        self._logger.info(f"{value}")
        self._count += 1
        if self._count > self._skip_count and not self._sensor.is_valid_value(value):
            if self._pump_switch.should_run_pumps() and module_shared_cache.liquid_pump_cooldown == 0:
                self._logger.info(f"pump activating")
                self._stir_switch.activate_stir()
                self._pump.activate_pump()
                module_shared_cache.liquid_pump_cooldown = consts.liquid_pump_cooldown
            self._led.on()
            self._count = 0
        else:
            self._led.off()
