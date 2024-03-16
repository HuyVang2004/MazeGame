import queue
import math


class AI:
    def __init__(self, span, size, start, end):
        self.span = span
        self.size = size
        self.start = start
        self.end = end
        self.closed = []

    def get_child(self, parent):
        childs = []
        for a in self.span:
            if a[0] == parent:
                childs.append(a[1])

            elif a[1] == parent:
                childs.append(a[0])

        return childs

    def solve(self):
        open = queue.PriorityQueue()
        self.closed = []
        g = [0 for i in range(len(self.span) + 1)]
        h = [0 for i in range(len(self.span) + 1)]
        f = [0 for i in range(len(self.span) + 1)]

        open.put((0, self.start))
        while not open.empty():
            ni = open.get_nowait()
            if ni[1] not in self.closed:
                self.closed.append(ni[1])
            if ni[1] == self.end:
                break
            else:
                child_ni = self.get_child(ni[1])

                for nk in child_ni:
                    g[nk] = g[ni[1]] + 1
                    h[nk] = math.fabs(self.end - nk) // self.size + math.fabs(self.end - nk) % self.size
                    f[nk] = g[nk] + h[nk]
                    if nk not in self.closed:
                        open.put((f[nk], nk))
        i = len(self.closed) - 1

        while i >= 0:
            if self.closed[i] not in self.get_child(self.closed[i - 1]):
                self.closed.remove(self.closed[i - 1])
            i -= 1
        self.closed.append(self.end)
        return self.closed
