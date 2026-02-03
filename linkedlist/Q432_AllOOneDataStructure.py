class Node:
    def __init__(self, frequency):
        self.frequency = frequency
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self._head = Node(0)
        self._tail = Node(0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._map = dict()

    def inc(self, key: str) -> None:
        if key not in self._map:
            self._insert_after(self._head, key, 1)
        else:
            node = self._map[key]
            node.keys.remove(key)
            current_frequency = node.frequency
            self._insert_after(node, key, current_frequency + 1)
            if len(node.keys) == 0:
                self._remove_node(node)

    def _insert_after(self, node: Node, key: str, frequency: int):
        destination = node.next
        # don't forget the case where next node is tail
        if node.next == self._tail or node.next.frequency != frequency:
            new_node = Node(frequency)
            new_node.next = node.next
            new_node.prev = node
            new_node.next.prev = new_node
            new_node.prev.next = new_node
            destination = new_node
        destination.keys.add(key)
        self._map[key] = destination

    def _insert_before(self, node: Node, key: str, frequency: int):
        destination = node.prev
        if node.prev == self._head or node.prev.frequency != frequency:
            new_node = Node(frequency)
            new_node.prev = node.prev
            new_node.next = node
            new_node.next.prev = new_node
            new_node.prev.next = new_node
            destination = new_node
        destination.keys.add(key)
        self._map[key] = destination

    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def dec(self, key: str) -> None:
        if key not in self._map:
            return  # do nothing if key doesn't exist
        node = self._map[key]
        del self._map[key]
        node.keys.remove(key)
        current_frequency = node.frequency
        if current_frequency > 1:
            self._insert_before(node, key, current_frequency - 1)
        if len(node.keys) == 0:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        # will this method be invoked when the list is empty?
        if self._tail.prev == self._head:
            return ""  # the list is empty
        return next(iter(self._tail.prev.keys))

    def getMinKey(self) -> str:
        if self._head.next == self._tail:
            return ""  # the list is empty
        return next(iter(self._head.next.keys))