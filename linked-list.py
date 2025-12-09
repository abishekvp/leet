class MyLinkedList:
    def __init__(self):
        self.values = []

    def get(self, index: int) -> int:
        return self.values[index]

    def addAtHead(self, val: int) -> None:
        self.values.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.values.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        # self.values = self.values[:index] + [val] + self.values[index:]
        self.values.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        self.values.pop(index)

linked_list = MyLinkedList()
linked_list.values = [1, 2, 3, 4, 5]
linked_list.addAtIndex(index=1, val=10)
print(linked_list.get(index=1))
