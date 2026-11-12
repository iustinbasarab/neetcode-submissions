class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max = 0
        for x in s: 
           if x - 1 not in s:
            start = x
            k = 1
            while start + 1 in s:
                k+=1
                start += 1
            if k > max : 
                max = k
        return max
            
