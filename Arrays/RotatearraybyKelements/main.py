def Rotate_array_by_K_elements(arr,k):
        temp = arr[k]
        for i in range(1, len(arr)):
               
         



n = int(input("Enter the size of the array: "))

arr = []
print(f"Enter the {n} elements of the array:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)
    k=int(input())

    Rotate_array_by_K_elements(arr,n)
print(arr)