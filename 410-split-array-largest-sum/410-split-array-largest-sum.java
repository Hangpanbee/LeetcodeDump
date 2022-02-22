class Solution {
    public int splitArray(int[] nums, int m) {
        int sum_nums = 0;
        int num_max = 0;
        for (int num: nums) {
            sum_nums += num;
            num_max = Math.max(num_max, num);
        };
        
        long l = num_max;
        long r = sum_nums;
        long mid;
        while (l < r) {
            mid = l + (r-l)/2; 
            if (valid(mid, nums, m) == true) {
                r = mid ;
            } else {
                l = mid + 1;
            };
        };
        
        return (int)l;
    };
    
    public boolean valid(long target, int[] nums, int m) {
        int count_m = 0;
        int total = 0;
        
        for (int num :nums) {
            total += num;
            if (total > target) {
                total = num;
                count_m++;
                if (count_m >= m) {
                    return false;
                };
            };
                
        };
        
        return true;
        
    }
    
    
    
}