class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dset = set()

        for i in nums:
            if i in dset:
                return True
            dset.add(i)
        return False
        
# so we could've used for loop or even sorting but the using a hashset is the most efficient in terms of tc even though we had to comprise on sc i.e,O(n)=