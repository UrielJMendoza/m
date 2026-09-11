class MyHashMap:
    def __init__(self):
        self.keysCheck = set()
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keysCheck:
            self.values[self.keys.index(key)] = value
        else:
            self.keysCheck.add(key)
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key not in self.keysCheck:
            return -1
        if key in self.keysCheck and self.values[self.keys.index(key)] is None:
            return -1
        else:
            return self.values[self.keys.index(key)]

    def remove(self, key: int) -> None:
        if key not in self.keysCheck:
            return None
        idx = self.keys.index(key)
        self.keysCheck.remove(key)
        self.keys.pop(idx)
        self.values.pop(idx)
