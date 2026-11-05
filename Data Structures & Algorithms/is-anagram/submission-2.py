class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vazute = {}
        for c in s:
            vazute[c]=vazute.get(c,0)+1
        for c in t:
            if c not in vazute:
                return False
            else:
                vazute[c]=vazute.get(c,0)-1
        for c in vazute:
            if vazute[c] != 0:
                return False
        return True