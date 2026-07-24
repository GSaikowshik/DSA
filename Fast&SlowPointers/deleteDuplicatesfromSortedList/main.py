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
    def create_linkedlist(self,arr:list[int])->Optional[listnode]:
        if not arr:return None
        head=listnode(arr[0])
        curr=head
        for val in arr[1:]:
            curr.next=listnode(val)
            curr=curr.next
        return head
    def linkedlist_to_array(self, head: Optional[listnode])-> list[int]:
        result=[]
        curr=head
        while curr:
            result.append(curr.val)
            curr=curr.next
        return result    
if __name__ == "__main__":
    sol = Solution()
    input_arr = [1,1,2,2,3,3,4,4]
    head = sol.create_linkedlist(input_arr)
    result = sol.deleteDuplicates(head)
    print(sol.linkedlist_to_array(result))