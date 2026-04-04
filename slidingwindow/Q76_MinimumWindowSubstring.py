from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Could there be duplicates in t? Yes
        # assuming s and t are not empty.
        # What if there is a tie? Return one solution.
        required = Counter(t)
        window_count = Counter() # default value to 0
        satisfied_chars = 0
        start = 0
        end = 0
        min_window = ""
        while end < len(s):
            current_char = s[end]
            if current_char in required:
                window_count[current_char] += 1
                if window_count[current_char] == required[current_char]:
                    satisfied_chars += 1
            while satisfied_chars == len(required):
                if not min_window or len(min_window) > end - start + 1:
                    min_window = s[start: end + 1]
                to_remove = s[start]
                if to_remove in required: # to_remove is not necessarily a required char!
                    window_count[to_remove] -= 1
                    if window_count[to_remove] < required[to_remove]:
                        satisfied_chars -= 1
                start += 1
            end += 1
        return min_window