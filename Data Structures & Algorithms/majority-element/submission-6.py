class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate , countt = 0,0

        for i in nums:
            if countt ==0:
                candidate =i
            countt +=(1 if i == candidate else -1)

        return candidate

        