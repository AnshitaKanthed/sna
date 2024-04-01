import itertools

def l(graph, node):
    neighbors = graph[node]
    k = len(neighbors)
    if k < 2:
        return 0
    
    connected_count = 0
    triangle_count = 0
    for i, j in itertools.combinations(neighbors, 2):
        if j in graph[i]:
            connected_count += 1
            if i in graph[j]:
                triangle_count += 1
    
    if connected_count == 0:
        return 0
    return triangle_count / connected_count

def clustering_coefficient(graph):
    n = len(graph)
    if n < 3:
        return 0
    return sum(l(graph, node) for node in graph) / n

def parse_graph_input():
    graph = {}
    print("Enter the number of nodes:")
    num_nodes = int(input())
    for i in range(num_nodes):
        print(f"Enter neighbors of node {i}: (comma-separated, e.g., 1,2,3)")
        neighbors = list(map(int, input().split(',')))
        graph[i] = neighbors
    return graph

# Example usage:
print("Please enter the graph:")
graph = parse_graph_input()
coefficient = clustering_coefficient(graph)
print("Clustering Coefficient:", coefficient)
