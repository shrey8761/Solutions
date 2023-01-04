class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lyst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        n = len(s)//2
        a = s[0:n]
        b = s[n:]
        count_a = 0
        count_b = 0
        d = {}
        f={}
#         for i in a:
#             if i in lyst:
#                 if i in d.keys():
#                     d[i] += 1
#                 else:
#                     d[i] = 1
                
#         for i in b:
#             if i in lyst:
#                 if i in f.keys():
#                     f[i] += 1
#                 else:
#                     f[i] = 1
#         return d==f
        for i in a:
            if i in lyst: 
                count_a +=1
                
        for i in b:
            if i in lyst: 
                count_b +=1
                
        return count_a==count_b
        