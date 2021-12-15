class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        curr_dict = {}
        max_length = 0
        slow, fast = 0, 0
        
        while fast < len(s):
            
            curr_dict[s[fast]] = 1 if s[fast] not in curr_dict else curr_dict[s[fast]] + 1
            

            while len(curr_dict) > 2:
                curr_dict[s[slow]] -= 1
                if curr_dict[s[slow]] == 0:
                    del curr_dict[s[slow]]
                slow += 1
            max_length = max(max_length, fast-slow+1)
            fast += 1
        
        return max_length