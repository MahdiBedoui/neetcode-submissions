class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None  
    
        
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
            curr = self.left.next
            while curr and index > 0:
                curr = curr.next 
                index -= 1 
            if curr and curr != self.right and index == 0:
                return curr.val
            return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next , self.left
        node.prev = prev
        node.next = next 
        prev.next = node 
        next.prev = node
     
    

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev  , self.right 
        prev.next = node 
        next.prev = node
        node.prev = prev
        node.next = next 


    def addAtIndex(self, index: int, val: int) -> None:
            curr = self.left.next 
            while curr and index > 0:
                curr = curr.next
                index -= 1 
            if curr and index == 0:
                node, prev, next = ListNode(val), curr.prev , curr
                prev.next = node 
                next.prev = node
                node.prev = prev
                node.next = next 
    


    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next


          
           


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)