def ascending_order(arr):
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1=[1,4,7]
    arr2=[9,6,3,4,0]
    print("The largest number in arr1:",ascending_order(arr1))
    print("The largest number in arr1:",ascending_order(arr2))