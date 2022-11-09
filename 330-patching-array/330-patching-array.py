class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered=0
        res=0
        for num in nums:
            while num>covered+1:
                res+=1
                covered=covered*2+1
                if covered>=n:
                    return res
            covered+=num
            if covered>=n:
                return res
        while covered<n:
            res+=1
            covered=covered*2+1            
        return res