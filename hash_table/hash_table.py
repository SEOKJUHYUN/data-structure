import hashlib

class HashTable : 
    def __init__(self, lens) -> None:
        self.hash_table = [None for _ in range(lens)]
        self.lens = lens

    def hashing(self, key) :
        hashing = hashlib.sha256()
        hashing.update(key.encode())
        hash_hex = hashing.hexdigest()
        return int(hash_hex, 16)

    def create_key(self, hash_hex) :
        return hash_hex % self.lens

    def insert(self, key, values) :
        hash_hex = self.hashing(key)
        key = self.create_key(hash_hex)

        if self.hash_table[key] is not None :
            for for_index, for_values in enumerate(self.hash_table[key]) :
                pass

        else :
            self.hash_table[key] = [hash_hex, values]

hash_table = HashTable(16)
hash_table.insert("asd", 123)