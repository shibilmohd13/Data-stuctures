from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, data):
        if data not in self.graph:
            self.graph[data] = []

    def add_edge(self, from_, to_, bidirectional=True):
        self.add_vertex(from_)
        self.add_vertex(to_)
        self.graph[from_].append(to_)

        if bidirectional:
            self.graph[to_].append(from_)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        if start not in visited:
            print(start, end=' ')
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)


# Example Usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("BFS:")
g.bfs(1)
print("\nDFS:")
g.dfs(1)
