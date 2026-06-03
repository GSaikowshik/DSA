class Solution:
    def pattern5(self,N):
        for i in range(N):
            for j in range(N,i,-1):
                print("*",end="")
            print()
sol=Solution()
N=int(input())
sol.pattern5(N)