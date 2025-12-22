from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(t)
        for char in s:
            d[char] -= 1
        for key, value in d.items():
            if value == 1:
                return key
        raise ValueError()
if __name__ == '__main__':
    solution = Solution()
    for s, t in [("abc", "abcd"), ("a", "aa")]:
        print("s: " + s + " t: " + t)
        print(solution.findTheDifference(s, t))
