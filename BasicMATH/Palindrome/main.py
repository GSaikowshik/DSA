class Solution:
    def Palindrome(self,N):
        rev=0
        while N>0:
            last_digit=N%10
            rev=rev*10+last_digit
            N=N//10
        return rev
if __name__ == "__main__":
    sol=Solution()
    N=int(input())
    reverseNum=sol.Palindrome(N)
    if N == reverseNum :
        print("IT IS PALINDROME")
    else:
        print("IT IS NOT PALIDROME")