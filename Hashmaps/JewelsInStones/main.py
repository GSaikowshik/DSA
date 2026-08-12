class Solution:
    def numJewelsInStones(self,jewels:str,stones:str)->int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
if __name__ == "__main__":
    jewels="aA"
    stones="aAAbbbb"
    sol=Solution()
    k=sol.numJewelsInStones(jewels,stones)
    print(k)
