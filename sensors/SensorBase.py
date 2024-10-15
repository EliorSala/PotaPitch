class Sensor:
    def read_value(self):
        raise NotImplementedError

    def is_valid_value(self, value):
        raise NotImplementedError

    def get_lcd_string(self, value):
        raise NotImplementedError
