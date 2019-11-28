# Class for Hash table

class Hash_Table_intro:

##############################Constructors##########################
    def __init__(self, key, item):
        self.key = key
        self.item = item


class Hash_Map:

    # Space-time complexity is O(1)
    def __init__(self, capacity=10):
        self.map = [] # Init. an empty list
        for i in range(capacity):
            self.map.append([])

##############################DEFINE FUNCTIONS##########################

    # Define a function to create a hashtable
    # Space-time complexity is O(1)
    def _get_hash(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Define a function to insert
    # Space-time complexity is O(N)
    def insert(self, key, value):
        hash_keys = self._get_hash(key)
        hash_keys_values = [key, value]

        if self.map[hash_keys] is None:
            self.map[hash_keys] = list([hash_keys_values])
            return True
        else:
            for pairs in self.map[hash_keys]:
                if pairs[0] == key:
                    pairs[1] = hash_keys_values
                    return True
            self.map[hash_keys].append(hash_keys_values)
            return True

    # Define a function to update
    # Space-time complexity is O(N)
    def update(self, key, value):
        hash_keys = self._get_hash(key)
        if self.map[hash_keys] is not None:
            for pairs in self.map[hash_keys]:
                if pairs[0] == key:
                    pairs[1] = value
                    print(pairs[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # Define a fuction to get the information for the hashtable
    # Space-time complexity is O(N)
    def get(self, key):
        hash_keys = self._get_hash(key)
        if self.map[hash_keys] is not None:
            for pairs in self.map[hash_keys]:
                if pairs[0] == key:
                    return pairs[1]
        return None

    # Define a function to delete
    # Space-time complexity is O(N)
    def delete(self, key):
        hash_keys = self._get_hash(key)
        if self.map[hash_keys] is None:
            return False
        for i in range(0, len(self.map[hash_keys])):
            if self.map[hash_keys][i][0] == key:
                self.map[hash_keys].pop(i)
                return True
        return False



