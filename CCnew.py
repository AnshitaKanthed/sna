import itertools

def local_clustering_coefficient(graph, node):
    # Get the neighbors of the node
    neighbors = graph[node]
    # Get the degree of the node
    k = len(neighbors)
    if k < 2: #If the node has fewer than 2 neighbors , 
        return 0 # means there are not enough neighbors to form triangles, so local clustering coefficient is 0.
    
    connected_count = 0
    triangle_count = 0
    # Iterate over all pairs of neighbors
    for i, j in itertools.combinations(neighbors, 2): 
         # Check if there's a connection between the pair
        if j in graph[i]:
            connected_count += 1
            # Check if there's a triangle formed
            if i in graph[j]:
                triangle_count += 1
    
    if connected_count == 0:
        return 0
    # Calculate local clustering coefficient
    return triangle_count / connected_count

def clustering_coefficient(graph):
    # Get the number of nodes in the graph
    n = len(graph)
    if n < 3:
        return 0
    # Calculate the average clustering coefficient for the whole graph
    return sum(local_clustering_coefficient(graph, node) for node in graph) / n

def parse_graph_input():
    graph = {}
    # Get the number of nodes in the graph
    print("Enter the number of nodes:")
    num_nodes = int(input())
    for i in range(num_nodes):
        # Get neighbors of the current node from user input
        print(f"Enter neighbors of node {i}: (comma-separated, e.g., 1,2,3)")
        neighbors = list(map(int, input().split(',')))
        graph[i] = neighbors
    return graph

# Example usage:
print("Please enter the graph:")
graph = parse_graph_input()
coefficient = clustering_coefficient(graph)
print("Clustering Coefficient:", coefficient)
