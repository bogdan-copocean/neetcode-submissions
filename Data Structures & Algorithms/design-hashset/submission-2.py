class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class MyHashSet:

    def __init__(self):
        self._buckets = [Node() for _ in range(10000)]
    
    def _hash(self, value):
        return value % len(self._buckets)
    
    def _get_next_free_spot(self, hashed) -> Node:
        node = self._buckets[hashed]
        while node.next is not None:
            node = node.next
        return node
    
    def _search_key(self, key):
        hashed = self._hash(key)
        node = self._buckets[hashed]
        while node:
            if node.value == key:
                return node
            node = node.next
        return None

    def add(self, key: int) -> None:
        hashed = self._hash(key)
        node = self._get_next_free_spot(hashed)
        if node.prev and node.prev.value == key:
            return
        node.value = key
        node.next = Node()
        node.next.prev = node
        
    def remove(self, key: int) -> None:
        node = self._search_key(key)
        if node:
            if node.prev:
                node.prev.next = None
            else:
                node.value = None

    def contains(self, key: int) -> bool:
        exists = self._search_key(key)
        if exists and exists.value is not None:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)