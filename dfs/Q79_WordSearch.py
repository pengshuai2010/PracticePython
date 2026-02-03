from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # will board be empty?
        # will word be empty? 
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        num_rows = len(board)
        num_cols = len(board[0])  # assuming board won't be empty
        visited = [[False for _ in range(num_cols)] for __ in range(num_rows)]

        def helper(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            if not in_boundary(row, col) or visited[row][col] or word[index] != board[row][col]:
                return False
            visited[row][col] = True
            result = False
            for direction in directions:
                x, y = row + direction[0], col + direction[1]
                if helper(x, y, index + 1):
                    result = True
                    break
            visited[row][col] = False
            return result

        def in_boundary(row: int, col: int) -> bool:
            return 0 <= row < num_rows and 0 <= col < num_cols

        for i in range(num_rows):
            for j in range(num_cols):
                if helper(i, j, 0):
                    return True
        return False

    def test(self):
        s = "hello"
        l = [1, 2, 3]
        r = [1, 2, 3]
        count = 3

        def test_nested():
            s = 2
            print(s)
            l = [2, 2]
            l.append(4)
            r[0] = 0
            nonlocal count # to modify count, we must first declare it to be nonlocal
            count += 1
            print(l)
            print(f"count is {count}")

        test_nested()
        print(s)
        print(l)
        print(f"count is {count}")
        print(r)

if __name__ == "__main__":
    Solution().test()
