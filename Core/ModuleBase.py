from Common.ModuleSharedCache import ModuleSharedCache


class ModuleBase:
    def run_module(self, module_shared_cache: ModuleSharedCache):
        raise NotImplementedError
