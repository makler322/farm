class Farm:
    def __init__(self):
        self.animals_info = None
        self.weather_info = None

    def pack_data_to_modeling(self, animals_info, weather_info):
        self.animals_info = animals_info
        self.weather_info = weather_info
        farm_info = {}
        ans_dict = {
            "to_sale_young": [],
            "to_sale_adult": [],
            "to_sale_old": [],
            "sum_young": [],
            "sum_adult": [],
            "sum_old": [],
            "food_cost": [],
            "forfeit": [],
            "profit": [],
            "to_remainder_young": [],
            "to_remainder_adult": [],
            "to_remainder_old": [],
            "cur_sum": [],
            "default_flag": False
        }

        farm_info["ans_dict"] = ans_dict
        farm_info["cur_sum"] = self.animals_info["farm_start_sum"]
        farm_info["default_flag"] = False
        farm_info["random_death_rate"] = self.weather_info["random_death_rate"]

        farm_info["cnt_young"] = self.animals_info["farm_cnt_young"]
        farm_info["cnt_adult"] = self.animals_info["farm_cnt_adult"]
        farm_info["cnt_old"] = self.animals_info["farm_cnt_old"]
        farm_info["start_sum"] = self.animals_info["farm_start_sum"]

        farm_info["food_cost_per_year"] = self.weather_info["food_cost_per_year"]
        farm_info["birth_rate_adult"] = self.weather_info["birth_rate_adult"]
        farm_info["birth_rate_adult"] = self.weather_info["birth_rate_adult"]
        farm_info["birth_rate_old"] = self.weather_info["birth_rate_old"]
        farm_info["survival_rate_young"] = self.weather_info["survival_rate_young"]
        farm_info["death_rate_old"] = self.weather_info["death_rate_old"]

        return farm_info
