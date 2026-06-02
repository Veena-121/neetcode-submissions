class Solution:
    def isPalindrome(self, s: str) -> bool:

       
        mys="".join(i for i in s if i.isalnum())
        mys =mys.lower()
        l=0
        r=len(mys)-1

        while r>l:
            if mys[r] != mys[l]:
                return False
            l+=1
            r-=1
        return True

        