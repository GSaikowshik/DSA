class Solution:
    def isAnagramm(self,s:str,t:str)->bool:
        if len(s) != len(t):
            return False
        l={}
        for m in s:
            if m in l:
                l[m] += 1
            else:
                l[m] = 1
        for m in t:
            if m not in l:
                return False
            elif l[m] == 1:
                del l[m]
            else:
                l[m] -= 1
        return True
if __name__ == "__main__":
    s = "rat"
    t = "car"
    sol=Solution()
    k=sol.isAnagramm(s,t)
    print(k)