class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dset = set()

        for i in nums:
            if i in dset:
                return True
            dset.add(i)
        return False
        