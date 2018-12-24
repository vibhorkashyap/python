class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def insertAtHead(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            

    def insertAtTail(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def printList(self):
        arr = []
        curr = self.head
        while curr.next:
            arr.append(curr.data)
            curr = curr.next
        arr.append(curr.data)
        print arr

    def removeNode(self,data):
        prev = None
        curr = self.head
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def reverseList(self):
        prev = None
        curr = self.head
        nex  = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next
        self.head = prev

LL = LinkedList()
for i in range(1,5):
    LL.insertAtTail(i)
LL.printList()
LL.removeNode(3)
LL.printList()
LL.reverseList()
LL.printList()
