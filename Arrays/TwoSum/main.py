class Solution:
    def two_sum_exists(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return "YES"
        return "NO"

    def two_sum_indices(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14
    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))