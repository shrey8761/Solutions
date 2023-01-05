# class Solution:
#     def frequencySort(self, s: str) -> str:
#         out = ''
#         for i, j in Counter(s).most_common():
#             out += i*j

#         return out




class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        d = c.most_common()
        
        temp = ''
        for i,j in d:
            temp += i*j
        return temp