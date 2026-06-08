class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}

        for i in nums:
            hmap[i] = hmap.get(i,0)+1

        for key,val in hmap.items():
            if val >=2:
                return True
        return False
        