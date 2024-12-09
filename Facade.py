from machine import Timer

from Core.ModuleBase import ModuleBase


class Facade:
    def __init__(self, main_led, modules_list):
        self.tim = Timer()
        self._main_led = main_led
        self._modules_list: list[ModuleBase] = modules_list

    def start(self):
        self.tim.init(freq=5, mode=Timer.PERIODIC, callback=self.on_tick)

    def on_tick(self, timer):
        try:
            print("start")
            self._main_led.toggle()

            for module in self._modules_list:
                module.run_module()

            self._main_led.toggle()
            print("end")
        except Exception as e:
            print(e)
