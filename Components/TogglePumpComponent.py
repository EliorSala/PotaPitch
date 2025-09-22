import time

from Core.PumpBase import PumpBase


class TogglePumpComponent(PumpBase):
    def __init__(self, pump_pin):
        """
        Initializes the water pump with a specified active time.

        :param active_time: Duration (in seconds) for which the pump will be active.
        """
        super().__init__(pump_pin)
        self.activated = False

    def activate_pump(self):
        """
        Activates the water pump for the duration equal to active_time.
        """

        if self.activated:
            self.pump_pin.off()
        else:
            self.pump_pin.on()
        self.activated = not self.activated
