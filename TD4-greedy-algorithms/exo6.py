# Implement the knapsakc problem using the strategy of highest value first
# w.r.t the maximum bag capacity set to W= 26

# key : letter
# values : (value, weight)
data: dict = {
    "A": (4, 2),
    "B": (3, 2),
    "C": (8, 5),
    "D": (5, 2),
    "E": (10, 7),
    "F": (7, 4),
    "G": (1, 1),
    "H": (7, 4),
    "I": (3, 2),
    "J": (3, 1),
    "K": (6, 4),
    "L": (12, 10),
    "M": (2, 2),
    "N": (4, 1),
}


def knapsack_problem(data: dict, W: int = None) -> dict:
    solution = {}
    weights = []
    for object, vw in data.items():
        # print(object,'->' ,vw)
        values_ = list(data[object].values())[vw]
        return values_


values_ = list(data.values())
print(values_)

for object, vw in data.items():
    # print(list(data.values())[0][0])
    # values_ = list(data[object])[0]
    pass
