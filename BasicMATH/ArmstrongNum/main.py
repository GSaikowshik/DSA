def ArmstrongNum(N):
    k=len(str(N))
    num=0
    while  N>0:
       ld = N % 10   
       num+=ld**k
       N = N // 10  
    return num == N
if __name__ == "__main__":
 N=int(input("Enter Number:")) 
 if ArmstrongNum(N):
    print(f"{N} is an Armstrong number.")
 else:
    print(f"{N} is not an Armstrong number.") 