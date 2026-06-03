class Solution:
    def validPalindrome(self, s: str) -> bool:

        flag=0
        l=0
        r=len(s)-1
        while r>l:
            if flag >1 :
                return False
            if s[l] != s[r]:
                flag +=1
                l+=1
                r-=1
            if s[l] ==s[r]:
                l+=1
                r-=1
        return True
            
        