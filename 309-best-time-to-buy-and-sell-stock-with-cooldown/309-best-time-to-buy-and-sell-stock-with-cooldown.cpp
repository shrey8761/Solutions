map<pair<int,bool>,int> mp;

int earnMaxProfit(vector<int>& prices,int currIndex,int n,bool buyIt){
    
    if(currIndex >= n)  return 0;
    
    if(mp.find(make_pair(currIndex,buyIt)) != mp.end()) return mp[make_pair(currIndex,buyIt)];
    
    int opt1 = 0;
    int opt2 = 0;
    
    if(buyIt){
        opt1 = -1*prices[currIndex] + earnMaxProfit(prices,currIndex+1,n,false);    
    }else{
        opt1 = prices[currIndex] + earnMaxProfit(prices,currIndex+2,n,true); 
    }    
        
    opt2 = earnMaxProfit(prices,currIndex+1,n,buyIt);
        
    
    return mp[make_pair(currIndex,buyIt)] = max(opt1,opt2);
}

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n = prices.size();
        if(n == 0 || n == 1)    return 0;
        
        mp.clear();
        return earnMaxProfit(prices,0,n,true);
        
    }
};