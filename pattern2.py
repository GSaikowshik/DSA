class Solution:
    def pattern2(self,N):
        for i in range(N):
            for j in range(i+1):
                print("*",end="")
            print()
sol=Solution()
N=int(input())
sol.pattern2(N)