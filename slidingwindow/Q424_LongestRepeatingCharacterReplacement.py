from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # is s guaranteed to consist of only upper case English letters?
        counter = Counter()
        start = 0
        end = 0
        most_popular_ch = None
        window_size = 0
        max_substring_len = 0
        while end < len(s):
            ch = s[end]
            counter[ch] += 1
            window_size += 1
            if most_popular_ch is None or counter[ch] > counter[most_popular_ch]:
                most_popular_ch = ch
            while window_size - counter[most_popular_ch] > k:
                counter[s[start]] -= 1
                window_size -= 1
                if s[start] == most_popular_ch:
                    for key in counter:
                        if counter[key] > counter[most_popular_ch]:
                            most_popular_ch = key
                start += 1
            max_substring_len = max(max_substring_len, window_size)
            end += 1
        return max_substring_len