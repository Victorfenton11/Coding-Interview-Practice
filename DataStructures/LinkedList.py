class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def length(self):
        curr = self.head
        i = 0
        while curr is not None:
            i += 1
            curr = curr.next
        return i
    
    def search(self, value):
        curr = self.head
        i = 0
        while curr is not None:
            if curr.value == value:
                return i
            curr = curr.next
            i += 1
        return -1

    def insertAtEnd(self, value):
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(value)
        return

    def insertAtBeginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        return
    
    def insertAtIndex(self, value, index):
        if index == 0:
            self.insertAtBeginning(value)
            return

        curr = self.head
        i = 0
        while curr is not None:
            if i == index - 1:
                newNode = Node(value)
                newNode.next = curr.next
                curr.next = newNode
                return
            curr = curr.next
            i += 1
        raise IndexError("Index out of range")
    
    def remove(self, value):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value == value:
                if curr == self.head:
                    if curr.next:
                        self.head = curr.next
                    else:
                        self.head = None
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        raise ValueError(f"The value {value} is not in the linked list")
    
    def __str__(self):
        values = []
        curr = self.head
        while curr is not None:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values)

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return
    
llist = LinkedList()
print(llist)
llist.insertAtEnd(1)
print(llist)
llist.insertAtEnd(4)
print(llist)
llist.insertAtEnd(6)
print(llist)
print(llist.length())
llist.remove(1)
print(llist)
print(llist.length())
llist.insertAtEnd(5)
print(llist)
print(llist.search(5))
llist.insertAtEnd(3)
llist.insertAtEnd(230)
llist.reverse()
print(llist)
print(llist.length())
llist.insertAtIndex(11, 0)
print(llist)
llist.insertAtIndex(12, 3)
print(llist)
llist.insertAtIndex(13, 7)
print(llist)
llist.insertAtIndex(14, 9)