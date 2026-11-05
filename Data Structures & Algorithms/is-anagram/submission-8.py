class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fr = [0] * 26
        for i in range(len(s)):
            fr[ord(s[i])-ord('a')]+=1
            fr[ord(t[i])-ord('a')]-=1
        return fr == [0] * 26