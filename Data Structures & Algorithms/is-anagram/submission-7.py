class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap={}
        tmap={}
        
        for i in s:
            smap[i] = smap.get(i,0)+1
        
        for i in t:
            tmap[i] = tmap.get(i,0)+1

        for i in smap:
            if smap[i] != tmap.get(i):
                return False
        return True
