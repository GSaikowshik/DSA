from typing import Optional

class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in h:
                return [i, h[y]]
            else:
                h[x] = i
        return []
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
    input_arr = [2, 7, 11, 13,15]
    target = 9
    result = sol.twoSum(input_arr, target)
    print(f"Two Sum Output: {result}") 
    head = sol.create_linkedlist(input_arr)
    print(f"Linked List created successfully! Head value: {head.val}")