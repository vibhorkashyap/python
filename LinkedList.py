class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def insertAtHead(self,Node):
        if self.head is None:
            self.head = Node
        else:
            temp = self.head
            self.head = Node
            self.head.next = temp

    def insertAtTail(self,Node):
        if self.head is None:
            self.head = Node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node

    def deleteByValue(self,value):
        temp = self.head
        if value == self.head.data:
            return None
        else:
            while(temp.next.data != value):
                temp = temp.next
            if temp.next != None:
                temp.next = temp.next.next
            else:
                temp.next = None


    def deleteHead(self):
        if self.head is None :
            return None
        elif self.head.next is None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp = None


    def deleteTail(self):
        temp = self.head
        if temp.next is None:
            return temp
        else:
            while(temp.next.next != None):
                temp = temp.next
            temp.next.next = None
            temp.next = None


    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
       


LL = LinkedList()
for i in range(10):
    LL.insertAtTail(Node(i))

LL.printList()
print("###################")

LL.deleteByValue(7) #deletes 4
LL.deleteTail() #deletes 9
LL.deleteTail() #deletes 8
LL.deleteHead() #deletes 0
LL.printList()
