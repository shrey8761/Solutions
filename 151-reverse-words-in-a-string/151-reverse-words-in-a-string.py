class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        res = ""
        for i in range(len(a)-1,-1,-1):
            res = res + a[i] + " "
            
        return res[:len(res)-1]
        
        # res = []
        # temp = ""
        # for c in s:
        #     if c != " ":
        #         temp += c 
        #     elif temp != "":
        #         res.append(temp)
        #         temp = ""
        # if temp != "":
        #     res.append(temp)
        # return " ".join(res[::-1])
