import heapq


class MaxStack:

    def __init__(self):
        self._count = 0
        self._max_heap = []
        self._stack = []
        self._deleted = set()

    def push(self, x: int) -> None:
        item = (x, self._count)
        heapq.heappush_max(self._max_heap, item)
        self._stack.append(item)
        self._count += 1

    def pop(self) -> int:
        while self._stack[-1][1] in self._deleted:
            self._stack.pop()
        item = self._stack.pop()
        self._deleted.add(item[1])
        return item[0]

    def top(self) -> int:
        while self._stack[-1][1] in self._deleted:
            self._stack.pop()
        top = self._stack[-1]
        return top[0]

    def peekMax(self) -> int:
        while self._max_heap[0][1] in self._deleted:
            heapq.heappop_max(self._max_heap)
        item = self._max_heap[0]
        return item[0]

    def popMax(self) -> int:
        while self._max_heap[0][1] in self._deleted:
            heapq.heappop_max(self._max_heap)
        item = heapq.heappop_max(self._max_heap)
        self._deleted.add(item[1])
        return item[0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()