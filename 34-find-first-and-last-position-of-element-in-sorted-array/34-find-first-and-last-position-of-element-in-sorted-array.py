class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] <= target:
        #         if nums[i] == target:
        #             res.append(i)
        # if len(res) == 1:
        #     res.append(res[0])
        # if [] == res:
        #     res.append(-1)
        #     res.append(-1)
        # return res
        
        

        # res = []
        # d = defaultdict(list)
        # ans = []
        # d={'a':[-1,-1], target : ans}
        
        # s = 0
        # e = len(nums)
        # mid = s + e // 2
        # while s<=e:
        #     if nums[mid] < target:
        #         s = mid + 1
        #     elif nums[mid] > target:
        #         e = mid -1
        #     elif nums[mid] == target:
        #         d[target].append(mid)
        # res.append[target][0]
        # res.append[target][-1]
        # if res == []:
        #     res.append(d[a])
        # return res
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
                if nums[i] == target:
                    res.append(i)
                    break
        if len(res) == 0:
            res.append(-1)
            res.append(-1)
            return res
        return [res[0],res[-1]]
            
    
        
        
        
        