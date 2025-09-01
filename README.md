# Dijkstra Algorithm Performance Comparison

This project demonstrates the **performance comparison of different implementations of Dijkstra's shortest path algorithm** on a large undirected weighted graph. The goal is to measure and compare the execution time of:

- **Custom Dijkstra without a heap (O(V²))**
- **Custom Dijkstra using a Min-Heap (Priority Queue) (O((V + E) log V))**
- **NetworkX's built-in Dijkstra implementation**

---

## ✅ Features
- Generates a **random weighted undirected graph** with configurable size and density.
- Implements **two custom versions of Dijkstra's algorithm**:
  - Without a heap (inefficient, O(V²))
  - With a heap (optimized using `heapq`)
- Uses **NetworkX's `single_source_dijkstra_path_length`** as a benchmark.
- Measures **execution time** for each method.
- Verifies that all implementations produce **identical shortest path results**.

---
## Results
- Networkx's dijkstra algorithm showed best performence among those 3 algorithms. Times are shon as follows:
- Execution time of My Dijkstra without heap: 6.717967748641968 seconds
- Execution time of My Dijkstra with using heap: 3.692349672317505 seconds
- Execution time of networkx dijkstra: 2.9202988147735596 seconds
- Outputs are same #Outputs checked with if condition if they are same.
- Networkx's dijkstra algorithm < My Dijkstra with using heap < My Dijkstra without heap
- In here we can see using heap data structure reduces the time complexity as desired.

