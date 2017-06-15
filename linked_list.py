class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

	def setData(data):
		self.data = data
	def getData(self):
		return self.data
	def setNext(next):
		self.next = next
	def getNext(self):
		return self.next

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.count = 0

	def insertAtBeg(data):
		if self.head == None:
			newNode = Node(data)
			self.head = newNode
			self.count += 1
		else:
			newNode = Node(data)
			newNode.next = self.head
			self.head = newNode
			self.count += 1

	def printListSize(self):
		print ("%d items in list" %self.count ) 

	def insertAtEnd(data):
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = Node(data)
		self.count += 1

	def deleteNode(data):
		curr = self.head
		if self.head == None:
			print ( "No items in list to delete")
		while curr.next.data != data:
			curr = curr.next 
		curr.next = curr.next.next


	def printList(self):
		curr = self.head
		while curr != None:
			print(curr.data)
			curr = curr.next

li = LinkedList()
li.insertAtBeg(2)
li.insertAtEnd(3)
li.insertAtEnd(4)
li.printListSize()
li.printList()
li.deleteNode(3)
li.printList()
