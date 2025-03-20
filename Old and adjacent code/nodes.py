#this graph represents the dice tiles on a boggle grid. The list outputted is a list of all boggle letter orders

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'C', 'E', 'F', 'G'],
    'C': ['B', 'D', 'F', 'G', 'H'],
    'D': ['C', 'G', 'H'],
    'E': ['A', 'B', 'F', 'I', 'J'],
    'F': ['A', 'B', 'C', 'E', 'G', 'I', 'J', 'K'],
    'G': ['B', 'C', 'D', 'F', 'H', 'J', 'K', 'L'],
    'H': ['C', 'D', 'G', 'K', 'L'],
    'I': ['E', 'F', 'J', 'M', 'N'],
    'J': ['E', 'F', 'G', 'I', 'K', 'M', 'N', 'O'],
    'K': ['F', 'G', 'H', 'J', 'L', 'N', 'O', 'P'],
    'L': ['G', 'H', 'K', 'O', 'P'],
    'M': ['I', 'J', 'N'],
    'N': ['I', 'J', 'K', 'M', 'O'],
    'O': ['J', 'K', 'L', 'N', 'P'],
    'P': ['K', 'L', 'P']
}

# Helper function to perform DFS
def find_paths(graph, start_node, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []
    
    path.append(start_node)  # Add the current node to the path

    # If path length exceeds 3, store it
    if len(path) > 3:
        all_paths.append(path[:])  # Store a copy of the path

    # Explore neighbors of the current node
    for neighbor in graph[start_node]:
        if neighbor not in path:  # Only visit nodes not already in the path
            find_paths(graph, neighbor, path, all_paths)

    path.pop()  # Backtrack to explore other paths

# Function to list all paths longer than 3
def list_permutations(graph):
    all_paths = []
    for node in graph:
        find_paths(graph, node, [], all_paths)
    return all_paths

# Run the function and display the results
paths = list_permutations(graph)
print("Paths longer than 3 nodes:")
print(len(paths))
#for path in paths:
#    print(path)

#Now I want to overlap this with the boggle grid and an english language dictionary