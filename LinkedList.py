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
        my_list = []
        while current:
            my_list.append(current.data) 
            current = current.next

        expo = len(my_list)-1
        decimal = 0

        for i in range(0,len(my_list)):
            decimal = decimal + my_list[i]*(2**expo)
            expo=expo-1

        print(decimal)

list = LinkedList()
list.insertAtBegin(0)
list.insertAtBegin(0)
list.insertAtBegin(1)

list.printL()








