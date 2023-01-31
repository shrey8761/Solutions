class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = [s for _, s in sorted(zip(ages, scores))]
        dp = [0] * len(scores)
        for i in range(len(scores) - 1, -1, -1):
            for j in range(i + 1, len(scores)):
                if scores[j] >= scores[i]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += scores[i]
        return max(dp)