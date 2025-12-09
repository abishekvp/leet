class DynamicArray:
    
    def __init__(self, capacity: int):
        self.ls = [None]*capacity

    def get(self, i: int) -> int:
        return self.ls[i]

    def set(self, i: int, n: int) -> None:
        self.ls[i] = n

    def pushback(self, n: int) -> None:
        self.ls.append(n)

    def popback(self) -> int:
        self.ls.pop()

    def resize(self) -> None:
        for i in range(len(self.ls)):
            if self.ls[i] == None:
                self.ls.pop(self.ls[i])

    def getSize(self) -> int:
        return len(self.ls)
    
    def getCapacity(self) -> int:
        return len(self.ls)