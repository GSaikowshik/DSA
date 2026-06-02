class Solution:
    def pattern4(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i,end="")
            print()
sol=Solution()
N=int(input())
sol.pattern4(N)