class Solution:
    def minFlips(self, s: str) -> int:
        ss = s + s

        def calculate_min_flips(expected_curr):
            flips = [0] * len(ss)
            min_flips = len(s)
            for i in range(len(ss)):
                ch = ss[i]
                if ch != expected_curr:
                    flips[i] = 1
                expected_curr = '0' if expected_curr == '1' else '1'
            left = 0
            right = 0
            num_flips = 0
            while right < len(ss):
                num_flips += flips[right]
                if right - left + 1 == len(s):
                    min_flips = min(min_flips, num_flips)
                    num_flips -= flips[left]
                    left += 1
                right += 1
            return min_flips

        return min(calculate_min_flips('0'), calculate_min_flips('1'))

