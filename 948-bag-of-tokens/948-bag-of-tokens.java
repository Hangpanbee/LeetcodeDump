class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        if (tokens.length == 0) return 0;
        
        Arrays.sort(tokens);
        int l = 0; int r = tokens.length-1;
        int currPower = power;
        int currScore = 0;
        while (l <= r) {
            
            if (currPower < tokens[l] && currScore > 0 && r-l > 1) {
                currPower += tokens[r];
                r--;
                currScore -= 1;
            } else if (currPower >= tokens[l]) {
                currPower -= tokens[l];
                l++;
                currScore += 1;
            } else {
                return currScore;
            }
        }
        
        return currScore;
        
    }
}