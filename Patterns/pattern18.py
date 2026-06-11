class Solution:
    def pattern18(self, N):
        for i in range(N):
            alpha = ord('A') + N-i-1
            for j in range(i + 1):
                print(chr(alpha+ j), end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    N = int(input())
    sol.pattern18(N)
