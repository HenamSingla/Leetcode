class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana={}
        for i in strs:
            new=''.join(sorted(i))
            if new in ana:
                ana[new].append(i)
            else:
                ana[new]=[i]
        return list(ana.values())
             

           