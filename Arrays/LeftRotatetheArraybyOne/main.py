def Left_Rotate_the_Array_by_One(arr,self):
        temp = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
        
        arr[-1] = temp



n = int(input("Enter the size of the array: "))

arr = []
print(f"Enter the {n} elements of the array:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)
    Left_Rotate_the_Array_by_One(arr,n)
print(arr)