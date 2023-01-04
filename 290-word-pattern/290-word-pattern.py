class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wp = s.split()
        if len(pattern) != len(wp):
            return False

        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d: #this means key not there.
                if wp[i] in d.values(): #this means key is not , but value is there.
                     return False
                d[pattern[i]] = wp[i]
            elif d[pattern[i]] != wp[i]:
                return False
        return True
            
        