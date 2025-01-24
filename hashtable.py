class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        # simple funcion hash
        return hash(key) % self.size

    def insert(self, key, value):        
        index = self._hash(key) # O(1)
        self.table[index] = value

    def get(self, key):        
        index = self._hash(key)
        return self.table[index]

    def delete(self, key):        
        index = self._hash(key)
        self.table[index] = None

# Using
ht = HashTable()
ht.insert("rm", "real madrid")
print(ht.get("rm"))  
