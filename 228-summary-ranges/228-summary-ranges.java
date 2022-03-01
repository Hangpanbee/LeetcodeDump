class Solution {
    public List<String> summaryRanges(int[] nums) {
        int l = 0;
        int r = 1;
   
        ArrayList<String> ans = new ArrayList<String>();
        while (r <= nums.length) {
            if (r == nums.length || nums[r] != (nums[l] + r-l)) {
                if (l == (r-1)) {
                    ans.add(Integer.toString(nums[l]));
                } else {
                    ans.add(Integer.toString(nums[l]) + "->" + Integer.toString(nums[r-1]));
                };
                
                l = r;
            };
            
            r++;
            
        };
        
        return ans;
    };
};