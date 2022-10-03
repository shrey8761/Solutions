class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n= colors.length(),gsum = 0, gmax = 0, ans = 0;
        
        for(int i = 0; i<n; i++){
            if(i>0 && colors.charAt(i) != colors.charAt(i - 1)){
                ans += gsum - gmax;
                gsum = 0;
                gmax = 0;
            }
            gsum += neededTime[i];
            gmax = Math.max(gmax, neededTime[i]);
        }
        ans += gsum - gmax;
        return ans;
    }
}