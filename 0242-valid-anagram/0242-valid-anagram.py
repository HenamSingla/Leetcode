class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s={}
        for i in s:
            if i in map_s.keys():
                map_s[i]+=1
            else:
                map_s[i]=1
        
        map_t={}
        for j in t:
            if j in map_t.keys():
                map_t[j]+=1
            else:
                map_t[j]=1
        
        if map_s==map_t:
            return True
        return False