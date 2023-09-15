class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        set<vector<int>>st;
        for(int i=0;i<nums.size();i++){
            int j=i+1, k=nums.size()-1, tar=-nums[i];
            while(j<k){
                if((nums[j]+nums[k])==tar){
                    st.insert({nums[i], nums[j], nums[k]});
                    j++;
                }
                else if((nums[j]+nums[k])<tar)
                    j++;
                else
                    k--;
                    
            }
        }
        return vector<vector<int>>(st.begin(), st.end());
    }
};