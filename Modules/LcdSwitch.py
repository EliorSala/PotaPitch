from Common.ModuleSharedCache import ModuleSharedCache
from Core.ModuleBase import ModuleBase
from Libraries.i2c_lcd import I2cLcd


class LcdSwitch(ModuleBase):
    def __init__(self, lcd, lcd_switch):
        self._lcd: I2cLcd = lcd
        self._lcd_switch = lcd_switch

    def run_module(self, module_shared_cache: ModuleSharedCache):
        if self._lcd_switch.value() != 0:
            self._lcd.display_on()
            self._lcd.backlight_on()
        else:
            self._lcd.display_off()
            self._lcd.backlight_off()
