import PySimpleGUI as sg


class Interface:
    def __init__(self):
        self.close_event = sg.WIN_CLOSED
        self.result_animal_values = {}
        self.result_weather_values = {}

    def show_window(self, window):
        while True:
            event, values = window.read()
            if event == "end" or event == self.close_event:
                return -1
            if event == 'result_key':
                break

        window.close()
        if not values:
            return 0
        self.result_animal_values = {}
        self.result_weather_values = {}
        for item in values.items():
            key, value = item
            if "farm" in key:
                self.result_animal_values[key] = int(float(value))
            else:
                self.result_weather_values[key] = float(value)
        if len(self.result_weather_values) == 0:
            return 2
        return 1

    def get_user_start_result(self):
        return self.result_animal_values, self.result_weather_values

    def get_user_animal_result(self):
        ans_dict = {
            "farm_start_sum": self.result_animal_values["farm_start_sum"] +
                              self.result_animal_values["farm_to_sale_young"] * self.result_animal_values[
                                  "farm_sum_young"] +
                              self.result_animal_values["farm_to_sale_adult"] * self.result_animal_values[
                                  "farm_sum_adult"] +
                              self.result_animal_values["farm_to_sale_old"] * self.result_animal_values[
                                  "farm_sum_old"]
            ,
            "farm_cnt_young": self.result_animal_values["farm_remainder_young"] - self.result_animal_values[
                "farm_to_sale_young"],
            "farm_cnt_adult": self.result_animal_values["farm_remainder_adult"] - self.result_animal_values[
                "farm_to_sale_adult"],
            "farm_cnt_old": self.result_animal_values["farm_remainder_old"] - self.result_animal_values[
                "farm_to_sale_old"],
        }
        return ans_dict
