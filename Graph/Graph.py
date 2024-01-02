from operator import ne


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, data):
        if data not in self.graph:
            self.graph[data] = []

    def add_edge(self, from_, to_ , bi=False):
        self.add_vertex(from_)
        self.add_vertex(to_)
        self.graph[from_].append(to_)
        
        if bi:
            self.graph[to_].append(from_)

    def display(self):
        print("{")
        for char,edges in self.graph.items():
            print(f"{char} : {edges}")
        print("}")



new = Graph()

new.add_vertex(10)
new.add_vertex(56)
new.add_vertex(13)
new.add_vertex(43)
new.add_vertex(67)
new.add_edge(20,24,True)
new.add_edge(10,56,True)
new.add_edge(10,24)
new.add_edge(0,24)
new.add_edge(20,67)
new.display()
