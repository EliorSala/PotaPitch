
class PumpBase:
    def __init__(self,  pump_pin, active_time):
        """
        Initializes the pump with the specified active time.

        :param pump_pin: pin of the pump.
        :param active_time: Duration (in seconds) for which the pump will be active.
        """
        self.pump_pin = pump_pin
        self.pump_pin.on()
        self.active_time = active_time

    def activate_pump(self):
        """
        Abstract method to activate the pump. Must be implemented by any subclass.
        """
        pass
