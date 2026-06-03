class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        k=0
        for i in range(len(nums1)):
            if nums1[i] ==0 and nums2[k] <= len(nums2):
                nums1[i] = nums2[k]
                k+=1
        nums1.sort()

        