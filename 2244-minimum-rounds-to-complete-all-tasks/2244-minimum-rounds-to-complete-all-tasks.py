class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d={}
        for i in range(len(tasks)):
            if tasks[i] in d:
                d[tasks[i]] += 1
            else:
                d[tasks[i]] = 1
        ans = 0        
        for i in d.values():
            if i == 1:
                return -1
            temp_3 = (i-2)//3
            temp_2 = (i-temp_3*3)//2
            ans += temp_3 + temp_2
            
        return ans
                
                