class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):        
        return 1  # Force colision

    def insert(self, key, value):        
        index = self._hash(key)
        self.table[index] = value

    def get(self, key):        
        index = self._hash(key)
        return self.table[index]

    def delete(self, key):        
        index = self._hash(key)
        self.table[index] = None

ht = HashTable()
ht.insert("rm", "real madrid")
ht.insert("barca", "barcelona")  


print(ht.get("rm"))  
print(ht.get("barca"))
