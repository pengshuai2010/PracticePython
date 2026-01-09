from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        # is capacity guaranteed > 0?
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)


if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))
    lru_cache.put(3, 3)
    print(lru_cache.get(2))
    lru_cache.put(4, 4)
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
# answer:
# 1
# -1
# -1
# 3
# 4

