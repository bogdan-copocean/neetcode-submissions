class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyHashSet:

    def __init__(self):
        self._buckets = [Node() for _ in range(100)]
    
    def _hash(self, value):
        return value % len(self._buckets)

    def add(self, key: int) -> None:
        idx = self._hash(key)
        curr = self._buckets[idx]
        while curr.next:
            if curr.next.value == key:
                return
            curr = curr.next
        curr.next = Node(key)
        
    def remove(self, key: int) -> None:
        curr = self._buckets[self._hash(key)]
        while curr.next:
            if curr.next.value == key:
                curr.next = curr.next.next
                return
            curr = curr.next


    def contains(self, key: int) -> bool:
        curr = self._buckets[self._hash(key)]
        while curr.next:
            if curr.next.value == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)