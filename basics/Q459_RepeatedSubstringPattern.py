class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # will s be null or empty?
        for i in range(1, len(s)  // 2 + 1):
            if len(s) % i != 0:
                continue
            is_repeated_pattern = True
            pattern = s[:i]
            for j in range(0, len(s) - 1, i):
                if s[j:j + i] != pattern:
                    is_repeated_pattern = False
                    break
            if is_repeated_pattern:
                return True
        return False

    def repeatedSubstringPattern_rotation(self, s: str) -> bool:
        # clarify will s be null or empty?
        t = s * 2
        
        return t.find(s, 1, len(t) - 1) != -1
if __name__ == '__main__':
    Solution().repeatedSubstringPattern("ab")