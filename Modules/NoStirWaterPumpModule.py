from Common.ModuleSharedCache import ModuleSharedCache
from Core.ModuleBase import ModuleBase
from Core.PumpBase import PumpBase
from Core.StirSwitchBase import StirSwitchBase


class NoStirWaterPumpModule(ModuleBase, StirSwitchBase):
    def run_module(self, module_shared_cache: ModuleSharedCache):
        return

    def activate_stir(self):
        return
