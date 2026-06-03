class Solution:
    def validPalindrome(self, s: str) -> bool:

        flag=0
        l=0
        r=len(s)-1
        for i in range(len(s)):
            if flag >1 :
                return False
            if s[l] != s[r]:
                flag +=1
        return True
            
        