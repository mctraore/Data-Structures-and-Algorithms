class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        current = self.head
        for i in range(position-1):
            current = current.next
            if not current:
                return None
        return current
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

    
    def insert(self, new_element, position):
        if position ==1:
            new_element.next = self.head
            self.head = new_element
        else:
            current = self.head
            for i in range(position-2):
                current = current.next
                if not current:
                    return None
            temp = current.next
            new_element.next = temp
            current.next  = new_element
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass
    
    
    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.val == value:
                    current.next = current.next.next
                    
        """Delete the first node with a given value."""
        pass