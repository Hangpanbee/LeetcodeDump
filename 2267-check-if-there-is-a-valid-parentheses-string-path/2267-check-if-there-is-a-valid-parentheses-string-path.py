class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        @lru_cache(None)
        def helper(x,y,count):
            if x==n-1 and y==m-1:
                if count==1 and grid[n-1][m-1]==")":
                    return True
                else:
                    return False
            elif count==-1:
                return False
            else:
                ans=False
                if grid[x][y]==")":
                    count-=1
                else:
                    count+=1
                xt=[x+1,x]
                yt=[y,y+1]
                for i in range(0,2):
                    if xt[i]<n and yt[i]<m:
                        ans=ans or helper(xt[i],yt[i],count)
                return ans
        return helper(0,0,0)
                        
        
    
        return False
            
    
    def getParaValue(self, para):
        return 1 if para == "(" else -1