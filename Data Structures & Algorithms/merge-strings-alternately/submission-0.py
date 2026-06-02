class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        r,l=0,0

        while r<len(word1) and l<len(word2):
            ans.extend(word1[r])
            ans.extend(word2[l])
            r+=1
            l+=1
        
        ans.extend(word1[r:])
       
        ans.extend(word2[l:])


        return "".join(ans)
        