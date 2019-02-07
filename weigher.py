from random import uniform

# Just for simulating
MIN_DELTA = 50
MAX_DELTA = 500

class Weigher:

    current_weight_grams = 0

    def __init__(self):
        print("Weigher constructor")
    
    def get_delta(self):
        previous_weight = self.current_weight_grams
        self.weigh()
        return self.current_weight_grams - previous_weight
    
    def weigh(self):
        # This would actually be some code to fetch the weight
        self.current_weight_grams = self.current_weight_grams + uniform(MIN_DELTA, MAX_DELTA)