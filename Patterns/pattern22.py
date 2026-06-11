class Solution:
    def pattern(self,N):
        for i in range(2*N-1):
            for j in range(2*N-1):
                top=i
                bottom=j
                left=(2*N-2)-i
                right=(2*N-2)-j
                min_value=min(top,bottom,left,right)
                print(min_value,end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    sol.pattern(N)