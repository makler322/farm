import PySimpleGUI as sg


class Contract:
    def __init__(self, result_from_modeling):
        self.result_from_modeling = result_from_modeling
        # sg.theme(theme_color)  # Add a touch of color
        self.close_event = sg.WIN_CLOSED

    def ans_layout_create(self, ind=0):

        # print("result_from_modeling -> ", self.result_from_modeling)
        layout_to_draw = [
            # """
            # Приложение говорит, что сейчас:
            #     голов молодняка
            #     ...
            # Если это так, то рекомендуется продать
            #     голов молодняка по цене
            #
            # Также стоит закупить корма на сумму
            #
            # Ваша прибыль с прошлого года составила
            # Итого общий капитал
            #
            # Смоделировать год работы фермы     закончить
            # """
            [sg.Text("Приложение говорит, что сейчас:")],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_remainder_young"][ind]}""",
                             key='farm_remainder_young'),
                sg.Text(f"""голов молодняка""")
            ],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_remainder_adult"][ind]}""",
                             key='farm_remainder_adult'),
                sg.Text(f"""голов взрослых животных""")
            ],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_remainder_old"][ind]}""",
                             key='farm_remainder_old'),
                sg.Text(f"""голов старых животных""")
            ],
            [sg.Text(
                f"""На следующий год рекомендуется купить корма на сумму {self.result_from_modeling["food_cost"][ind]} у.е. \n""")],
            [sg.Text(f"""Рекомендовано к продаже:""")],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_sale_young"][ind]}""",
                             key='farm_to_sale_young'),
                sg.Text(f"""голов молодняка по цене не ниже"""),
                sg.InputText(default_text=f"""{self.result_from_modeling["sum_young"][ind]}""",
                             key='farm_sum_young'),
            ],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_sale_adult"][ind]}""",
                             key='farm_to_sale_adult'),
                sg.Text(f"""голов взрослых животных по цене не ниже"""),
                sg.InputText(default_text=f"""{self.result_from_modeling["sum_adult"][ind]}""",
                             key='farm_sum_adult'),
            ],
            [
                sg.InputText(default_text=f"""{self.result_from_modeling["to_sale_old"][ind]}""",
                             key='farm_to_sale_old'),
                sg.Text(f"""голов старых животных по цене не ниже"""),
                sg.InputText(default_text=f"""{self.result_from_modeling["sum_old"][ind]}""",
                             key='farm_sum_old'),
            ],
            [sg.Text(f"""Ожидаемая прибыль на следующий год: {int(self.result_from_modeling["profit"][ind])}""")],
            [
                sg.Text("Остаток средств без учёта прибыли:"),
                sg.InputText(default_text=f"""{self.result_from_modeling["cur_sum"][ind]}""",
                             key='farm_start_sum'),
            ],
            [
                sg.Button('Смоделировать год работы фермы', button_color=('#F0F0F0', '#FF4343'),
                          border_width=1, key='result_key', font=("Helvetica", 12)),
                sg.Button('Закончить', button_color=('#F0F0F0', '#FF4343'),
                          border_width=1, key="end", font=("Helvetica", 12)),
            ],
        ]

        return layout_to_draw

    def create_contract_window(self):
        if self.result_from_modeling["default_flag"]:
            layout = [
                [sg.Text(f"""К сожалению, такое распределение бюджета \n
приведёт к банкротству фермы.
""", font=("Helvetica", 12))],
                [
                    sg.Button('Закончить', button_color=('#F0F0F0', '#FF4343'),
                              border_width=1, key="end", font=("Helvetica", 12)),
                ],
            ]
        else:
            layout = [
                [sg.Frame(f'Результат моделирования', self.ans_layout_create(), font=("Helvetica", 12))],
            ]

        window = sg.Window('Весёлая ферма', layout)
        return window
