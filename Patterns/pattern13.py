class Solution:
    def pattern13(self,N):
        num=1
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(num,end="")
                num += 1
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.pattern13(N)