class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        # will s be empty?
        if len(s) == 0:
            return 0
        char_set = set() # keeps track of the chars in the substring
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            ch = s[end]
            while ch in char_set:
                # keep shrinking the sliding window and removing chars from chat_set
                char_set.remove(s[start])
                start += 1
            char_set.add(ch) # we previously removed ch from the set, need to add it back
            max_len = max(max_len, end - start + 1)
            end += 1

        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # will s be empty?
        if len(s) == 0:
            return 0
        d = {}
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            ch = s[end]
            if ch in d and d[ch] >= start: # Think of "bb" and "abb" case
                start = d[ch] + 1
            max_len = max(max_len, end - start + 1)
            d[ch] = end
            end += 1
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # will s be empty?
        if len(s) == 0:
            return 0
        d = {}
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            ch = s[end]
            if ch in d:
                new_start = d[ch] + 1
                # Actually it is not necessary to delete the keys. We just need to check if
                # d[ch] >= start. See the solution above.
                # This optimization doesn't change the time complexity though.
                for i in range(start, d[ch] + 1):
                    del d[s[i]]
                start = new_start
            else:
                max_len = max(max_len, end - start + 1)
            d[ch] = end
            end += 1
        return max_len