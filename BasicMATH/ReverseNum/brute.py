class Solution:
    def ReverseNUM(self,N):
        revNUM=0
        while N > 0:
            last_digit=N%10
            revNUM=revNUM*10+last_digit
            N=N//10
        return revNUM
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    print(sol.ReverseNUM(N))