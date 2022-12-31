class Solution {
public:

    int dirR[4]={0,1,0,-1};
    int dirC[4]={1,0,-1,0};
    
    void solve(vector<vector<int>>& grid,int n,int m,int row,int col,vector<vector<int>>& dp,int& ans)
    {
        
     
                
           
        for(int i=0;i<4;i++)
        {
            
            int nr=row+dirR[i];
            int nc=col+dirC[i];
            if(nr<n && nr>=0 && nc<m && nc>=0 && grid[nr][nc]!=-1 && grid[nr][nc]!=1)
            {
                if(grid[nr][nc]==2)
                {
                    int flag=0;
                    for(int i=0;i<n;i++)
                    {
                        for(int j=0;j<m;j++)
                        {
                          
                        if(grid[i][j]==0)flag=1;
                        }
                       
                    }

                    if(!flag)
                    {
                        ans++;
                    }
                    continue;
                }
                
                // if(grid[nr][nc]==0)
                // {
                //      grid[nr][nc]=-1;
                // }
               grid[nr][nc]=-1;
                solve(grid,n,m,nr,nc,dp,ans);
                grid[nr][nc]=0;
                //  if(grid[nr][nc]==-1)
                // {
                //      grid[nr][nc]=0;
                // }
               
            }
            
        }
       
        
    }

    int uniquePathsIII(vector<vector<int>>& grid) {
        
        int n=grid.size();
        int ans=0;
        int m=grid[0].size();
        vector<vector<int>> dp(n,vector<int>(n,-1));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j]==1)
                   solve(grid,n,m,i,j,dp,ans);
            }
        }
        return ans;
        
    }
};