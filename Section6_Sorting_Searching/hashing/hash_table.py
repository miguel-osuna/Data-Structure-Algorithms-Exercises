class HashTable():
    def __init__(self):
        self._size = 11
        self.slots = [None] * self._size
        self.data = [None] * self._size

    def __str__(self):
        return str((self.slots, self.data))

    # Overloads 'len' operator as 'len(self)'
    def __len__(self):
        return self._size

    # Overloads 'in' operator as 'item in self'
    def __contains__(self, item):
        return item in self.data

    # Implements evaluation as 'self[key]'
    def __getitem__(self, key):
        return self.get(key)

    # Implements assignment as 'self[key] = value'
    def __setitem__(self, key, data):
        self.put(key, data)

    # Overloads 'del' operator as 'del self[key]'
    def __delitem__(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        found = False
        stop = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                del self.slots[position]
                del self.data[position]
                print("Item deleted")
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
                    print("Couldn't delete item")

    def hashfunction(self, key, size):
        ''' Generates a hash '''
        return key % size

    def rehash(self, hash, size):
        ''' Generates a new hash from an old hash '''
        return (hash + 1) % size

    def get(self, key):
        ''' Gets item from hash table '''
        startslot = self.hashfunction(key, len(self.slots))

        found = False
        stop = False
        data = None
        position = startslot

        # Looks for the matching key slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def put(self, key, data):
        ''' Sets item in hash table '''
        hashValue = self.hashfunction(key, len(self.slots))

        # Assigns data if slot is available
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        # Replaces data if key slot is the same
        elif self.slots[hashValue] == key:
            self.data[hashValue] = data
        # Looks for slots available
        else:
            nextslot = self.rehash(hashValue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

            # Assigns data if slot is available
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            # Replaces data if key slot is the same
            else:
                self.data[nextslot] = data


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[7] = "wolf"
    H[8] = "seal"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(H)
    del H[22]
    print(H)
    print("human" in H)
    print("dog" in H)
