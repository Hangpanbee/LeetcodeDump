class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {
        
        int[] prefixSum = new int[length+1];
        
        for (int[] update: updates) {
            int s = update[0];
            int e = update[1];
            int add = update[2];
            prefixSum[s] += add;
            prefixSum[e+1] -= add; 
        }
        
        int[] ans = new int[length];
        int runningSum = 0;
        for (int i = 0; i < length; i++) {
            runningSum += prefixSum[i];
            ans[i] = runningSum;
        }
        
        return ans;
        
    }
}