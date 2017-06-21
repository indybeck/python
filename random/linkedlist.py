#singly linked list
class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def setHead(self, head):
		self.head = head

	def insert_at_front(self, data):
		a_node = Node()
		if self.head:
			a_node = Node().setNext(self.head)

		a_node.setData(data)
		self.setHead(a_node)
		