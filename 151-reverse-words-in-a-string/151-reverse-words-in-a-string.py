class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        res = ""
        for i in range(len(a)-1,-1,-1):
            res = res + a[i] + " "
            
        return res[:len(res)-1]
        