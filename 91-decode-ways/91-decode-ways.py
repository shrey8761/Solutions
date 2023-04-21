class Solution:
    def numDecodings(self,s): 
# def num_ways_to_decode(s):
    # Check if the input string is empty or starts with 0
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 # There is only one way to decode an empty string
        dp[1] = 1 # There is only one way to decode a single-digit string

        for i in range(2, n+1):
            # If the current digit can be decoded by itself, we can add the number of ways to decode the previous digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # If the current digit and the previous digit can be decoded as a single letter, we can add the number of ways to decode the two digits before the current digit
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n] # Return the number of ways to decode the entire string
