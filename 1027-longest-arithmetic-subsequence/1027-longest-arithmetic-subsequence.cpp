class Solution {
public:
    int longestArithSeqLength(vector<int>& arr) {
        
        int n = arr.size();
        
        if(n < 3)
        {
            return n;
        }
        
        int maxi = 0;
        
        // declare a dp
        
        vector<vector<int>> dp(n + 1, vector<int> (1005, 0));
        
        // fill dp
        
        for(int i = 0; i < n; i++)
        {
            for(int j = i - 1; j >= 0; j--)
            {
                int diff = arr[i] - arr[j];
                
                int count = dp[j][diff + 500] + 1;
                
                // update maxi
                
                maxi = max(maxi, count);
                
                dp[i][diff + 500] = max(dp[i][diff + 500], dp[j][diff + 500] + 1);
            }
        }
        
        return maxi + 1;
    }
};