import time

from Common import consts
from Common.PinMap import pin_map
from sensors.PhSensor import PhSensor
from sensors.EcSensor import EcSensor
from machine import Pin, ADC, I2C
from Libraries.i2c_lcd import I2cLcd


def display_test(lcd, value):
    lcd.clear()
    lcd.putstr(value)


def test():
    i2c = I2C(0, scl=Pin(pin_map["LCD_1"]), sda=Pin(pin_map["LCD_0"]), freq=400000)
    i2c_address = i2c.scan()[0]  # Typically it's 0x27 or 0x3F
    lcd = I2cLcd(i2c, i2c_address, 4, 20)  # 4x20 LCD display

    display_test(lcd, "starting test\n in any second...")
    time.sleep(3)

    # ph test
    ph_sensor_pin = ADC(Pin(pin_map["PH"]))
    display_test(lcd, f"ph raw value: {ph_sensor_pin.read_u16()}")
    time.sleep(1)

    # ec test
    ec_sensor_pin = ADC(Pin(pin_map["EC"]))
    display_test(lcd, f"ec raw value: {ph_sensor_pin.read_u16()}")
    time.sleep(1)

    # led test
    ph_led = Pin(pin_map["LED_PH"], Pin.OUT)
    ph_led.on()
    display_test(lcd, "ph led test")
    time.sleep(1)
    ph_led.off()

    ec_led = Pin(pin_map["LED_EC"], Pin.OUT)
    ec_led.on()
    display_test(lcd, "ec led test")
    time.sleep(1)
    ec_led.off()

    led_main = Pin(pin_map["MAIN_LED"], Pin.OUT)
    led_main.on()
    display_test(lcd, "main led test")
    time.sleep(1)
    led_main.off()

    lcd_switch = Pin(pin_map["LCD_SWITCH"], Pin.IN, Pin.PULL_UP)
    display_test(lcd, f"lcd switch: {lcd_switch.value()}\n" +
                      f"please switch the switch")
    time.sleep(3)
    display_test(lcd, f"lcd switch value now" +
                      f"{lcd_switch.value()}")
    time.sleep(1)

    # pumps
    stirring_pump_pin = Pin(pin_map["STIRRING_PUMP"], Pin.OUT)
    display_test(lcd, "stirring pump test")
    stirring_pump_pin.off()
    time.sleep(3)
    stirring_pump_pin.on()

    ph_pump_pin = Pin(pin_map["PH_PUMP"], Pin.OUT)
    display_test(lcd, "ph pump test")
    ph_pump_pin.off()
    time.sleep(3)
    ph_pump_pin.on()

    nutriments_pump_pin = Pin(pin_map["NUTRIMENTS_PUMP"], Pin.OUT)
    display_test(lcd, "nutriments pump test")
    nutriments_pump_pin.off()
    time.sleep(3)
    nutriments_pump_pin.on()


if __name__ == '__main__':
    test()

