// int fn(int pos, vector<int> &coins, int target, vector<vector< int>> &dp)
// {
//    	//base
//     if (pos == 0)
//     {
//         if (target % coins[0] == 0)
//         {

//             return dp[pos][target] = target / coins[0];
//         }
//         else
//         {
//             return 1e9;
//         }
//     }

//    	//logic
//     if (dp[pos][target] != -1)
//     {
//         return dp[pos][target];
//     }
//     int nottake = fn(pos - 1, coins, target, dp);
//    	//1E9
//     int take = 1e9;
//     if (target >= coins[pos])
//     {
//         take = fn(pos, coins, target - coins[pos], dp) + 1;
//     }

//     return dp[pos][target] = min(take, nottake);

// }
class Solution
{
    public:
        int coinChange(vector<int> &coins, int amount)
        {
            vector<vector < int>> dp(coins.size(), vector<int> (amount + 1, 0));

            for (int target = 0; target <= amount; target++)
            {
                if (target % coins[0] == 0)
                {
                    dp[0][target] = target / coins[0];
                }
                else
                {
                    dp[0][target] = 1e9;
                }
            }

           	//iterate -> table create
           	//row -> position, cl->target
            for (int pos = 1; pos < coins.size(); pos++)
            {
                for (int target = 0; target <= amount; target++)
                {
                    int nottake = dp[pos - 1][target];
                   	//1E9
                    int take = 1e9;
                    if (target >= coins[pos])
                    {
                        take = dp[pos][target - coins[pos]] + 1;
                    }

                    dp[pos][target] = min(take, nottake);
                }
            }

            int ans =  dp[coins.size() - 1][amount];

           	// int ans = fn(coins.size() - 1, coins, amount,dp);

           	// for(int i = 0; i < coins.size(); i++){
           	//     for(int j =0; j<=amount;j++){
           	//         cout<<dp[i][j] << " ";
           	//     }
           	//     cout<<endl;
           	// }

            if (ans >= 1e9)
            {
                return -1;
            }
            return ans;
        }
};