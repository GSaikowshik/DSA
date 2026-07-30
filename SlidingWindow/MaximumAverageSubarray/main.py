class Solution:
    def MaxAverage(self,nums:list[int],k:int)->float:
        n=len(nums)
        sum=0
        for i in range(k):
            sum+=nums[i]
            max_avg=sum/k
        for i in range(k,n):
            sum+=nums[i]
            sum-=nums[i-k]
            avg=sum/k
            max_avg=max(max_avg,avg)
        return max_avg
if __name__=="__main__":
    nums=[1,12,-5,-6,50,3]
    k=4
    sol=Solution()
    k=sol.MaxAverage(nums,k)
    print(k)