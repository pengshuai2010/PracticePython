import collections


class Solution:
    def isValid(self, s: str) -> bool:
        # will there be other characters?
        stack = collections.deque()
        mapping = {'}': '{', ']': '[', ')': '('}
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                matching = mapping[ch]
                top = stack[-1] # stack[len(stack) - 1]
                if top != matching:
                    return False
                stack.pop()
        return len(stack) == 0

# test cases:
# ()
# ()()
# {}
# []
# )
# (
# (}
# {(})