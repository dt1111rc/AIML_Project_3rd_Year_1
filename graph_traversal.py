
import networkx as nx            # Used for creating complex network
import time                      # Gives us the current time
import psutil                    # Helps to access system details and process utilities
import uuid                      # Provides unique bit code for specific computer in order to differentiate the user's hardwork behind the designing of the program
import matplotlib.pyplot as plt    # Used for desining graph or charts


# Loading the dataset
# We assume that the dataset is in a file called "facebook_combined.txt"
R = nx.read_edgelist('/kaggle/input/facebook/facebook_combined.txt')  

# Basic information about the graph of which we are going to create a complex network

print(f"Number of nodes present: {R.N_nodes()}")
print(f"Number of edges present: {R.N_edges()}")
print(f"Graph is directed ? {R.is_directed()}")
print(f"Graph density = {nx.density(R)}")

# Declaration of values
node_initial = '0' # Example for the starting node
node_final = '100' # Example for the goal node

if node_initial not in R or node_final not in R:
  raise Error("NOT FOUND ! Please check again .")

from collections import deque    # Enqueue/Dequeue operation
def bfs(graph, INITIAL, TARGET):
  visited = set()
  queue = dequeue([(INITIAL, [INITIAL])])    # Queue of tuples(node, path)
  while queue:    # Unless value is within the queue , else out of the loop
    current_node, path = queue.popleft()
    if current_node not in visited:
      visited.add(current_node)
      for neighbor in graph.neighbors(current_node):
        if neighbor not in visited:
          new_path = list(path)
          new_path.append(neighbor)
          queue.append(neighbor,new_path)
  return None
 
path= bfs(G,'12','1000')
print("Path :", path)
def dfs(graph, INITIAL):
    stack = [(INITIAL, [INITIAL])]  
    visited = set()
    all_paths = []

    while stack:
        current_node, path = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            all_paths.append(path)  
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))
    return all_paths
path= dfs(G,'12')
p=set()
for i in path:
    p.update(i)
print("Number of nodes reachable from 12: ", len(p))

