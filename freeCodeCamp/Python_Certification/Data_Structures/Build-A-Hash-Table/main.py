class HashTable:

    def __init__(self):
        self.collection = {}

    def hash(self, phrase):
        sum = 0 
        for c in phrase:
            sum += int(ord(c))
        return sum
            
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
        else:
            return None

h = HashTable()
h.add('fcc', 'sport')
print(h.collection)
print(h.lookup('cfc'))
