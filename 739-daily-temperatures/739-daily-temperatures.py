class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        id = len(temperatures)-1
        t = temperatures[id]
        ans = [0]
        stack.append(id)
        stack.append(t)
        for i in range(len(temperatures)-2,-1,-1):
            res = 0
            while len(stack) != 0:
                if stack[-1] > temperatures[i]:
                    res = stack[-2] - i
                    break
                else:
                    stack.pop()
                    stack.pop()
            stack.append(i)
            stack.append(temperatures[i])
            ans.append(res)
        ans = ans[::-1]
        return ans
                
            
        
                
                
                