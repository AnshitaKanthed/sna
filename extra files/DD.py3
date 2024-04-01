import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()

# Generate the random graph
# G = nx.gnp_random_graph(10, 0.5, directed=True)
G = nx.karate_club_graph

# Plot the graph
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(G)  # Layout for the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=200, edge_color='black', linewidths=0.5)
plt.title("Random Directed Graph")

# Plot the degree distribution
plt.subplot(1, 2, 2)
plot_degree_dist(G)

plt.tight_layout()
plt.show()
