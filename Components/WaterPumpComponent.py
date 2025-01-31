import time

from Core.PumpBase import PumpBase


class WaterPumpComponent(PumpBase):
    def __init__(self, pump_pin, default_active_time):
        """
        Initializes the water pump with a specified active time.

        :param default_active_time: Duration (in seconds) for which the pump will be active.
        """
        super().__init__(pump_pin, default_active_time)

    def activate_pump(self, active_time=None):
        """
        Activates the water pump for the duration equal to active_time.
        """
        self.pump_pin.off()
        if active_time is None:
            time.sleep(self.default_active_time)
        else:
            time.sleep(active_time)
        self.pump_pin.on()
