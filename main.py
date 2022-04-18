from modeling import Modeling
from graph import Graph

# start graph

start_info = {
    "cnt_young": 70,
    "cnt_adult": 90,
    "cnt_old": 85,

    "food_cost_per_year": 1000,
    "start_sum": 100000,
}

farm_info = {
    "birth_rate_adult": 0.8,
    "birth_rate_old": 0.5,
    "survival_rate_young": 0.95,
    "death_rate_old": 0.3,
}

main_graph = Graph()
start_info = main_graph.run_start_graph()

main_model = Modeling(start_info, farm_info)
modeling_ans_info = main_model.modeling(6)

main_graph.run_contract_graph(modeling_ans_info)
