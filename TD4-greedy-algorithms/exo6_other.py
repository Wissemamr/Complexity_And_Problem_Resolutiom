from typing import Union


def knapsack_problem(data: dict, W: int = None) -> Union[dict, int]:
    selected_objects_dict = {}
    sum_weights: int = 0
    max_value = 0
    max_key = None
    sum_values = 0
    while data != {} and sum_weights + max_value <= W:
        max_value = 0
        max_key = None
        for object, obj_dict in list(data.items()):
            if obj_dict["value"] > max_value:
                max_value = obj_dict["value"]
                max_key = object

        if max_key is not None:
            # update the solution dictionary with the max element
            selected_objects_dict[max_key] = data.pop(max_key)
            sum_weights += selected_objects_dict[max_key]["weight"]
            sum_values += selected_objects_dict[max_key]["value"]

    return selected_objects_dict, sum_weights, sum_values


data: dict = {
    "A": {"value": 4, "weight": 2},
    "B": {"value": 3, "weight": 2},
    "C": {"value": 8, "weight": 5},
    "D": {"value": 5, "weight": 2},
    "E": {"value": 10, "weight": 7},
    "F": {"value": 7, "weight": 4},
    "G": {"value": 1, "weight": 1},
    "H": {"value": 7, "weight": 4},
    "I": {"value": 3, "weight": 2},
    "J": {"value": 3, "weight": 1},
    "K": {"value": 6, "weight": 4},
    "L": {"value": 12, "weight": 10},
    "M": {"value": 2, "weight": 2},
    "N": {"value": 4, "weight": 1},
}


# print(list(data.values())[0]['value'])
sol, sum_weights, sum_vals = knapsack_problem(data, W=26)
print(
    f"\nThe solution dict is : {sol} \nThe knapsack contains objects : {list(sol.keys())} \nThe sum of their weights is : {sum_weights} \nThe sum of the values is : {sum_vals} \n"
)
