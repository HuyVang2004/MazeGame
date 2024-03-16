import random


class DSU:
    def __init__(self, n):
        self.parent = []
        for i in range(n * n):
            self.parent.append(i)

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.parent[u] = v
            return True
        return False


class Grap:
    def __init__(self, n):
        self.E = []
        self.size = n
        for i in range(n):
            for j in range(n * i, n * (i + 1)):
                if j + 1 < n * (i + 1):
                    self.E.append([j, j + 1])
                if i + 1 < n:
                    self.E.append([j, j + n])

    def random_edge(self):
        return random.choice(self.E)

    def kruskal(self):
        S = []

        dsu = DSU(self.size)

        while len(S) < self.size * self.size - 1:
            edge = self.random_edge()
            u = edge[0]
            v = edge[1]
            if dsu.union(u, v):
                S.append(edge)

        return S


class Maze:
    def __init__(self, size):
        self.span = Grap(size).kruskal()
        self.maze = [[1 for _ in range(size * 2 + 1)] for _ in range(size * 2 + 1)]
        self.convert_array(size)

    def convert_array(self, size):
        for a in self.span:
            i = a[0] // size
            j = a[0] % size
            if a[1] - a[0] == 1:
                self.maze[2 * i + 1][2 * j + 1] = 0
                self.maze[2 * i + 1][2 * j + 2] = 0
                self.maze[2 * i + 1][2 * j + 3] = 0
            if a[1] - a[0] == size:
                self.maze[2 * i + 1][2 * j + 1] = 0
                self.maze[2 * i + 2][2 * j + 1] = 0
                self.maze[2 * i + 3][2 * j + 1] = 0
