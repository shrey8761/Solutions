class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        m = len(strs)
        ans = 0
        for i in range(n):
            for j in range(1,m):
                if strs[j][i] <  strs[j-1][i]:
                    # print(strs[j][i])
                    ans+=1
                    break
        return ans
        