class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, v1, v2):

        if v1 not in self.graph:
            self.graph[v1] = [v2]
        else:
            self.graph[v1].append(v2)

        # adding the code below makes the graph undirected
        if v2 not in self.graph:
            self.graph[v2] = [v1]
        else:
            self.graph[v2].append(v1)

    def print(self):
        for vertex in self.graph:
            print("Vertex: " + str(vertex), end=" -> ")
            for neighbor in self.graph[vertex]:
                print(str(neighbor), end=" -> ")
            print()


if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(1, 8)
    g.addEdge(8, 13)
    g.addEdge(1, 7)
    g.addEdge(5, 7)
    g.print()
    print(g.graph)
    stack = []
    visited = {}
    stack.append(1)

    while len(stack):
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex)
            visited[vertex] = True

        if vertex in g.graph:
            for neighbor in g.graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
