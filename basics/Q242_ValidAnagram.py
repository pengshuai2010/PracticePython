from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = dict()
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
            else:
                return False
        for char in char_dict:
            if char_dict[char] != 0:
                return False
        return True

    def isAnagram_counter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)