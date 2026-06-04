class Solution:
    def pattern12(self, N):
        spaces = 2 * (N - 1)
        for i in range(N):
            for j in range(1, i+1):
                print(j, end="")
            for j in range(spaces):
                print(" ", end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces -= 2
if __name__ == "__main__":
    sol = Solution()
    N = int(input(""))
    sol.pattern12(N)