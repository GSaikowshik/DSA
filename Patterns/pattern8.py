class Solution:
    def pattern8(self,N):
        for i in range(N):
            for j in range(i):
                print(" ",end="")
            for j in range(2*N-(2*i+1)):
                print("*",end="")
            for j in range(i):
                print(" ",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.pattern8(N)