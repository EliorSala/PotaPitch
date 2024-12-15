class PumpsSwitch:
    def __init__(self, pumps_switch):
        self._pumps_switch = pumps_switch

    def should_run_pumps(self):
        return self._pumps_switch.value() != 0
