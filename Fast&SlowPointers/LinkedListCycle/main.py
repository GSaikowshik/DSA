from typing import Optional

class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[listnode]) -> bool:
        dummy = listnode()
        dummy.next = head
        slow = fast = dummy
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
                
        return False
        
    def create_linkedlist(self, arr: list[int]) -> Optional[listnode]:
        if not arr: return None
        head = listnode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = listnode(val)
            curr = curr.next
        return head

if __name__ == "__main__":
    sol = Solution()
    input_arr = [1,2,3,5]
    head = sol.create_linkedlist(input_arr)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = head.next 
    result = sol.hasCycle(head)
    print(f"Output: {result}") 
    