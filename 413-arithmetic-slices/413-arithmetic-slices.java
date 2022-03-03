class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length == 1) {
            return 0;
        };
        
        int curr_diff = nums[1] - nums[0];
        int l = 0;
        int r = 1;
        int ans = 0;
        while (r < nums.length) {
            if ((nums[r] - nums[r-1]) != curr_diff) {
                curr_diff = nums[r] - nums[r-1];
                l = r-1;
                r++;
                continue;
            }; 
            
            if ((r-l+1) >= 3) {
                ans += (r-l+1) - 3 + 1;
            };
            r++;
            
        };
        
        return ans;
        
            
    }
}