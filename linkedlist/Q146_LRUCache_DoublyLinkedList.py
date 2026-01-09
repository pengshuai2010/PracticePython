from functools import lru_cache


class LRUCache:

    def __init__(self, capacity: int):
        # is capacity guaranteed > 0?
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping: dict[int, ListNode] = {}

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self._remove_from_list(node)
        self._insert_at_head(node)
        return node.value

    def _remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, key: int, value: int) -> None:
        # Should we put in the item first or evict first?
        # it doesn't matter
        if key in self.mapping:
            # find and update
            node = self.mapping[key]
            node.value = value
            self._remove_from_list(node)
        else:
            node = ListNode(key, value)
            self.mapping[key] = node
        self._insert_at_head(node)
        if len(self.mapping) > self.capacity:
            to_remove = self.tail.prev
            self._remove_from_list(to_remove)
            # Don't forget to also remove from mapping!
            del self.mapping[to_remove.key]

    def _insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.prev.next = node
        node.next.prev = node


class ListNode:
    def __init__(self, key: int = 0, value: int = 0, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    def __str__(self):
        return f'{{{self.key}:{self.value}}}'

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



