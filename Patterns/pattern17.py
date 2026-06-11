class Solution:
    def pattern17(self, N):
        for i in range(N):
            for j in range(N - i - 1):
                print(" ", end="")
            
            alpha = ord("A")
            breakpoint = i
            
            for j in range(2 * i + 1):
                print(chr(alpha), end="")
                if j < breakpoint:
                    alpha += 1
                else:
                    alpha -= 1
            
            print()

if __name__ == "__main__":
    sol = Solution()
    N = int(input())
    sol.pattern17(N)