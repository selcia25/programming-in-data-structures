class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            self.last_node.next = self.head
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp, end = " ")
            temp = temp.next
            if temp == self.head:
                break
        print()
if __name__ == "__main__":
    l = CircularLinkedList()
    l.append(2)
    l.append(3)
    l.append(4)
    print(l.display())