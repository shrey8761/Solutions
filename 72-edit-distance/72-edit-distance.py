class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        memo={}
        
        def getMinDistance(i,j):
            if i<0 and j<0:
                return 0
            elif i<0:
                return j+1
            elif j<0:
                return i+1
            key=(i,j)
            if key in memo:
                return memo[key]
            if w1[i]==w2[j]:
                memo[key]= 0+getMinDistance(i-1,j-1)
            else:
                # replace
                replace=1+getMinDistance(i-1,j-1)
                # remove
                remove=1+getMinDistance(i-1,j)
                #add
                add=1+getMinDistance(i,j-1)
                
                memo[key]=min(replace,remove,add)
            return memo[key]
        
        return getMinDistance(len(w1)-1,len(w2)-1)
