### graph.py
### an implementation of a graph using an adjacency list.

## helper class representing a node in a graph. For the moment, nodes
## only have names. Later, we will add state variables.
import sys


class Node():
    def __init__(self, n):
        self.name = n
        self.parent = 0

    def __hash__(self):
        return hash(self.name)


### an edge is a link between two nodes. Right now, the only other
### information an edge carries is the weight of the link. Later we
### will add other annotations.

class Edge():
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


### The graph class itself.
### The nodeTable is a dictionary that maps names to Node objects.
### (this keeps us from having to repeatedly search edgeMap.keys())

### The edgeMap is a dictionary that maps nodes to lists of Edges emanating from that node.

class Graph():

    def __init__(self):
        self.nodeTable = {}
        self.edgeMap = {}

    ### implements the 'in' keyword. Returns true if the node is in the graph.
    def __contains__(self, item):
        return item in self.nodeTable

    def getNode(self, src):
        return self.nodeTable[src]

    def addNode(self, src):
        if src not in self.nodeTable:
            self.nodeTable[src] = Node(src)

    def addEdge(self, src, dest, weight):
        e = Edge(src, dest, weight)
        self.addNode(src)
        self.addNode(dest)
        if src in self.edgeMap:
            self.edgeMap[src].append(e)
        else:
            self.edgeMap[src] = [e]

    ## Assume file is in the mtx format: % is a comment
    ## Otherwise it's source destination weight
    ### The file in the github repo will work as a sample for you.
    ### It's in the format: source, vertex, weight. You should assume that the graph is symmetric -
    ### if there's an edge from a to b, there's an edge from b to a.
    ### You can find lots of others here: http://networkrepository.com/index.php
    def readFromFile(self, fname):
        with open(fname) as f:
            for line in f.readlines():
                if not line.startswith("%"):
                    (s, d, w) = line.split()
                    self.addEdge(s, d, w)
                    self.addEdge(d, s, w)

    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using breadth-first search.

    def breadthFirstSearch(self, startNode, endNode):
        if self.__contains__(startNode) and self.__contains__(endNode):
            ### keep track of visited nodes
            visited = [False] * (len(self.nodeTable) + 1)

            ### this is the list of the bfs path
            bfs = []

            ### this is the queue im gonna use to see which node i will visit
            queue = [startNode]
            node = startNode

            while node != endNode:
                edges = self.edgeMap.get(node)
                for edge in edges:
                    if not visited[int(edge.dest)]:
                        queue.append(edge.dest)
                        self.getNode(edge.dest).parent = node
                        visited[int(edge.dest)] = True
                node = queue.pop(0)

            node = self.getNode(node)
            while node.name != startNode:
                bfs.append(node.name)
                node = self.getNode(node.parent)
            bfs.append(node.name)
            return bfs[::-1]
        return []

    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using depth-first search.

    def depthFirstSearch(self, startNode, endNode):
        if self.__contains__(startNode) and self.__contains__(endNode):
            ### keep track of visited nodes
            visited = [False] * (len(self.nodeTable) + 1)

            ### this is the list of the bfs path
            dfs = []

            ### this is the queue im gonna use to see which node i will visit
            queue = [startNode]
            node = startNode

            while node != endNode:
                edges = self.edgeMap.get(node)
                for edge in edges:
                    if not visited[int(edge.dest)]:
                        queue.append(edge.dest)
                        self.getNode(edge.dest).parent = node
                        visited[int(edge.dest)] = True
                node = queue.pop()

            node = self.getNode(node)
            while node.name != startNode:
                dfs.append(node.name)
                node = self.getNode(node.parent)
            dfs.append(node.name)
            return dfs[::-1]
        return []

    ### implement Djikstra's all-pairs shortest-path algorithm.
    ### https://yourbasic.org/algorithms/graph/#dijkstra-s-algorithm
    ### return the array of distances and the array previous nodes.
    def djikstra(self, startNode):
        q = self.edgeMap
        dist = []
        parent = []
        for v in q:
            dist.append(sys.maxsize)
            parent.append(None)
        dist[int(startNode) - 1] = 0

        for n in q:
            for i in q.get(n):
                if dist[int(n) - 1] + int(i.weight) < dist[int(i.dest) - 1]:
                    dist[int(i.dest) - 1] = dist[int(n) - 1] + int(i.weight)
                    parent[int(i.dest) - 1] = n
        return dist, parent

    ### takes as input a starting node, and computes the minimum spanning tree, using Prim's algorithm.
    ### https:// en.wikipedia.org/wiki/Prim % 27s_algorithm
    ### you should return a new graph representing the spanning tree generated by Prim's.
    def prim(self, startNode):
        pass

    ### 686 students only ###
    ### takes as input a startingNode and returns a list of all nodes in the maximum clique containing this node.
    ### https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique

    def clique(self, startNode):
        pass


if __name__ == '__main__':
    g = Graph()
    g.readFromFile("soc-tribes.edges")
    bfs = g.breadthFirstSearch("1", "10")
    dfs = g.depthFirstSearch("1", "10")
    d_cost, d_parent = g.djikstra("1")

    print("bfs from 1 -> 10: " + str(bfs))
    print("dfs from 1 -> 10: " + str(dfs))

