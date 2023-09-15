class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        vector<int>l(n), r(n);
        int m1=0, m2=0, res=0;
        for(int i=0;i<n;i++){
            m1=max(m1, height[i]);
            l[i]=m1;
        }
        for(int i=n-1;i>=0;i--){
            m2=max(m2, height[i]);
            r[i]=m2;
        }
        for(int i=0;i<n;i++){
            res+=min(l[i], r[i])-height[i];
        }
        return res;
    }
};