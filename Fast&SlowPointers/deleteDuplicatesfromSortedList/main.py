from typing import Optional

class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[listnode]) -> Optional[listnode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    
if __name__ == "__main__":
    head = listnode(1)
    head.next = listnode(1)
    head.next.next = listnode(2)
    
    sol = Solution()
    result = sol.deleteDuplicates(head)
    
    curr = result
    while curr:
        print(f"{curr.val}", end="")
        curr = curr.next
    print("None")