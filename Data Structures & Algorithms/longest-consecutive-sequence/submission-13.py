class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for x in s: 
           if x - 1 not in s:
            start = x
            k = 1
            while start + 1 in s:
                k+=1
                start += 1
            if k > maxi : 
                maxi = k
        return maxi
            
