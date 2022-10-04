class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
	
        //sorting the vector
        sort(nums.begin(),nums.end());
        
        int unique=0;
		
		//size of array
        int x=nums.size();
		
		
		//as the first is always unique
        nums[unique]=nums[0];
        unique++;
        for(int i=1;i<x;i++){
		
			//if the current element is equal to previous then skip
            if(nums[i-1]==nums[i]){}
			
			//otherwise update in the array with the unique pointer
            else{
                nums[unique]=nums[i];
                unique++;
            }
        }
		
		//return no. of unique elements
        return unique;
    }
};