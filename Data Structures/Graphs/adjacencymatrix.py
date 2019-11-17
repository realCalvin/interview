

class Graph:
    def __init__(self, size):
        self.graph = [[0 for i in range(size)] for j in range(size)]
        self.size = size

    def addEdge(self, v1, v2, weight):
        if v1 >= self.size or v2 >= self.size:
            print("Out of bounds")
            return 
        self.graph[v1][v2] = weight
        self.graph[v2][v1] = weight

    def print(self):
        for row in self.graph:
            print(row)
    

if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(3, 4, 8)
    g.addEdge(5, 2, 5)
    g.print()