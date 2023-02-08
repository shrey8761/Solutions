from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        a = defaultdict()
        a = {'(':')','{':'}','[':']'}
        opn = ['(','{','[']
        st = [0]
        for i in s:
            if i in opn:
                st.append(a[i]) 
            elif st[-1] == i: 
                st.pop()
            else:
                return False 
        return  [0] == st
                
        