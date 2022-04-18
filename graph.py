import PySimpleGUI as sg


class Graph:
    def __init__(self, theme_color='Purple'):
        sg.theme(theme_color)  # Add a touch of color
        self.close_event = sg.WIN_CLOSED

    def create_start_window(self):

        capital_layout = [
            [sg.InputText(key='start_sum')],
        ]

        food_layout = [
            [sg.InputText(key='food_cost_per_year')],
        ]

        young_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(key='cnt_young')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_young')]
        ]

        adult_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(key='cnt_adult')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_adult')]
        ]

        old_animal_layout = [
            [sg.Text('Количество   '), sg.InputText(key='cnt_old')],
            # [sg.Text('Цена продажи'), sg.InputText(key='cost_old')]
        ]

        animals_layout = [
            [sg.Frame('Молодые', young_animal_layout, font=("Helvetica", 20))],
            [sg.Frame('Взрослые', adult_animal_layout, font=("Helvetica", 20))],
            [sg.Frame('Старые', old_animal_layout, font=("Helvetica", 20))],
        ]

        layout = [
            [sg.Frame('Животные', animals_layout, font=("Helvetica", 20))],
            [sg.Frame('Текущий капитал', capital_layout, font=("Helvetica", 20))],
            [sg.Frame('Стоимость корма необходимого взорслому животному в течении года', food_layout,
                      font=("Helvetica", 20))],
            [sg.Button('Рассчитать идеальный контракт', button_color=('#F0F0F0', '#FF4343'),
                       border_width=1, key='result_key', font=("Helvetica", 12))],
        ]

        window = sg.Window('', layout)
        return window

    def ans_layout_create(self, ind, result_from_modeling):
        layout_to_draw = [
            [sg.Text(f"""Товарная биржа обязуется \n 
продать корма на сумму {result_from_modeling["food_cost"][ind]} у.е. \n""")],
            [sg.Text(f"""Владелец фермы обязуется продать: \n
{result_from_modeling["to_sale_young"][ind]} голов молодняка по цене не ниже {result_from_modeling["sum_young"][ind]} у.е. \n
{result_from_modeling["to_sale_adult"][ind]} голов взрослых животных по цене не ниже {result_from_modeling["sum_adult"][ind]} у.е. \n
{result_from_modeling["to_sale_old"][ind]} голов старых животных по цене не ниже {result_from_modeling["sum_old"][ind]} у.е. \n 
            """)],
            [sg.Text(f"""В случае невыполнения обязательств \n 
владелец обязан выплатить неустойку в размере \n 
не более {result_from_modeling["forfeit"][ind]} у.е. за каждое непроданное животное""")],
            [sg.Text(f"""\nДоход владельца фермы составит {result_from_modeling["profit"][ind]} у.е.""")],
        ]

        return layout_to_draw

    def create_contract_window(self, result_from_modeling):
        if result_from_modeling["default_flag"]:
            layout = [
                [sg.Text(f"""К сожалению, стартового капитала \n
недостаточно для оптимального контракта\n
Попробуйте накопить больше денег для\n
взаимодействия с товарной биржей
""", font=("Helvetica", 12))]
            ]
        else:
            layout = [
                [sg.Frame(f'Первый год', self.ans_layout_create(0, result_from_modeling), font=("Helvetica", 12)),
                 sg.VSeperator(),
                 sg.Frame(f'Второй год', self.ans_layout_create(1, result_from_modeling), font=("Helvetica", 12))],

                [sg.Frame(f'Третий год', self.ans_layout_create(2, result_from_modeling), font=("Helvetica", 12)),
                 sg.VSeperator(),
                 sg.Frame(f'Четвёртый год', self.ans_layout_create(3, result_from_modeling), font=("Helvetica", 12))],

                [sg.Frame(f'Пятый год', self.ans_layout_create(4, result_from_modeling), font=("Helvetica", 12)),
                 sg.VSeperator(),
                 sg.Frame(f'Шестой год', self.ans_layout_create(5, result_from_modeling), font=("Helvetica", 12))],
            ]

        window = sg.Window('', layout)
        return window

    def show_window(self, window):
        while True:
            event, values = window.read()
            if event == self.close_event or event == 'result_key':
                print('You entered ', values)
                break

        window.close()
        return values

    def run_start_graph(self):
        window = self.create_start_window()
        values_result = self.show_window(window)
        for item in values_result.items():
            key, value = item
            values_result[key] = int(value)
        return values_result

    def run_contract_graph(self, result_from_modeling):
        window = self.create_contract_window(result_from_modeling)
        return self.show_window(window)
