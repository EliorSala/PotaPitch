from machine import Timer

from Common.ModuleSharedCache import ModuleSharedCache
from Core.ModuleBase import ModuleBase
from logger import Logger


class Facade:
    def __init__(self, main_led, modules_list, cycle_frequency, logger):
        self.tim = Timer()
        self._main_led = main_led
        self._modules_list: list[ModuleBase] = modules_list
        self.freq = 1 / cycle_frequency
        self._logger: Logger = logger
        self._module_shared_cache = ModuleSharedCache()

    def start(self):
        self.tim.init(freq=self.freq, mode=Timer.PERIODIC, callback=self.on_tick)

    def on_tick(self, timer):
        self._logger.cleanup_logs()
        try:
            self._main_led.toggle()

            for module in self._modules_list:
                module.run_module(self._module_shared_cache)

            if self._module_shared_cache.liquid_pump_cooldown > 0:
                self._module_shared_cache.liquid_pump_cooldown -= 1

            self._main_led.toggle()
        except Exception as e:
            print(e)
