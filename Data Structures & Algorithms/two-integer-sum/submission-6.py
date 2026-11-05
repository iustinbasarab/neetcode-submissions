class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i,n in enumerate(nums):
            dif = target - n
            if dif in dct:
                return [dct[dif],i]
            dct[n]=i

        