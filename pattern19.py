class Solution:
    def upper_side(self,N):
        for i in range(N):
            for j in range(N-i):
                print("*",end="")
            for j in range(2*i):
                print(" ",end="")
            for j in range(N-i):
                print("*",end="")
            print()
    def lower_side(self,N):
        for i in range(N):
            for j in range(i+1):
                print("*",end="")
            for j in range(2*N-(2*i+2)):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.upper_side(N)
    sol.lower_side(N)