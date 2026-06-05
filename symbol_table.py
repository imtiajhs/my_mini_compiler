class SymbolTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, name, datatype):
        index = self.hash_func(name)

        for item in self.table[index]:
            if item[0] == name:
                item[1] = datatype
                return

        self.table[index].append([name, datatype])

    def display(self):

        result = []

        for i in range(self.size):
            for item in self.table[i]:
                result.append([i, item[0], item[1]])

        return result