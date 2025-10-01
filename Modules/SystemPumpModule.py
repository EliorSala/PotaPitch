from Common.ModuleSharedCache import ModuleSharedCache
from Components import TogglePumpComponent
from Core.ModuleBase import ModuleBase
from Core.PumpBase import PumpBase


class SystemPumpModule(ModuleBase):
    def __init__(self, system_pump):
        self.system_pump: TogglePumpComponent = system_pump

    def run_module(self, module_shared_cache: ModuleSharedCache):
        self.system_pump.activate_pump()
