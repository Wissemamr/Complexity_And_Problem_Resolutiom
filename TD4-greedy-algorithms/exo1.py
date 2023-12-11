""" Get max of the list
objective : maxmimise the sum of elemets
constraint : not append an element that's adjacent to any of the rpevious elements 
"""


def get_solution_set(inp_list: list) -> set:
    pass


def verify_adjacent_elem(inp_list: list) -> bool:
    for i in inp_list:
        pass


def get_elem_sum(inp_list: list) -> int | float:
    return sum(inp_list)


if __name__ == "__main__":
    inp_list = [15, 4, 20, 17, 11, 8, 11, 16, 7, 14, 2, 7, 5, 17, 19, 18, 4, 5, 13, 8]


best_solution = get_solution_set(inp_list=inp_list)
print(f"The solution set is : {best_solution}")
