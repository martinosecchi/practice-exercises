
const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: [],
}

/**
 * Return a string with the graph nodes concatenated in Depth First Search order.
 */
const concatDFS = (graph, node) => {
    let nodeStr = node;
    for (let neighbor of graph[node]) {
        nodeStr = nodeStr + concatDFS(graph, neighbor);
    }
    return nodeStr
}

console.log(concatDFS(graph, "a") == "abdfce");


/**
 * Return a string with the graph nodes concatenated in Breadth First Search order.
 */
const concatBFS = (graph, node) => {
    const queue = [node];
    let nodeStr = "";
    while (queue.length > 0) {
        const current = queue.shift();
        nodeStr += current;
        for (let neighbor of graph[current]){
            queue.push(neighbor);
        }
    }
    return nodeStr;
}

console.log(concatBFS(graph, "a") == "abcdef");


/**
 * Return true if there is a path between the source node and the destination node.
 * Assume the input graph is acyclic and directed.
 */
const hasPath = (graph, source, dest) => {
    if (source == dest) return true;
    for (const neighbor of graph[source]){
        if (hasPath(graph, neighbor, dest)){
            return true;
        };
    }
    return false;
}


// acyclic directed graph
const directedGraph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: [],
}
console.log(hasPath(directedGraph, "f", "k") == true)
console.log(hasPath(directedGraph, "j", "k") == true)
console.log(hasPath(directedGraph, "i", "h") == true)
console.log(hasPath(directedGraph, "f", "j") == false)
console.log(hasPath(directedGraph, "g", "k") == false)


/**
 * Convert an edge list into an undirected adjacency list
 */
const buildGraphFromUndirectedEdges = (undirectedEdges) => {
    const graph = {};
    for (const edge of undirectedEdges){
        const [node1, node2] = edge
        if (!(node1 in graph)) graph[node1] = [];
        if (!(node2 in graph)) graph[node2] = [];
        
        graph[node1].push(node2);
        graph[node2].push(node1);
    }
    return graph;
}

/**
 * Given a (possibly cyclic) undirected graph, return true if there is a path
 * between the source node and the destination.
 */
const hasUndirectedPath = (edges, source, dest) => {
    
    const hasDFSPath = (graph, src, dst, visited = {}) => {
        if (src in visited) return false;
        if (src == dst) return true;

        visited[src] = true;
        for (const neighbor of graph[src]){
            if (hasDFSPath(graph, neighbor, dst, visited)){
                return true;
            }
        }
        return false;
    }

    const graph = buildGraphFromUndirectedEdges(edges);
    return hasDFSPath(graph, source, dest);

}

const edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
    ["k", "j"],  // cycle edge
];

console.log(hasUndirectedPath(edges, "i", "l") == true)
console.log(hasUndirectedPath(edges, "i", "m") == true)
console.log(hasUndirectedPath(edges, "m", "j") == true)
console.log(hasUndirectedPath(edges, "i", "n") == false)


/**
 * Count how many separate connected components are in the given graph.
 */
const connectedComponentCount = (graph) => {

    const explore = (node, visited) => {
        if (visited.has(node)) return;
        visited.add(node);
        for(const neighbor of graph[node]){
            explore(neighbor, visited);
        }
    }

    const visited = new Set();
    let count = 0;
    for (const nodeName in graph){
        const node = parseInt(nodeName);
        if (visited.has(node)) continue;
        explore(node, visited)
        count += 1;
    }
    return count;
}

const disconnectedGraph = {
    1: [2],
    2: [1],
    3: [],
    4: [6],
    5: [6],
    6: [4, 5, 7, 8],
    7: [6],
    8: [6],
}

console.log(connectedComponentCount(disconnectedGraph) == 3);


/**
 * Return the number of nodes in the largest connected component of the graph.
 */
const largestComponent = (graph) => {

    const countComponent = (graph, node, visited) => {
        if (visited.has(node)) return 0;
        visited.add(node);
        let count = 1;
        for (const neighbor of graph[node]) {
            count += countComponent(graph, neighbor, visited)
        }
        return count;
    }

    const visited = new Set();
    let largestCount = 0;
    for (const nodeKey in graph){
        const node = parseInt(nodeKey);
        const componentCount = countComponent(graph, node, visited);
        if (componentCount > largestCount){ 
            largestCount = componentCount;
        }
    }

    return largestCount;
}

const largeDisconnectedGraph = {
    0: [8, 1, 5],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
    5: [0, 8],
    6: [],
    7: [],
    8: [0, 5],
}

console.log(largestComponent(largeDisconnectedGraph) == 4)


/**
 * Return the shortest path in number of edges (unweighted) between node a and node b
 */
const shortestPathDFS = (edges, a, b) => {

    const MAX = edges.length;

    const getShortest = (graph, source, dest, visited) => {
        if (visited.has(source)) return MAX;
        if (source == dest) return 0;

        visited.add(source);
        let shortest = MAX;
        for (let neighbor of graph[source]){
            const path = 1 + getShortest(graph, neighbor, dest, visited);
            if (path < shortest) shortest = path;
        }
        return shortest;
    }

    const visited = new Set();
    const graph = buildGraphFromUndirectedEdges(edges);
    return getShortest(graph, a, b, visited);
}


const shortestPathBFS = (edges, source, dest) => {
    const visited = new Set();
    const graph = buildGraphFromUndirectedEdges(edges);
    const queue = [[source, 0]];
    while (queue.length > 0){
        const [current, path] = queue.shift();

        if (visited.has(current)) continue;
        visited.add(current);

        if (current == dest) return path;

        for (const neighbor of graph[current]){
            queue.push([neighbor, path + 1]);
        }

    }
    return -1; 
}

const pathEdges = [
    ['w', 'x'],
    ['y', 'x'],
    ['y', 'z'],
    ['v', 'z'],
    ['v', 'w'],
];

console.log(shortestPathDFS(pathEdges, 'w', 'z') == 2);
console.log(shortestPathBFS(pathEdges, 'w', 'z') == 2);


/**
 * Count the number of separate islands in a grid where each cell is either land or water.
 * An island is a vertically or horizontally connected region of land.
 */
const islandCount = (grid) => {

    const LAND = "L";
    const WATER = "W";
    const n = grid.length;
    const m = n > 0 ? grid[0].length : 0;

    const explore = (grid, i, j, visited) => {
        const iOutOfBound = i < 0 || i >= n;
        const jOutOfBound = j < 0 || j >= m;
        if (iOutOfBound || jOutOfBound) return false;
        if (grid[i][j] == WATER) return false;
        if (visited[i][j]) return false;

        visited[i][j] = true;
        explore(grid, i - 1, j, visited)
        explore(grid, i + 1, j, visited)
        explore(grid, i, j - 1, visited)
        explore(grid, i, j + 1, visited)
        return true
    }

    const visited = grid.map(row => row.map(c => false));
    let count = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {            
            if (!visited[i][j] && grid[i][j] == LAND) {
                explore(grid, i, j, visited);
                count++;
            } 
        }
    }
    return count;
}

const W = "W";
const L = "L";
const grid = [
    [W, L, W, W, W],
    [W, L, W, W, W],
    [W, W, W, L, W],
    [W, W, L, L, W],
    [L, W, W, L, L],
    [L, L, W, W, W],
]

console.log(islandCount(grid) == 3);


/**
 * Return the size of the smallest island.
 */
const minimumIsland = (grid) => {

    const LAND = "L";
    const WATER = "W";
    const n = grid.length;
    const m = n > 0 ? grid[0].length : 0;

    const measureIsland = (grid, i, j, visited) => {
        const iOutOfBound = i < 0 || i >= n;
        const jOutOfBound = j < 0 || j >= m;
        if (iOutOfBound || jOutOfBound) return 0;
        if (grid[i][j] == WATER) return 0;
        if (visited[i][j]) return 0;

        visited[i][j] = true;
        let size = 1;
        size += measureIsland(grid, i - 1, j, visited);
        size += measureIsland(grid, i + 1, j, visited);
        size += measureIsland(grid, i, j - 1, visited);
        size += measureIsland(grid, i, j + 1, visited);
        return size
    }

    const visited = grid.map( row => row.map( c => false));
    let smallestIsland = n * m;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (!visited[i][j] && grid[i][j] == LAND){
                const islandSize = measureIsland(grid, i, j, visited)
                if (islandSize < smallestIsland){ 
                    smallestIsland = islandSize;
                }
            }
        }        
    }
    return smallestIsland;
}

console.log(minimumIsland(grid) == 2);
