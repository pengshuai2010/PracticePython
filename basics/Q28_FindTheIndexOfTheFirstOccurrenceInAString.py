class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # clarifying questions: haystack needle guaranteed to be valid? null, empty?
        # len(needle) > len(haystack)?
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
