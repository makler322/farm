class Modeling:
    def __init__(self):
        self.cnt_young = None
        self.cnt_adult = None
        self.cnt_old = None
        self.start_sum = None
        self.food_cost_per_year = None

        self.birth_rate_adult = None
        self.birth_rate_old = None
        self.survival_rate_young = None
        self.death_rate_old = None

        self.raw_cur_sum = None
        self.cur_sum = None
        self.default_flag = None
        self.ans_dict = None
        self.random_death_rate = None

    def get_cost(self, animal_type, profit_rate=1.4):
        if animal_type == "young":
            return int(self.cnt_young * self.food_cost_per_year * 0.5 * profit_rate)

        if animal_type == "adult":
            return int(self.cnt_adult * self.food_cost_per_year * profit_rate)

        if animal_type == "old":
            return int(self.cnt_old * self.food_cost_per_year * profit_rate / 3)

    def coverage_amount_young(self, cnt_young_next_year, coverage_amount):
        if (cnt_young_next_year - self.cnt_young) > 1:
            to_sale_young = max(int((cnt_young_next_year - self.cnt_young) / 4), 1)
            self.cnt_young = cnt_young_next_year - to_sale_young
            desired_amount = coverage_amount + self.get_cost("young")
            sum_per_young = int(desired_amount / to_sale_young)
            self.cur_sum += desired_amount
            coverage_amount = 0
            # print(f"Sale {to_sale_young} of young animals by sum: {sum_per_young}")

        else:
            to_sale_young = 0
            sum_per_young = -1
            coverage_amount += self.cnt_young * self.food_cost_per_year * 0.5
        return to_sale_young, sum_per_young, coverage_amount

    def coverage_amount_adult(self, cnt_adult_next_year, coverage_amount):
        if (cnt_adult_next_year - self.cnt_adult) > 1:
            to_sale_adult = max(int((cnt_adult_next_year - self.cnt_adult) / 5), 1)
            self.cnt_adult = cnt_adult_next_year - to_sale_adult
            desired_amount = coverage_amount + self.get_cost("adult")
            sum_per_adult = int(desired_amount / to_sale_adult)
            self.cur_sum += desired_amount
            coverage_amount = 0
            # print(f"Sale {to_sale_adult} of adult animals by sum: {sum_per_adult}")

        else:
            to_sale_adult = 0
            sum_per_adult = -1
            coverage_amount += self.cnt_adult * self.food_cost_per_year
        return to_sale_adult, sum_per_adult, coverage_amount

    def coverage_amount_old(self, cnt_old_next_year, coverage_amount):
        if (cnt_old_next_year - self.cnt_old) > 1:
            to_sale_old = max(int((cnt_old_next_year - self.cnt_old) / 1.5), 1)
            self.cnt_old = cnt_old_next_year - to_sale_old
            desired_amount = coverage_amount + self.get_cost("old")
            sum_per_old = int(desired_amount / to_sale_old)
            self.cur_sum += desired_amount
            coverage_amount = 0
            # print(f"Sale {to_sale_old} of old animals by sum: {sum_per_old}")

        else:
            to_sale_old = 0
            sum_per_old = -1
            coverage_amount += self.cnt_old * self.food_cost_per_year / 3
        return to_sale_old, sum_per_old, coverage_amount

    def random_death(self):
        self.cnt_young = int(self.cnt_young * self.random_death_rate)
        self.cnt_adult = int(self.cnt_adult * self.random_death_rate)
        self.cnt_old = int(self.cnt_old * self.random_death_rate)

    def get_rate(self, cnt):
        rate = 0.01
        while cnt * rate < 1.5:
            rate *= 1.1
        rate = min(rate, 0.3)
        return 1 - rate

    def recount(self, animals_info):
        cnt_young = animals_info["cnt_young"]
        cnt_adult = animals_info["cnt_adult"]
        cnt_old = animals_info["cnt_old"]

        self.sum_young = animals_info["sum_young"]
        self.sum_adult = animals_info["sum_adult"]
        self.sum_old = animals_info["sum_old"]

        total_sum = self.sum_young * cnt_young + self.sum_adult * cnt_adult + self.sum_old * cnt_old
        total_cnt = cnt_old + cnt_adult + cnt_young
        if total_cnt == 0:
            return {
                "sum_young": 0,
                "sum_adult": 0,
                "sum_old": 0,
            }

        sum_per_animal_avg = total_sum / total_cnt

        if cnt_adult > 0 and cnt_old > 0:
            old_rate = self.get_rate(cnt_old)
            self.sum_old = old_rate * sum_per_animal_avg
            self.sum_young = sum_per_animal_avg if cnt_young > 0 else 0
            self.sum_adult = \
                (total_sum - self.sum_old * cnt_old - self.sum_young * cnt_young) / cnt_adult

        elif cnt_adult > 0:
            young_rate = self.get_rate(cnt_young)
            self.sum_young = young_rate * sum_per_animal_avg
            self.sum_old = 0
            self.sum_adult = \
                (total_sum - self.sum_old * cnt_old - self.sum_young * cnt_young) / cnt_adult

        elif cnt_old > 0:
            if cnt_young > 0:
                old_rate = self.get_rate(cnt_old)
                self.sum_old = old_rate * sum_per_animal_avg
                self.sum_adult = 0
                self.sum_young = \
                    (total_sum - self.sum_old * cnt_old - self.sum_adult * cnt_adult) / cnt_young
            else:
                self.sum_old = 10000
                self.sum_adult = 0
                self.sum_young = 0
        else:
            self.sum_young = sum_per_animal_avg if cnt_young > 0 else 0
            self.sum_adult = 0
            self.sum_old = 0

        animals_ans_info = {
            "sum_young": int(self.sum_young),
            "sum_adult": int(self.sum_adult),
            "sum_old": int(self.sum_old),
            "sum_avg": int(sum_per_animal_avg)
        }

        return animals_ans_info

    def modeling_year(self):
        # print("self.cnt_young", self.cnt_young)
        cnt_young_next_year = int(self.birth_rate_adult * self.cnt_adult + self.birth_rate_old * self.cnt_old)
        cnt_adult_next_year = int(self.survival_rate_young * self.cnt_young)
        cnt_old_next_year = int(self.cnt_adult + (1 - self.death_rate_old) * self.cnt_old)

        print("total be", cnt_young_next_year, cnt_adult_next_year, cnt_old_next_year)
        while max(cnt_young_next_year, cnt_adult_next_year, cnt_old_next_year):
            food_cost_next_year = int(self.food_cost_per_year * (
                    cnt_young_next_year / 2 + cnt_adult_next_year + cnt_old_next_year / 3
            ))
            if food_cost_next_year <= self.cur_sum:
                self.ans_dict["food_cost"].append(food_cost_next_year)
                self.cur_sum -= food_cost_next_year
                self.raw_cur_sum = self.cur_sum
                break
            else:
                cnt_young_next_year -= 1 if cnt_young_next_year > 0 else 0
                cnt_adult_next_year -= 1 if cnt_adult_next_year > 0 else 0
                cnt_old_next_year -= 1 if cnt_old_next_year > 0 else 0

        if max(cnt_young_next_year, cnt_adult_next_year, cnt_old_next_year) == 0:
            return False
        coverage_amount = 0
        success_flag = False
        if (cnt_young_next_year - self.cnt_young) > max(
                (cnt_adult_next_year - self.cnt_adult),
                (cnt_old_next_year - self.cnt_old),
                1
        ) and not success_flag:
            success_flag = True
            to_sale_adult, sum_per_adult, coverage_amount_adult = self.coverage_amount_adult(
                cnt_adult_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_adult
            to_sale_old, sum_per_old, coverage_amount_old = self.coverage_amount_old(
                cnt_old_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_old
            to_sale_young, sum_per_young, coverage_amount_young = self.coverage_amount_young(
                cnt_young_next_year, coverage_amount
            )

        elif (cnt_adult_next_year - self.cnt_adult) > max(
                (cnt_young_next_year - self.cnt_young),
                (cnt_old_next_year - self.cnt_old),
                1
        ) and not success_flag:
            success_flag = True
            to_sale_young, sum_per_young, coverage_amount_young = self.coverage_amount_young(
                cnt_young_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_young
            to_sale_old, sum_per_old, coverage_amount_old = self.coverage_amount_old(
                cnt_old_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_old
            to_sale_adult, sum_per_adult, coverage_amount_adult = self.coverage_amount_adult(
                cnt_adult_next_year, coverage_amount
            )

        elif (cnt_old_next_year - self.cnt_old) > max(
                (cnt_adult_next_year - self.cnt_adult),
                (cnt_young_next_year - self.cnt_young),
                1
        ) and not success_flag:
            success_flag = True
            to_sale_young, sum_per_young, coverage_amount_young = self.coverage_amount_young(
                cnt_young_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_young
            to_sale_adult, sum_per_adult, coverage_amount_adult = self.coverage_amount_adult(
                cnt_adult_next_year, coverage_amount
            )

            coverage_amount += coverage_amount_adult
            to_sale_old, sum_per_old, coverage_amount_old = self.coverage_amount_old(
                cnt_old_next_year, coverage_amount
            )

        if not success_flag:
            to_sale_young, to_sale_adult, to_sale_old = 0, 0, 0
            sum_per_young, sum_per_adult, sum_per_old = 0, 0, 0
            self.cnt_young = cnt_young_next_year
            self.cnt_adult = cnt_adult_next_year
            self.cnt_old = cnt_old_next_year

        self.random_death()
        cur_animals_info = {
            "cnt_young": to_sale_young,
            "cnt_adult": to_sale_adult,
            "cnt_old": to_sale_old,

            "sum_young": sum_per_young,
            "sum_adult": sum_per_adult,
            "sum_old": sum_per_old,
        }
        self.ans_dict["to_remainder_young"].append(max(0, self.cnt_young))
        self.ans_dict["to_remainder_adult"].append(max(0, self.cnt_adult))
        self.ans_dict["to_remainder_old"].append(max(0, self.cnt_old))

        animals_recount_info = self.recount(cur_animals_info)

        self.ans_dict["to_sale_young"].append(min(self.ans_dict["to_remainder_young"][-1], to_sale_young))
        self.ans_dict["to_sale_adult"].append(min(self.ans_dict["to_remainder_adult"][-1],to_sale_adult))
        self.ans_dict["to_sale_old"].append(min(self.ans_dict["to_remainder_old"][-1],to_sale_old))

        self.ans_dict["sum_young"].append(animals_recount_info['sum_young'])
        self.ans_dict["sum_adult"].append(animals_recount_info['sum_adult'])
        self.ans_dict["sum_old"].append(animals_recount_info['sum_old'])
        if "sum_avg" in animals_recount_info:
            self.ans_dict["forfeit"].append(animals_recount_info['sum_avg'])
        else:
            self.ans_dict["default_flag"] = True
            self.ans_dict["forfeit"].append(0)

        print(f"Sale {to_sale_young} of young animals by sum: {sum_per_young}, recount: {animals_recount_info['sum_young']}")
        print(f"Sale {to_sale_adult} of adult animals by sum: {sum_per_adult}, recount: {animals_recount_info['sum_adult']}")
        print(f"Sale {to_sale_old} of old animals by sum: {sum_per_old}, recount: {animals_recount_info['sum_old']}")
        return True

    def modeling(self, farm_info):
        self.cnt_young = farm_info["cnt_young"]
        self.cnt_adult = farm_info["cnt_adult"]
        self.cnt_old = farm_info["cnt_old"]
        self.start_sum = farm_info["start_sum"]
        self.food_cost_per_year = farm_info["food_cost_per_year"]

        self.birth_rate_adult = farm_info["birth_rate_adult"]
        self.birth_rate_old = farm_info["birth_rate_old"]
        self.survival_rate_young = farm_info["survival_rate_young"]
        self.death_rate_old = farm_info["death_rate_old"]
        self.raw_cur_sum = 0

        self.cur_sum = farm_info["cur_sum"]
        self.default_flag = farm_info["default_flag"]
        self.ans_dict = farm_info["ans_dict"]
        self.random_death_rate = farm_info["random_death_rate"]

        if not self.modeling_year():
            self.ans_dict["default_flag"] = True
        print(self.cnt_young, self.cnt_adult, self.cnt_old)
        self.ans_dict["profit"].append(self.cur_sum - self.start_sum)
        self.ans_dict["cur_sum"].append(self.raw_cur_sum)
        print("profit: ", self.cur_sum - self.start_sum)

        return self.ans_dict

