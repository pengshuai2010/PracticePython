from collections import defaultdict, deque


class Solution:
    def minReorder_DFS(self, n: int, connections: list[list[int]]) -> int:
        total_cost = 0
        neighbors = defaultdict(list)
        for source, destination in connections:
            # We assign cost of 1 for source -> destination, why?
            # Because we start from node 0, and want make edges pointing back to node 0.
            neighbors[source].append((destination, 1))
            neighbors[destination].append((source, 0))
        # What seen does is to prevent a node from being visited twice
        # In this particular case seen prevents visiting a node's "parent" (we are told the graph would be like a tree)
        seen = {0}

        def helper(node):
            nonlocal total_cost
            for neighbor, cost in neighbors[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    total_cost += cost
                    helper(neighbor)

        helper(0)
        return total_cost

    # We should try using BFS whenever possible as DFS is subject to stack overflow issues. Particularly in CPython,
    # the default recursion depth limit is typically 1,000.
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        total_cost = 0
        neighbors = defaultdict(list)
        for source, destination in connections:
            # We assign cost of 1 for source -> destination, why?
            # Because we start from node 0, and want make edges pointing back to node 0.
            neighbors[source].append((destination, 1))
            neighbors[destination].append((source, 0))
        # What seen does is to prevent a node from being visited twice
        # In this particular case seen prevents visiting a node's parent
        queue = deque([0])
        seen = {0}

        while queue:
            node = queue.popleft()
            for neighbor, cost in neighbors[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    total_cost += cost
                    queue.append(neighbor)
        return total_cost
