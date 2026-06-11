class Solution:
    def pattern14(self,N):
        for i in range(N):
            for j in range(i+1):
                  alpha = chr(ord("A")+j)
                  print(alpha,end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.pattern14(N)