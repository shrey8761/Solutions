class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result, max_time = 0, 0
        
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                if neededTime[i] > neededTime[i+1]: 
                    result += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
                else:
                    result += neededTime[i]

        return result