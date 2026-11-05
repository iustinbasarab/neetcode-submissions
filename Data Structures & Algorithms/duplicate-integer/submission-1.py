class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listd = {}
        for i in nums:
            listd[i] = listd.get(i, 0) + 1
            if listd[i] == 2:
                return True
        return False