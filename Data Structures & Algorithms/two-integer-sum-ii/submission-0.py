class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        k=len(numbers)-1
        while i<k:
            if numbers[i] + numbers[k] > target:
                k-=1
            elif numbers[i] + numbers[k] < target:
                i+=1
            else :
                return [i+1,k+1]
        