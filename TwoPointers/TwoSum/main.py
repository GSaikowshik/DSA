class Solution:
    def TwoSum(self, nums: list[int],target:int) -> list[int]:
        n=len(nums)
        l=0
        r=n-1
        while l<r:
          sum=nums[l]+nums[r]
          if sum==target :
             return[l+1,r+1]
          elif sum<target:
             l +=1
          else:
             r -=1
        return
if __name__ == "__main__":
   sol=Solution()
   target=9
   nums=[2,7,11,15]
   print(sol.TwoSum(nums,target))
   