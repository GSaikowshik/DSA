class Solution:
    def Reverse_String(self,s:list[str])-> None:
        n=len(s)
        l=0
        r=n-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l += 1
            r -= 1
        return
if __name__ == "__main__":
    sol=Solution()
    s=["h","e","l","l","o"]
    sol.Reverse_String(s)
    print(s)