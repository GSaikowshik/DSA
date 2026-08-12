class Solution:
    def ransomNotes(self,ransomeNote:str,magazine:str)->bool:
        s={}
        for i in magazine:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        for i in ransomeNote:
            if i not in s:
                return False
            elif s[i] == 1:
                del s[i]
            else:
                s[i] -= 1
        return True
if __name__ == "__main__":
    sol=Solution()
    ransomNote = "aa"
    magazine = "aab"
    k=sol.ransomNotes(ransomNote,magazine)
    print(k)