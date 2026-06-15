class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def exists(self, root, key):
        if root is None:
            return False
        
        if key < root.key:
            return self.exists(root.left, key)
        elif key > root.key:
            return self.exists(root.right, key)
        else:
            return True

    def delete(self, root, key):
        if root is None:
            return

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            new = self.getMinValue(root.right)
            root.key = new.key
            root.right = self.delete(root.right, key)
        return root

    def getMinValue(self, root):
        while root.left:
            root = root.left
        return root

    def add(self, key):
        self.root = self.insert(self.root, key)
    
    def remove(self, key):
        self.root = self.delete(self.root, key)

    def contains(self, key):
        return self.exists(self.root, key)
        

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.buckets[idx].add(key)
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.buckets[idx].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)