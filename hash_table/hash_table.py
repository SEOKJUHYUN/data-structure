import hashlib

class HashTable : 
    def __init__(self, lens) -> None:
        self.hash_table = [[None] for _ in range(lens)]
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

        if self.hash_table[key][0] is not None :
            for _, for_values in enumerate(self.hash_table[key]) :
                if for_values[0] == hash_hex:
                    for_values[1] = values
                    return 0

                else :
                    continue

            self.hash_table[key].append([hash_hex, values])

        else :
            self.hash_table[key] = [[hash_hex, values]]

    def print(self, key) :
        hash_hex = self.hashing(key)
        key = self.create_key(hash_hex)

        if self.hash_table[key][0] is None :
            return 1

        elif self.hash_table[key][0][0] == hash_hex :
            return self.hash_table[key][0][1]

        else :
            for _, for_values in enumerate(self.hash_table[key]) :
                if for_values[0] == hash_hex:
                    return for_values[1]

hash_table = HashTable(2)
hash_table.insert("da", 123)
hash_table.insert("dh", 123)
hash_table.insert("dh", 456)
print(hash_table.print("dh"))
print(hash_table.print("da"))