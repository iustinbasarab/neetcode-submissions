class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        vazute = {}
        for c in s:
            vazute[c] = vazute.get(c, 0) + 1
        for c in t:
            if c not in vazute or vazute[c] == 0:
                return False
            vazute[c] -= 1
        return True