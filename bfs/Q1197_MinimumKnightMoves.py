from collections import deque
from typing import Tuple, List


class Solution:
    def minKnightMoves_wo_pruning(self, x: int, y: int) -> int:
        DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

        def get_neighbors(node) -> list[tuple[int, int]]:
            neighbors = []
            # Tuple unpacking is useful here
            for dx, dy in DIRECTIONS:
                neighbor = (node[0] + dx, node[1] + dy)
                neighbors.append(neighbor)
            return neighbors

        # We could just use list here because we are doing level order traversal instead of regular BFS
        front = [(0, 0)]
        front_seen = {(0, 0)}
        back = [(x, y)]
        back_seen = {(x, y)}
        steps = 0
        while len(front) > 0 and len(back) > 0:
            if len(front) > len(back):
                front, back = back, front
                front_seen, back_seen = back_seen, front_seen
            front_next = []
            for node in front:
                if node in back_seen:
                    return steps
                for neighbor in get_neighbors(node):
                    if neighbor not in front_seen:
                        front_next.append(neighbor)
                        front_seen.add(neighbor)
            front = front_next
            steps += 1
        return steps

    def minKnightMoves(self, x: int, y: int) -> int:
        DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

        def get_neighbors(node) -> list[tuple[int, int]]:
            neighbors = []
            # Tuple unpacking is useful here
            for dx, dy in DIRECTIONS:
                neighbor = (node[0] + dx, node[1] + dy)
                neighbors.append(neighbor)
            return neighbors

        # Optimization because of symmetry
        x = abs(x)
        y = abs(y)
        # We could just use list here because we are doing level order traversal instead of regular BFS
        front = [(0, 0)]
        front_seen = {(0, 0)}
        back = [(x, y)]
        back_seen = {(x, y)}
        steps = 0
        while len(front) > 0 and len(back) > 0:
            if len(front) > len(back):
                front, back = back, front
                front_seen, back_seen = back_seen, front_seen
            front_next = []
            for node in front:
                if node in back_seen:
                    return steps
                for neighbor in get_neighbors(node):
                    # We only need to search in the first quadrant and there is no need search beyond x + 2 and y + 2.
                    if (-2 <= neighbor[0] <= x + 2 and -2 <= neighbor[1] <= y + 2
                            and neighbor not in front_seen):
                        front_next.append(neighbor)
                        front_seen.add(neighbor)
            front = front_next
            steps += 1
        return steps