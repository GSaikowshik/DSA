class Solution:
    def pattern6(self,N):
        for i in range (N):
            for j in range(N,i,-1):
                 print(N-j+1,end=" ")
            print()
sol=Solution()
N=int(input())
sol.pattern6(N)