class Solution:
    def upward_pyramid(self,N):
        for i in range(N):
            for j in range(N-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            for j in range(N-i-1):
               print(" ",end="")
            print()  
    def inverted_pyramid(self,N):   
        for i in range(N):
            for j in range(i):
                    print(" ",end="")
            for j in range(2*N-(2*i+1)):
                    print("*",end="")
            for j in range(i):
                    print(" ",end="")
            print()
            
if __name__=="__main__":
    sol=Solution()
    N=int(input())
    sol.upward_pyramid(N)
    sol.inverted_pyramid(N)