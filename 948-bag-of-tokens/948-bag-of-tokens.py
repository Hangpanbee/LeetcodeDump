class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        tokens.sort()
        # go greedy then dp
        
        l, r = 0, len(tokens)-1
        curr_power = power
        curr_score = 0
        while l <= r:
            
            if curr_power < tokens[l] and curr_score > 0 and r-l > 1:
                curr_power += tokens[r]
                r-=1
                curr_score -= 1
            elif curr_power >= tokens[l]:
                curr_power -= tokens[l]
                l+= 1
                curr_score += 1
            else:
                return curr_score
        
        return curr_score
        
        