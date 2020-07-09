"""
Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash = self.calculate_hash_value(string)
        self.table[hash] = string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash = self.calculate_hash_value(string)
        if self.table[hash]:
            return hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash = ord(string[0])*100+ ord(string[1])
        return hash

    