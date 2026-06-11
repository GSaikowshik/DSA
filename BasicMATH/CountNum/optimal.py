import math
def CountNum(N):
      count=int(math.log10(N)+1)
      return count
            
if __name__ == "__main__":
    N=int(input())
    print("Number:",N)
    digits=CountNum(N)
    print("Number of Digits:",digits)
    