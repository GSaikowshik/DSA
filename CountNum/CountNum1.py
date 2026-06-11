def CountNum(N):
    count=0
    while N>0:
        count += 1
        N=N//10
    return count
if __name__ == "__main__":
    N=int(input())
    print("N:",N)
    num_digits=CountNum(N)
    print("Number of digits:",num_digits)

