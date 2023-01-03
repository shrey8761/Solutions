class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s_len = len(strs[0])
        ans = 0
        for i in range(s_len):
            n_s = ""
            for s in strs:
                n_s = n_s + s[i]
            #print(sorted(n_s))
            if n_s != "".join(sorted(n_s)):
                ans += 1
        return ans