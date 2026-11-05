class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]
        else:
            grupuri = {}
            for cuv in strs:
                cheie = tuple(sorted(cuv))
                if cheie not in grupuri:
                    grupuri[cheie] = []
                grupuri[cheie].append(cuv)
            return list(grupuri.values())
                
        