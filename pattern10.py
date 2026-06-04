class Solution:
    def upward_triangle(self,N):
        for i in range(N):
            for j in range(2*i+1):
                print("*",end="")
            print()
    def inverted_triangle(self,N):
        for i in range(N):
            for j in range(2*N-(2*i+1)):
                print("*",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.upward_triangle(N)
    sol.inverted_triangle(N)