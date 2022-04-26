from random import random


class Weather:
    def __init__(self, weather_info):
        self.weather_info = weather_info

    def random_death(self):
        random_death_rate = 0.8 + random()*0.15
        self.weather_info["random_death_rate"] = random_death_rate

    def pack_data_to_farm(self):
        self.random_death()
        return self.weather_info
