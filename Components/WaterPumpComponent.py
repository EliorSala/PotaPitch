import time

from Core.PumpBase import PumpBase


class WaterPumpComponent(PumpBase):
    def __init__(self, pump_pin, active_time):
        """
        Initializes the water pump with a specified active time.

        :param active_time: Duration (in seconds) for which the pump will be active.
        """
        super().__init__(pump_pin, active_time)

    def activate_pump(self):
        """
        Activates the water pump for the duration equal to active_time.
        """
        self.pump_pin.off()
        time.sleep(self.active_time)
        self.pump_pin.on()
