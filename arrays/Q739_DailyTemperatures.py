from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Go from left to right. The stack is a monotonic stack in decreasing order.
        # When current day's temperature is greater than the that of stack top, it would be the first day
        # that the temperature is greater than that of the stack top. So we should pop out the stack top,
        # and update the next_greater_index on the top_index.
        stack = []
        n = len(temperatures)
        next_greater_index = [-1] * n
        answer = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top_index = stack.pop()
                next_greater_index[top_index] = i
                answer[top_index] = i - top_index
            stack.append(i)
        return answer

    def dailyTemperatures_rightToLeft(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        next_greater_index = [-1] * n
        answer = [0] * n
        for i in reversed(range(n)):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                next_greater_index[i] = stack[-1]
                answer[i] = next_greater_index[i] - i
            else:
                next_greater_index[i] = -1
                answer[i] = 0
            stack.append(i)
        return answer

# tempreture
# 0, 1, 2, 3
# 4, 5, 3, 7
# next greater index
# 1 , 3 , 3 , -1
# answer
# 1, 2, 1, 0
# stack
# 3, 1, 0