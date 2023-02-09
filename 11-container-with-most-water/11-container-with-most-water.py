class Solution:
    def maxArea(self, h: List[int]) -> int:
#         working brute force
        # res = 0
        # ans = 0 
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         ans = (j-i)*(min(height[i],height[j]))
        #         res = max(res,ans)
        # return res
        
#         OPTIMIZED PICHINIg Window 
        maxwater = 0 # Initialize maximum variable to 0
        l, r = 0, len(h)-1 # Define initial window of maximum size
        while l < r:
            if h[l] <= h[r]:#Find smaller height and shift its pointer inwards
                maxwater = max(maxwater, (r-l) * h[l])
                l+=1
            else:
                maxwater = max(maxwater, (r-l) * h[r])
                r-=1
        return maxwater