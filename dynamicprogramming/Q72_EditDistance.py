class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1] * len(word2) for _ in range(len(word1))]

        def min_distance_recursion(word1: str, word2: str, index1: int, index2: int):
            if index1 < 0:
                return index2 + 1
            if index2 < 0:
                return index1 + 1
            if memo[index1][index2] != -1:
                return memo[index1][index2]
            if word1[index1] == word2[index2]:
                return min_distance_recursion(word1, word2, index1 - 1, index2 - 1)
            replace_distance = min_distance_recursion(word1, word2, index1 - 1, index2 - 1)
            delete_distance = min_distance_recursion(word1, word2, index1 - 1, index2)
            insert_distance = min_distance_recursion(word1, word2, index1, index2 - 1)
            result = 1 + min(replace_distance, delete_distance, insert_distance)
            memo[index1][index2] = result
            return result

        return min_distance_recursion(word1, word2, len(word1) - 1, len(word2) - 1)
