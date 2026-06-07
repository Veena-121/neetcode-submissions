class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = nums[0]
        countt=0

        for i in range(len(nums)):
            if nums[i] == candidate:
                countt +=1
            elif nums[i] != candidate:
                countt -=1
            elif countt == 0:
                nums[i] = candidate

        return candidate

        