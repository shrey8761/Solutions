class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        track = []
        ans = []
        def backtrack(s, i):
            if i == len(s) :
                ans.append(" ".join(track))
                return
            for word in wordDict:
                n = len(word)
                if s[i:].startswith(word):
                    track.append(word)
                    backtrack(s,i + n)
# <!-- Here if I put track.remove(word), it can not go through the "aaaaaaa" case -->
                    track.pop()
        backtrack(s, 0)
        return ans
            
