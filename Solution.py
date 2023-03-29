from collections import deque


class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        visited = set()
        q = deque([self.start_node])
        levels = [-1] * len(self.graph)

        visited.add(self.start_node)
        q.append(self.start_node)
        levels[self.start_node] = 0

        while q:
            currentNode = q.popleft()

            for neighbour in self.graph[currentNode]:
                if neighbour not in visited:
                    q.append(neighbour)
                    levels[neighbour] = levels[currentNode] + 1
                    visited.add(neighbour)
        return levels
