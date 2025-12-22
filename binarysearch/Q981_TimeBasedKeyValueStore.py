import bisect


class TimeMap:
    _map: dict[str, list]

    def __init__(self):
        self._map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self._map[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # i = bisect_right(l, x) is the insertion position to the right of the elements that are less than or equal
        # to x. so (i - 1) is the index of the rightmost element that is less than or equal to x.
        # if i == 0, that means there is no element that is less than or equal to x in the list l.
        index = bisect.bisect_right(self._map[key], timestamp, key=lambda x: x[0])
        if index > 0:
            return self._map[key][index - 1][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)