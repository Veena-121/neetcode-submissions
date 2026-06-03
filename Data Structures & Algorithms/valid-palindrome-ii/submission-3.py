class Solution:
    def validPalindrome(self, s: str) -> bool:

        l=0
        r=len(s)-1
        while r>l:
            if s[l] != s[r]:
                skipl , skipr = s[l+1:r+1], s[1:r]
                return (skipl == skipl[::-1] or skipr == skipr[::-1])
            l,r = l+1 , r-1
        
              
        return True
            
        