class Solution:
    def top(self,N):
        for i in range(N):
            for j in range(i+1):
                print("*",end="")
            for j in range(2*N-(2*i+2)):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
    def  bottom(self,N):
        for i in range(N-1):
            for j in range(N-i-1):
                print("*",end="")
            for j in range(2*i+2):
                print(" ",end="")
            for j in range(N-i-1):
                print("*",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.top(N)
    sol.bottom(N)