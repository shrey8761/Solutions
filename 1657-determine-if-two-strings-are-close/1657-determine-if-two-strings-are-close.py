from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1) 
        b = Counter(word2)
        if len(word1) != len(word2):
            return False
        if set(word1) == set(word2):
            if sorted(a.values()) == sorted(b.values()):
                return True
        
        
        