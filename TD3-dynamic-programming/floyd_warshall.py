"""
NOTE : 
This directed work is about dynamic programming
Exercise 01 : FLOYD'S ALGORITHM IMPLEMENTATION
Exercise 02 :  NUMBER'S PYRAMID

"""
DEBUG: bool = True

# nodes = vertices


def Floyd_Warshall(graph: dict):
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    if DEBUG:
        print(f"THE GRAPH NODES : {nodes}")

    dist = []

    for i in range(num_nodes):
        row = []
        for j in range(num_nodes):
            if i != j:
                row.append(float("inf"))
            else:
                row.append(0)
        dist.append(row)

    if DEBUG:
        print(f"THE DISTANCE MAT : {dist} ")
    # Update the dist mat
    for i in range(num_nodes):
        for neighbor in graph[nodes[i]]:
            j, weight = neighbor
            dist[i][nodes.index(j)] = weight

    # Perform the FW
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                # if there is a shorter path from i to j through  intermediate node k
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example usage
if __name__ == "__main__":
    graph = {0: [(1, 3), (2, 7)], 1: [(0, 3), (2, 1)], 2: [(0, 7), (1, 1)]}
    result = Floyd_Warshall(graph)
    print(f"The best way is :{result}")
    for row in result:
        print(row)
