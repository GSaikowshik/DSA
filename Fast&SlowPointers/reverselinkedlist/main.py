from typing import Optional

class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverse_linkedlist(self,head:Optional[listnode])->Optional[listnode]:
        