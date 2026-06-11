class Solution:
    def pattern1(self, N):
        for i in range(N):
            for j in range(N):
                print("*",end="")
            print()

sol = Solution()
N = int(input()) 
sol.pattern1(N)  