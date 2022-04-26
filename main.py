from start import StartWindow
from interface import Interface
from animal import Animal
from weather import Weather
from farm import Farm
from modeling import Modeling
from сontract import Contract


start_window_object = StartWindow()
interface_object = Interface()
modeling_object = Modeling()
farm_object = Farm()

start_window = start_window_object.create_start_window()
interface_status = interface_object.show_window(start_window)
print(interface_status)

if interface_status < 0:
    exit(0)

while True:
    if interface_status < 1:
        break

    elif interface_status == 1:
        user_animal_values, user_weather_values = interface_object.get_user_start_result()
        print("user_animal_values", user_animal_values)
        animal_object = Animal(user_animal_values)
        weather_object = Weather(user_weather_values)

        animal_info = animal_object.pack_data_to_farm()
        weather_info = weather_object.pack_data_to_farm()
    elif interface_status == 2:
        user_animal_values = interface_object.get_user_animal_result()

        animal_object = Animal(user_animal_values)
        animal_info = animal_object.pack_data_to_farm()
    else:
        break

    farm_info = farm_object.pack_data_to_modeling(animal_info, weather_info)
    contract_info = modeling_object.modeling(farm_info)

    contract_object = Contract(contract_info)
    contract_window = contract_object.create_contract_window()

    interface_status = interface_object.show_window(contract_window)
