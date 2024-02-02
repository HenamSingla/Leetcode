class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        dict= {}
        
        for j in ransomNote:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
                
                
        for i in magazine:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for letter in dict:
            if letter not in dic:
                return False
            if dict[letter] > dic[letter]:
                return False
            
        return True
            
            

        