class Solution:
    def primeNum(N):
        if N%2==0:
            print("Not a Prime Number")
        else:
            print("Prime Number")
if __name__ == "__main__":
    N=int(input())
    Solution.primeNum(N)
    