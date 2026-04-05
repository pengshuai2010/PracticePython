from collections import defaultdict, deque
from typing import List


class Solution:
    # Time complexity is O(N + E), where N is the number of nodes, and E is the number of edges (dislike relationships
    # in this case).
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # assuming n > 1
        neighbors = defaultdict(list)
        for dislike in dislikes:
            a, b = dislike
            neighbors[a].append(b)
            neighbors[b].append(a)
        group1 = set()
        group2 = set()

        def helper(source):
            queue = deque()
            queue.append(source)
            # it is OK to assign the source node to a random group, because we already know that this node
            # has no connection to the nodes we have previously assigned (suppose it had, it would already been in
            # group1 or group2).
            group1.add(source)
            current_group = group1
            next_group = group2
            while queue:
                size = len(queue)
                for i in range(size):
                    node = queue.popleft()
                    for neighbor in neighbors[node]:
                        if neighbor in current_group:
                            return False
                        if neighbor not in next_group:
                            queue.append(neighbor)
                            next_group.add(neighbor)
                current_group, next_group = next_group, current_group
            return True

        for i in range(1, n + 1):
            if i in group1 or i in group2:
                continue
            if not helper(i):
                return False
        return True