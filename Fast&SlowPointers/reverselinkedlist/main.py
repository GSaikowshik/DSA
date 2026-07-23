from typing import Optional

class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverse_linkedlist(self,head:Optional[listnode])->Optional[listnode]:
        curr = head
        prev = None
        while curr and curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def create_linkedlist(self,arr: list[int])-> Optional[listnode]:
        if not arr:return None
        head=listnode(arr[0])
        curr=head
        for val in arr[1:]:
            curr.next=listnode(val)
            curr=curr.next
        return head
    def linkedlist_to_array(self,head:Optional[listnode])-> list[int]:
        result=[]
        curr=head
        while curr:
            result.append(curr.val)
            curr=curr.next
        return result


if __name__ == "__main__":    
    sol = Solution()
    input_arr = [1, 2, 3, 4, 5]
    head = sol.create_linkedlist(input_arr)
    result = sol.reverse_linkedlist(head)
    print(sol.linkedlist_to_array(result))