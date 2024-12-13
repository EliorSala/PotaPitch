from machine import Timer

from Core.ModuleBase import ModuleBase
from logger import Logger


class Facade:
    def __init__(self, main_led, modules_list, logger):
        self.tim = Timer()
        self._main_led = main_led
        self._modules_list: list[ModuleBase] = modules_list
        self._logger: Logger = logger

    def start(self):
        self.tim.init(freq=5, mode=Timer.PERIODIC, callback=self.on_tick)

    def on_tick(self, timer):
        self._logger.cleanup_logs()
        try:
            self._main_led.toggle()

            for module in self._modules_list:
                module.run_module()

            self._main_led.toggle()
        except Exception as e:
            print(e)
