from random import uniform
from hx711 import HX711
import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

# Just for simulating
MIN_DELTA = 50
MAX_DELTA = 500

INPUT_PIN = 21
OUTPUT_PIN = 20

class Weigher:

    current_weight_grams = 0

    def __init__(self):
        self.hx = HX711(INPUT_PIN, OUTPUT_PIN)
        self.hx.set_offset(8552308.25)
        self.hx.set_scale(372.81775700934577)
    
    def get_delta(self):
        previous_weight = self.current_weight_grams
        self.weigh()
        return self.current_weight_grams - previous_weight
    
    def weigh(self):
        self.hx.power_up()
        val = self.hx.get_grams()
        self.hx.power_down()
        self.current_weight_grams = val
    
    def cleanup(self):
        GPIO.cleanup()
        print("Weigher cleaned up GPIOs")
