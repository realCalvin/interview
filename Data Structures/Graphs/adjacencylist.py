

class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = [v2]
        else:
            self.graph[v1].append(v2)

    def print(self):
        for vertex in self.graph:
            print("Vertex: " + str(vertex), end=" -> ")
            for neighbor in self.graph[vertex]:
                print(str(neighbor), end=" -> ")
            print()

if __name__ == '__main__':
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(1,4)
    g.addEdge(1,8)
    g.addEdge(1,7)
    g.addEdge(5,7)
    g.print()
    print(g.graph)