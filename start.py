import PySimpleGUI as sg


class StartWindow:
    def __init__(self, theme_color='Purple'):
        sg.theme(theme_color)  # Add a touch of color
        self.close_event = sg.WIN_CLOSED

    def create_animal_layout(self):
        young_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(default_text="70", key='farm_cnt_young')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_young')]
        ]

        adult_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(default_text="90", key='farm_cnt_adult')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_adult')]
        ]

        old_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(default_text="85", key='farm_cnt_old')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_old')]
        ]

        animals_layout = [
            [sg.Frame('Молодые', young_animal_layout, font=("Helvetica", 20))],
            [sg.Frame('Взрослые', adult_animal_layout, font=("Helvetica", 20))],
            [sg.Frame('Старые', old_animal_layout, font=("Helvetica", 20))],
        ]

        return animals_layout

    def create_weather_layout(self):
        rates_info = [
            [sg.Text('Коэффициент рождаемости у взрослых '), sg.InputText(default_text="0.8", key='birth_rate_adult')],
            [sg.Text('Коэффициент рождаемости у старых '), sg.InputText(default_text="0.5", key='birth_rate_old')],
            [sg.Text('Коэффициент выживаемости у молодняка '), sg.InputText(default_text="0.95", key='survival_rate_young')],
            [sg.Text('Коэффициент выживаемости у старых '), sg.InputText(default_text="0.3", key='death_rate_old')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_young')]
        ]

        # weather_layout = [
        #     [sg.Frame('Погодные условия', rates_info, font=("Helvetica", 20))],
        # ]

        return rates_info

    def create_start_window(self):
        capital_layout = [
            [sg.InputText(default_text="100000", key='farm_start_sum')],
        ]
        food_layout = [
            [sg.InputText(default_text="1000", key='food_cost_per_year')],
        ]
        animals_layout = self.create_animal_layout()
        weather_layout = self.create_weather_layout()

        layout = [
            [
                sg.Frame('Животные', animals_layout, font=("Helvetica", 20)),
                sg.VSeperator(),
                sg.Frame('Погодные условия', weather_layout, font=("Helvetica", 20))
            ],

            [sg.Frame('Текущий капитал', capital_layout, font=("Helvetica", 20))],
            [sg.Frame('Стоимость корма необходимого взорслому животному в течении года', food_layout,
                      font=("Helvetica", 20))],
            [
                sg.Button('Смоделировать год работы фермы', button_color=('#F0F0F0', '#FF4343'),
                          border_width=1, key='result_key', font=("Helvetica", 12)),
                sg.Button('Закончить', button_color=('#F0F0F0', '#FF4343'),
                          border_width=1, key="end", font=("Helvetica", 12)),
            ],
        ]

        window = sg.Window('Весёлая ферма', layout)
        return window

    # def show_window(self, window):
    #     while True:
    #         event, values = window.read()
    #         if event == self.close_event or event == 'result_key':
    #             print('You entered ', values)
    #             break
    #
    #     window.close()
    #     return values

    # def run_start_graph(self):
    #     window = self.create_start_window()
    #     values_result = self.show_window(window)
    #     for item in values_result.items():
    #         key, value = item
    #         values_result[key] = int(value)
    #     return values_result
    #
    # def run_contract_graph(self, result_from_modeling):
    #     window = self.create_contract_window(result_from_modeling)
    #     return self.show_window(window)
