class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs_on = 0
        for i in range(1, n + 1):
            toggles = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    toggles += 1
            is_on = toggles % 2 == 1
            if is_on:
                bulbs_on += 1
        return bulbs_on