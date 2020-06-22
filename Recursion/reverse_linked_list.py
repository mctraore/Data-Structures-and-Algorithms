class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        
        prev = head
        current = head.next
        
        while current!= None:
      
            if prev == head:
               
                prev.next = None    
            temp = current.next
        
            current.next = prev
           
            prev = current
       
            current = temp
 
        return prev