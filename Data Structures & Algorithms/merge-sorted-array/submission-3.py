class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        k=0
        for i in range(m-1,len(nums1)):
            if nums1[i] ==0 and k<n:
                nums1[i] = nums2[k]
                k+=1
        nums1.sort()

        