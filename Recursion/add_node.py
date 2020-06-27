class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is not None:
            current = self.head
            while(self.head):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

new_list = LinkedList()
new_list.insert(5)
new_list.insert(6)