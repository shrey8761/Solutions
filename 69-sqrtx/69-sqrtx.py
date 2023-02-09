class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x==1:
            return x
        i = 0
        while i*i < x:
            i+=1
        return i if i*i == x else i-1
        