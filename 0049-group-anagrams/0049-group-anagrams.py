class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new={}
        for s in strs:
            anag= ''.join(sorted(s))
            if anag in new:
                new[anag].append(s)
            else:
                new[anag]=[s]
    return list(new.values())

