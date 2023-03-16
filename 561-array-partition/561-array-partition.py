class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return nums[0]
        res = nums[0]

        for i in range(2,len(nums),2):
            res = res + nums[i]
        return res