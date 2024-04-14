class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printL(self):
        current =  self.head
        decimal=0
        while current:
            decimal=decimal*2+ current.data
            current = current.next
        print(decimal)

list = LinkedList()
list.insertAtBegin(1)
list.insertAtBegin(0)
list.insertAtBegin(1)

list.printL()








