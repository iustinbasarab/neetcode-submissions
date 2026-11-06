class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rez = {}
        for i in nums:
            rez[i]=rez.get(i,0)+1
        return sorted(rez,key=rez.get,reverse=True)[:k]
            
            