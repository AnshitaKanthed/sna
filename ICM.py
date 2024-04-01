import random

def independent_cascade_model(graph, seed_set, iterations=1000):
    influenced_nodes = set(seed_set)
    newly_influenced = set(seed_set)
    
    for _ in range(iterations):
        if len(newly_influenced) == 0:
            break
        newly_influenced_this_round = set()
        for node in newly_influenced:
            neighbors = graph.get(node, {})
            for neighbor, probability in neighbors.items():
                if neighbor not in influenced_nodes:
                    if random.random() < probability:
                        newly_influenced_this_round.add(neighbor)
        influenced_nodes.update(newly_influenced_this_round)
        newly_influenced = newly_influenced_this_round
    
    return len(influenced_nodes)

def main():
    # Taking inputs from the user
    num_nodes = int(input("Enter the number of nodes in the network: "))
    graph = {}
    for i in range(num_nodes):
        neighbors = {}
        num_neighbors = int(input(f"Enter the number of neighbors for node {i+1}: "))
        for _ in range(num_neighbors):
            neighbor, probability = map(float, input(f"Enter neighbor node and probability for node {i+1} (separated by space): ").split())
            neighbors[int(neighbor)] = probability
        graph[i+1] = neighbors
    
    seed_set = list(map(int, input("Enter the seed set (comma-separated): ").split(',')))
    
    # Calculate influence
    max_influence = 0
    for _ in range(1000):  # Run simulation multiple times to get average influence
        influence = independent_cascade_model(graph, seed_set)
        max_influence = max(max_influence, influence)
    print("Influence of the seed set:", max_influence)

if __name__ == "__main__":
    main()
