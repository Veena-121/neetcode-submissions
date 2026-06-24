class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=1,n-2
        if nums[0] > nums[1]:
            return l
        elif nums[n-1]> nums[n-2]:
            return n-1

        while l<=r:
            m = l+(r-l)//2
            if nums[m-1]<nums[m] and nums[m]>nums[m+1]:
                return m
            elif nums[m] > nums[m-1]:
                l=m+1
            else:
                r=m-1
        return -1

        