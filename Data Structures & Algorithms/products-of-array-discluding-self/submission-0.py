class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stanga = [1]*n
        dreapta = [1]*n
        for i in range(1,n):
            stanga[i] = stanga[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            dreapta[i] = dreapta[i+1]*nums[i+1]

        return [stanga[i] * dreapta[i] for i in range(n)]
        