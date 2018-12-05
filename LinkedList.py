class Node(object):

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
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def insertAtTail(self,data):

        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)

    def removeNode(self,value):

        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
                    
            prev = curr
            curr = curr.next
            
        return False


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

L = LinkedList()
L.insertAtHead(1)
L.insertAtTail(2)
L.insertAtTail(3)
L.insertAtHead(4)
L.removeNode(3)
L.printList()
