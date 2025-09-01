import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time
import random

# Fix seed for reproducibility
random.seed(42)

# Create graph
G = nx.Graph()
num_nodes = 10000
G.add_nodes_from(range(num_nodes))  # Nodes: 0, 1, 2, ..., 99

# Add random weighted edges (sparse graph, ~10% chance of an edge)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < 0.1:  # Adjust for density (0.1 = 10% chance)
            weight = random.randint(1, 20)
            G.add_edge(i, j, weight=weight)

print(f"Graph created with {len(G.nodes())} nodes and {len(G.edges())} edges.")

# Step 2: Implement Dijkstra manually
def dijkstra_with_heap(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]  # priority queue (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Dijkstra without heap
def dijkstra_no_heap(graph, start):
    nodes = list(graph.nodes())
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    visited = set()

    while len(visited) < len(nodes):
        # Find the unvisited node with the smallest distance
        min_node = None
        min_distance = float('inf')
        for node in nodes:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        if min_node is None:  # No more reachable nodes
            break

        visited.add(min_node)

        for neighbor in graph.neighbors(min_node):
            weight = graph[min_node][neighbor]['weight']
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Measure time of My Dijkstra algorithm without heap
start_time = time.time()
shortest_paths1 = dijkstra_no_heap(G, 0)
end_time = time.time()
print("Execution time of My Dijkstra without heap:", end_time - start_time, "seconds")

# Measure time of My Dijkstra algorithm with using heap
start_time = time.time()
shortest_paths2 = dijkstra_with_heap(G, 0)  # Start from node 0
end_time = time.time()
print("Execution time of My Dijkstra with using heap:", end_time - start_time, "seconds")

# Measure time of My Dijkstra algorithm with using heap
start_time = time.time()
shortest_paths3 = nx.single_source_dijkstra_path_length(G, source=0)
end_time = time.time()
print("Execution time of networkx dijkstra:", end_time - start_time, "seconds")

#Checking if the outputs are same. It is necessery to see we find the optimal(shortest) paths.
if shortest_paths1 == shortest_paths3 and shortest_paths2 == shortest_paths3:
    print("Outputs are same")
