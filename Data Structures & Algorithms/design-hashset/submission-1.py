class MyHashSet:

    def __init__(self):
        self.hashMap = {}
        

    def add(self, key: int) -> None:
        self.hashMap[key] = key

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]
        else:
            pass
        

    def contains(self, key: int) -> bool:
        return True if key in self.hashMap else False