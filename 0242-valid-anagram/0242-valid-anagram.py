class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}      
        for i in s:
            if i not in s_dict.keys():
                s_dict[i]=1
            s_dict[i]+=1

        t_dict={}      
        for j in t:
            if j not in t_dict.keys():
                t_dict[j]=1
            t_dict[j]+=1
        if s_dict==t_dict:
            return True
        return False
        