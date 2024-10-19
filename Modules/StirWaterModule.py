from Core.ModuleBase import ModuleBase
from Core.PumpBase import PumpBase
from Core.StirSwitchBase import StirSwitchBase


class StirWaterModule(ModuleBase, StirSwitchBase):
    def __init__(self, stirring_pump):
        self.stirring_pump: PumpBase = stirring_pump
        self._should_activate = False

    def run_module(self):
        if self._should_activate:
            self.stirring_pump.activate_pump()
            self._should_activate = False

    def activate_stir(self):
        self._should_activate = True
