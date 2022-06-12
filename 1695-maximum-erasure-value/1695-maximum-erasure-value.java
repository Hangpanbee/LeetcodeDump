class Solution {
    public int maximumUniqueSubarray(int[] nums) {
     // positive
    // subarray that only contains unique -> contiguous
    // sliding window
        int l = 0; int r = 0;
        Map<Integer, Integer> windowCounts = new HashMap<>();
        int windowSum = 0;
        int maxScore = 0;
        while (r < nums.length) {
            // r = 0, windowCounts = {}
            // r = 1, windowCounts = {4:1}
            // r = 2, l = 0, windowCounts = {4:1, 2:1}
            while (windowCounts.containsKey(nums[r])) {
                maxScore = Math.max(maxScore, windowSum);
                // maxScore = 6
                windowCounts.put(nums[l], windowCounts.get(nums[l])-1);
                // windowCounts = {2: 1}
                if (windowCounts.get(nums[l]) == 0) {
                    windowCounts.remove(nums[l]);
                }
                windowSum -= nums[l];
                // windowSum = 2
                l++;
                //l=1
            }
            
            //windowCounts = {4: 1, 2: 1}
            windowCounts.put(nums[r], windowCounts.getOrDefault(nums[r],0)+1);
            windowSum += nums[r];
            // windowSum = 4;
            // windowSum = 6;
            r++;
        }
        
        return Math.max(maxScore, windowSum);
        
    }
}