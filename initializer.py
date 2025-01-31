from Common import consts
from Components.PumpsSwitch import PumpsSwitch
from Components.WaterPumpComponent import WaterPumpComponent
from Facade import Facade
from Modules.ClearLcdModule import ClearLcdModule
from Modules.LcdSwitch import LcdSwitch
from Modules.SensorModule import SensorModule
from Common.PinMap import pin_map
from Modules.StirWaterModule import StirWaterModule
from logger import Logger
from sensors.PhSensor import PhSensor
from sensors.EcSensor import EcSensor
from machine import Pin, ADC, I2C
from Libraries.i2c_lcd import I2cLcd


def initialize():
    logger = Logger()

    ph_sensor_pin = ADC(Pin(pin_map["PH"]))
    ph_sensor = PhSensor(ph_sensor_pin, consts.ph_max, consts.ph_min, consts.avg_array_size)

    ec_sensor_pin = ADC(Pin(pin_map["EC"]))
    ec_sensor = EcSensor(ec_sensor_pin, consts.ec_threshold, consts.avg_array_size)

    ph_led = Pin(pin_map["LED_PH"], Pin.OUT)
    ec_led = Pin(pin_map["LED_EC"], Pin.OUT)
    led_main = Pin(pin_map["MAIN_LED"], Pin.OUT)

    pumps_switch = Pin(pin_map["PUMPS_SWITCH"], Pin.IN, Pin.PULL_UP)
    pumps_switch_component = PumpsSwitch(pumps_switch)
    lcd_switch = Pin(pin_map["LCD_SWITCH"], Pin.IN, Pin.PULL_UP)

    # Initialize I2C - using I2C0 (SDA=GP0, SCL=GP1)
    i2c = I2C(0, scl=Pin(pin_map["LCD_1"]), sda=Pin(pin_map["LCD_0"]), freq=400000)
    # Find I2C address
    i2c_address = i2c.scan()[0]  # Typically it's 0x27 or 0x3F
    # Initialize the LCD display
    lcd = I2cLcd(i2c, i2c_address, 4, 20)  # 4x20 LCD display

    # pump pins
    stirring_pump_pin = Pin(pin_map["STIRRING_PUMP"], Pin.OUT)
    ph_pump_pin = Pin(pin_map["PH_PUMP"], Pin.OUT)
    nutriments_pump_pin = Pin(pin_map["NUTRIMENTS_PUMP"], Pin.OUT)

    stirring_pump = WaterPumpComponent(stirring_pump_pin, consts.stirring_duration)
    ph_pump = WaterPumpComponent(ph_pump_pin, consts.ph_pump_duration)
    nutriments_pump = WaterPumpComponent(nutriments_pump_pin, consts.nutriments_pump_duration)

    stirring_module = StirWaterModule(stirring_pump)

    modules_list = [
        LcdSwitch(lcd, lcd_switch),
        ClearLcdModule(lcd),
        SensorModule(ec_sensor, lcd, nutriments_pump, ec_led, stirring_module, pumps_switch_component,
                     consts.skip_count, logger),
        SensorModule(ph_sensor, lcd, ph_pump, ph_led, stirring_module, pumps_switch_component, consts.skip_count,
                     logger),
        stirring_module
    ]

    facade = Facade(led_main, modules_list, consts.cycle_frequency, logger)

    return facade
