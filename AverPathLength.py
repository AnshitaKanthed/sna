import networkx as nx

def create_social_network():
    # Create an empty graph
    G = nx.Graph()

    # Ask the user for the number of nodes and edges in the network
    num_nodes = int(input("Enter the number of nodes in the social network: "))
    num_edges = int(input("Enter the number of edges in the social network: "))

    # Add nodes to the graph
    for i in range(num_nodes):
        G.add_node(i)

    # Add edges to the graph
    print("Enter the edges (as pairs of nodes, separated by space):")
    for _ in range(num_edges):
        edge = input().split()
        G.add_edge(int(edge[0]), int(edge[1]))

    return G

def main():
    # Create the social network
    social_network = create_social_network()

    # Print out the network
    print("Social network:")
    print(social_network.edges())

    # Calculate the average shortest path length
    avg_path_length = nx.average_shortest_path_length(social_network)

    print("Average path length of the social network:", avg_path_length)

if __name__ == "__main__":
    main()
