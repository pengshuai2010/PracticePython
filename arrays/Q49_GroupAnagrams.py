import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                count[index] += 1
            groups[tuple(count)].append(s) # list is not hashable but tuple is
        return list(groups.values()) # why? because groups.values() is an iterator, not an actual list

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))