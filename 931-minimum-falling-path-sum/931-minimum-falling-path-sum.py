class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        dp= []
        for i in range(0,n):
            arr = []
            for j in range(0,n):
                arr.append(-1)
            dp.append(arr)
        
        mini = float(inf)
        for i in range(n):
            mini = min (mini, findmin(0,i,matrix,dp))
        return mini
    
def findmin(cr,cc, matrix ,dp):
    n = len(matrix[0])
    if cr>n-1 or cc > n-1 or cc < 0 or cr <0:
        return float(inf)

    if cr == n-1:
        return matrix[cr][cc]

    if dp[cr][cc] != -1:
        return dp[cr][cc]

    down = findmin(cr+1,cc,matrix,dp)
    downleft = findmin(cr+1,cc-1,matrix,dp)
    downright = findmin(cr+1,cc+1,matrix,dp)
    dp[cr][cc] = matrix[cr][cc] + min(down , min(downleft,downright))
    return dp[cr][cc]
    
    