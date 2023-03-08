class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long mx = *max_element(piles.begin(), piles.end());
        long long b = 1, e = mx;
        long long ans = mx;
        while (b <= e) {
            long long k = (b + e) / 2;
            // cout << k << " ";
            
            long long tmp = 0;
            for (int ele: piles) {
                tmp += ceil((double) ele / k);
            }

            if (tmp <= h) {
                e = k - 1;
                ans = min(ans, k);
            } else {
                b = k + 1;
            }
        }
        return ans;
    }
};