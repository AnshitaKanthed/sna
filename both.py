import random

class Graph:
    def __init__(self):
        self.nodes = {}  # Node ID to set of neighboring node IDs

    def add_edge(self, node1, node2):
        self.nodes.setdefault(node1, set()).add(node2)
        self.nodes.setdefault(node2, set()).add(node1)

    def simulate_independent_cascade(self, seed_set):
        influenced_nodes = set(seed_set)  # Start with the seed set as influenced nodes
        queue = list(seed_set)  # Initialize queue with seed set

        while queue:
            current_node = queue.pop(0)  # Get the first node in the queue
            neighbors = self.nodes.get(current_node, set())
            for neighbor in neighbors:
                # Check if the neighbor is not already influenced and if influence spreads
                if neighbor not in influenced_nodes and random.random() < 0.5:
                    influenced_nodes.add(neighbor)
                    queue.append(neighbor)

        return influenced_nodes

    def simulate_linear_threshold(self, seed_set):
        influenced_nodes = set(seed_set)  # Start with the seed set as influenced nodes
        active_nodes = set(seed_set)  # Start with the seed set as active nodes

        while active_nodes:
            current_node = active_nodes.pop()  # Get an active node
            neighbors = self.nodes.get(current_node, set())
            total_weight = len(neighbors)
            influenced_weight = sum(1 for neighbor in neighbors if neighbor in influenced_nodes)

            threshold = random.random()  # Generate a random threshold

            # If the influenced weight is greater than or equal to the threshold, activate the node
            if influenced_weight / total_weight >= threshold:
                influenced_nodes.add(current_node)

                # Add neighbors to the active set if not already influenced
                for neighbor in neighbors:
                    if neighbor not in influenced_nodes:
                        active_nodes.add(neighbor)

        return influenced_nodes


# Create a new empty graph
graph = Graph()

# Add edges to create the desired connections
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)

seed_set = {1}  # Define the seed set

# Simulate influence spread using Independent Cascade Model
influenced_nodes_independent_cascade = graph.simulate_independent_cascade(seed_set)
print("Influenced nodes using Independent Cascade Model:", influenced_nodes_independent_cascade)

# Simulate influence spread using Linear Threshold Model
influenced_nodes_linear_threshold = graph.simulate_linear_threshold(seed_set)
print("Influenced nodes using Linear Threshold Model:", influenced_nodes_linear_threshold)
