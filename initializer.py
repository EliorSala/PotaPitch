from Common import consts
from Facade import Facade
from Modules.ClearLcdModule import ClearLcdModule
from Modules.LcdSwitch import LcdSwitch
from Modules.SensorModule import SensorModule
from Common.PinMap import pin_map
from sensors.PhSensor import PhSensor
from sensors.EcSensor import EcSensor
from machine import Pin, ADC, I2C
from Libraries.i2c_lcd import I2cLcd


def initialize():
    ph_sensor_pin = ADC(Pin(26))
    ph_sensor = PhSensor(ph_sensor_pin, consts.ph_max, consts.ph_min)

    ec_sensor_pin = ADC(Pin(28))
    ec_sensor = EcSensor(ec_sensor_pin, consts.ec_threshold)

    ph_led = Pin(pin_map["LED_PH"], Pin.OUT)
    ec_led = Pin(pin_map["LED_EC"], Pin.OUT)
    led_main = Pin(pin_map["MAIN_LED"], Pin.OUT)

    lcd_switch = Pin(pin_map["LCD_SWITCH"], Pin.IN, Pin.PULL_UP)

    # Initialize I2C - using I2C0 (SDA=GP0, SCL=GP1)
    i2c = I2C(0, scl=Pin(pin_map["LCD_1"]), sda=Pin(pin_map["LCD_0"]), freq=400000)
    # Find I2C address
    i2c_address = i2c.scan()[0]  # Typically it's 0x27 or 0x3F
    # Initialize the LCD display
    lcd = I2cLcd(i2c, i2c_address, 4, 20)  # 4x20 LCD display

    modules_list = [
        LcdSwitch(lcd, lcd_switch),
        ClearLcdModule(lcd),
        SensorModule(ph_sensor, lcd, ph_led),
        SensorModule(ec_sensor, lcd, ec_led)
    ]

    facade = Facade(led_main, modules_list)

    return facade
