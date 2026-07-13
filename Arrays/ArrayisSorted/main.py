def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True

n = int(input("Enter the size of the array: "))

arr = []
print(f"Enter the {n} elements of the array:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)
ans = isSorted(arr, n)
if ans:
    print("True")
else:
    print("False")