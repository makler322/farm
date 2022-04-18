class Recount:
    def __init__(self, animals_info):
        self.cnt_young = animals_info["cnt_young"]
        self.cnt_adult = animals_info["cnt_adult"]
        self.cnt_old = animals_info["cnt_old"]

        self.sum_young = animals_info["sum_young"]
        self.sum_adult = animals_info["sum_adult"]
        self.sum_old = animals_info["sum_old"]

    def get_rate(self, cnt):
        rate = 0.01
        while cnt * rate < 1.5:
            rate *= 1.1
        rate = min(rate, 0.3)
        return 1 - rate

    def recount(self):
        total_sum = self.sum_young * self.cnt_young + self.sum_adult * self.cnt_adult + self.sum_old * self.cnt_old
        total_cnt = self.cnt_old + self.cnt_adult + self.cnt_young
        if total_cnt == 0:
            return {
                "sum_young": 0,
                "sum_adult": 0,
                "sum_old": 0,
            }

        sum_per_animal_avg = total_sum / total_cnt

        if self.cnt_adult > 0 and self.cnt_old > 0:
            old_rate = self.get_rate(self.cnt_old)
            self.sum_old = old_rate * sum_per_animal_avg
            self.sum_young = sum_per_animal_avg if self.cnt_young > 0 else 0
            self.sum_adult = \
                (total_sum - self.sum_old * self.cnt_old - self.sum_young * self.cnt_young) / self.cnt_adult

        elif self.cnt_adult > 0:
            young_rate = self.get_rate(self.cnt_young)
            self.sum_young = young_rate * sum_per_animal_avg
            self.sum_old = 0
            self.sum_adult = \
                (total_sum - self.sum_old * self.cnt_old - self.sum_young * self.cnt_young) / self.cnt_adult

        elif self.cnt_old > 0:
            old_rate = self.get_rate(self.cnt_old)
            self.sum_old = old_rate * sum_per_animal_avg
            self.sum_adult = 0
            self.sum_young = \
                (total_sum - self.sum_old * self.cnt_old - self.sum_adult * self.cnt_adult) / self.cnt_young
        else:
            self.sum_young = sum_per_animal_avg if self.cnt_young > 0 else 0
            self.sum_adult = 0
            self.sum_old = 0

        animals_ans_info = {
            "sum_young": int(self.sum_young),
            "sum_adult": int(self.sum_adult),
            "sum_old": int(self.sum_old),
            "sum_avg": int(sum_per_animal_avg)
        }

        return animals_ans_info
