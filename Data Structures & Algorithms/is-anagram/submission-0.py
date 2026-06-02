class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s_map ={}
            for ch in s:
                s_map[ch] = s_map.get(ch,0)+1

            t_map ={}
            for ch in t:
                t_map[ch] = t_map.get(ch,0)+1

            for ch in s_map:
                if s_map[ch] != t_map.get(ch,0):
                    return False
            return True
        return False

        