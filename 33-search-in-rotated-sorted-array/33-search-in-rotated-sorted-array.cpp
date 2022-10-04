class Solution {
public:
    
    int ptOfrotation (vector<int>& nums)
    {
        int start=0;
        int end=nums.size()-1;
        
        while(start<=end)
        {
            int mid=start+(end-start)/2;
            
            if(mid>=nums.size()-1 || nums[mid]>nums[mid+1] )
                return mid;
            
            if(nums[mid]>=nums[0])
                start=mid+1;
            
            else 
                end=mid-1;
        }
        
        return nums.size()-1;
    }
    
    int binary_search(vector<int>& nums, int target,int start,int end)
    {
        
        while(start<=end)
        {        
        int mid=start+(end-start)/2;
        
        if(nums[mid]==target)
            return mid;
            
        else if(nums[mid]>target)
            end=mid-1;
            
        else
            start=mid+1;
        }
        
        return -1;
        
    }
    
    
    int search(vector<int>& nums, int target) {
        
        int start=0;
        int end=nums.size()-1;
        int n=nums.size()-1;
        int ans1=-1;
        int ans2=-1;
        
        if(nums[start]==target)
            return start;
        
        else if(nums[end]==target)
            return end;
        
        if(start==end && nums[start]!=target)
            return -1;
        
       int por=ptOfrotation(nums);
        // int por=8;
        
       ans1= binary_search(nums,target,start,por);
        // cout<<ans1;
        
       if(ans1!=-1 || por!=nums.size()-1)
       ans2=binary_search(nums,target,por+1,end);
        
        // cout<<ans2;
        
       if(ans1==-1 && ans2==-1)
           return -1;
        
       if(ans1!=-1)
           return ans1;
        
       else
           return ans2;
        
    }
};