from Common.ModuleSharedCache import ModuleSharedCache
from Core.ModuleBase import ModuleBase
from Libraries.i2c_lcd import I2cLcd


class ClearLcdModule(ModuleBase):
    def __init__(self, lcd):
        self._lcd: I2cLcd = lcd

    def run_module(self, module_shared_cache: ModuleSharedCache):
        self._lcd.clear()
