from collections import defaultdict, deque

# Function to represent a graph as an adjacency list
def build_graph(edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    
    return graph

# Function to perform Breadth First Search
def bfs(graph, start):
    distances = {}
    visited = set()
    queue = deque([(start, 0)])  # (node, distance)
    
    visited.add(start)
    
    while queue:
        node, dist = queue.popleft()
        distances[node] = dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)
    
    return distances

# Function to calculate average path length of the graph
def average_path_length(graph):
    total_length = 0
    num_nodes = len(graph)
    
    for node in graph:
        distances = bfs(graph, node)
        total_length += sum(distances.values())
    
    # Divide total path length by number of node pairs to get average path length
    return total_length / (num_nodes * (num_nodes - 1))

if __name__ == "__main__":
    # Example graph represented by its edges
    edges = [
    (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5)
]

    graph = build_graph(edges)
    
    # Print the graph
    print("Graph:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    
    # Calculate the average path length
    avg_length = average_path_length(graph)
    
    # Write the average path length to a file
    with open("output/AveragePathLen-output.txt", "a") as file:
        file.write(f"Average Path Length: {avg_length:.2f}\n")
    
    print(f"\nAverage Path Length: {avg_length:.2f}")
