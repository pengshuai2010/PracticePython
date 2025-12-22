class MinStack:
    _stack:[]
    _min:[]

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._min) == 0:
            self._min.append(val)
        else:
            self._min.append(min(self._min[-1], val))

    def pop(self) -> None:
        if len(self._stack) == 0:
            raise IndexError("stack is empty")
        val = self._stack.pop()
        self._min.pop()
        return val

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()