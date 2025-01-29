
class PumpBase:
    def __init__(self, pump_pin, default_active_time):
        """
        Initializes the pump with the specified active time.

        :param pump_pin: pin of the pump.
        :param default_active_time: Duration (in seconds) for which the pump will be active.
        """
        self.pump_pin = pump_pin
        self.pump_pin.on()
        self.default_active_time = default_active_time

    def activate_pump(self, active_time=None):
        """
        Abstract method to activate the pump. Must be implemented by any subclass.
        """
        pass
