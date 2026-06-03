class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=s[::-1]
        count=0
        for i in range(len(t)-1):
            if t[i] == " ":
                continue
            elif t[i].isalpha():
                count+=1
                if t[i+1] ==" ":
                    return count
                


        