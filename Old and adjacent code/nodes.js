// Example graph represented as an adjacency list
const graph = {
    A: ['B', 'C', 'D'],
    B: ['A', 'E', 'F'],
    C: ['A', 'G', 'H'],
    D: ['A'],
    E: ['B'],
    F: ['B'],
    G: ['C'],
    H: ['C']
};

// Helper function to perform DFS
function findPaths(graph, startNode, path = [], allPaths = []) {
    path.push(startNode); // Add current node to the path

    // If path length exceeds 3, store it
    if (path.length > 3) {
        allPaths.push([...path]);
    }

    // Explore neighbors of the current node
    for (let neighbor of graph[startNode]) {
        // Only visit the neighbor if it's not already in the path
        if (!path.includes(neighbor)) {
            findPaths(graph, neighbor, path, allPaths);
        }
    }

    path.pop(); // Backtrack to explore other paths
}

// Function to list all paths longer than 3
function listPermutations(graph) {
    const allPaths = [];
    for (let node in graph) {
        findPaths(graph, node, [], allPaths);
    }
    return allPaths;
}

// Run the function and log the results
const paths = listPermutations(graph);
console.log("Paths longer than 3 nodes:", paths);
