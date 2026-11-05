class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0,len(nums)):
            j=i+1
            while j<len(nums):
                if target != nums[i] + nums[j]:            
                    j+=1
                else:
                    return [i,j]

        