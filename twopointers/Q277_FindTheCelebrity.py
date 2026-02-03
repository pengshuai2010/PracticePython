# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # assume n > 0
        # Two pointers!
        i = 0
        j = n -1
        while i < j:
            if knows(i, j):
                i += 1
            else:
                j -= 1
        # now i is candidate
        for j in range(n):
            if j == i:
                continue
            if knows(i, j) or not knows(j, i):
                return -1
        return i
