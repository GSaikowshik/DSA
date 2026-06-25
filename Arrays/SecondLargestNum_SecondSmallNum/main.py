def ascending_order(arr):
    arr.sort()
    return arr[-2]
def ascending_order2(arr):
    arr.sort()
    return arr[1]
if __name__ == "__main__":
    arr2=[9,6,3,4,0]
    print("The largest number in arr1:",ascending_order(arr2))
    print("The smallest number in arr1:",ascending_order2(arr2))
    