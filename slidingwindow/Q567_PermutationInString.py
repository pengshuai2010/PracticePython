class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # will s1 or s2 be empty?
        diff = {}
        for c in s1:
            diff[c] = diff.get(c, 0) - 1 # this is the diff
        window_size = len(s1)
        start = 0
        for end in range(len(s2)):
            ch = s2[end]
            diff[ch] = diff.get(ch, 0) + 1
            if diff[ch] == 0:
                del diff[ch]
            if end - start + 1 > window_size:
                start_ch = s2[start]
                diff[start_ch] = diff.get(start_ch, 0) - 1
                if diff[start_ch] == 0:
                    del diff[start_ch]
                start += 1
            if end - start + 1 == window_size and len(diff) == 0:
                    return True
        return False

    def checkInclusion_preprocess(self, s1: str, s2: str) -> bool:
        # will s1 or s2 be empty?
        if len(s2) < len(s1):
            return False
        diff = {}
        for i in range(len(s1)):
            c = s1[i]
            diff[c] = diff.get(c, 0) - 1 # this is the diff
            if diff[c] == 0:
                del diff[c]
            c = s2[i]
            diff[c] = diff.get(c, 0) + 1
            if diff[c] == 0:
                del diff[c]
        if len(diff) == 0:
            return True

        start = 0
        for end in range(len(s1), len(s2)):
            ch = s2[end]
            diff[ch] = diff.get(ch, 0) + 1
            if diff[ch] == 0:
                del diff[ch]
            start_ch = s2[start]
            diff[start_ch] = diff.get(start_ch, 0) - 1
            if diff[start_ch] == 0:
                del diff[start_ch]
            start += 1
            if len(diff) == 0:
                    return True
        return False
if __name__ == '__main__':
    print(Solution().checkInclusion("abc", "babc"))