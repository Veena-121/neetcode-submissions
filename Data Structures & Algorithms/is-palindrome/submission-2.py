class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr=""
         
        for c in s:
            if c.isalnum():
                strr+= c.lower()
        return strr == strr[::-1]

        