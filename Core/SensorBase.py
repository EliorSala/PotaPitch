class Sensor:
    def __init__(self, avg_array_size):
        self.last_values = [0] * avg_array_size
        self.last_values_index = 0

    def read_value(self):
        raise NotImplementedError

    def is_valid_value(self, value):
        raise NotImplementedError

    def get_lcd_string(self, value):
        raise NotImplementedError

    def calculate_mean(self):
        mean_voltage: float
        try:
            mean_values = list(filter(lambda value: value != 0, sorted(self.last_values)[2:-2]))
            mean_voltage = sum(mean_values) / len(mean_values)
        except ZeroDivisionError:
            mean_values = list(filter(lambda value: value != 0, sorted(self.last_values)))
            mean_voltage = sum(mean_values) / len(mean_values)
        return mean_voltage
