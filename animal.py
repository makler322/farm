class Animal:
    def __init__(self, animals_info):
        self.animals_info = animals_info

        self.cnt_young = animals_info["farm_cnt_young"]
        self.cnt_adult = animals_info["farm_cnt_adult"]
        self.cnt_old = animals_info["farm_cnt_old"]

        self.start_sum = animals_info["farm_start_sum"]

    def pack_data_to_farm(self):
        # self.recommended_food()
        return self.animals_info
