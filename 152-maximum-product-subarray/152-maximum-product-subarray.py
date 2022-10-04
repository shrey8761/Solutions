class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = nums[0]
        temp = 1
        for num in nums:
            temp *= num
            ans = max(ans,temp)
            if temp == 0:
                temp = 1
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            temp *= nums[i]
            ans = max(ans,temp)
            if temp == 0:
                temp = 1
        return ans