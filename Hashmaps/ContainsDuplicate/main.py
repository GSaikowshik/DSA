class Solution:
    def containDuplicate(self,nums:int)->bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
if __name__ == "__main__":
    nums=[1,2,3,1,2]
    sol=Solution()
    k=sol.containDuplicate(nums)
    print(k)