class Solution:
    def minSwaps(self, data_list: List[int]) -> int:
        window_size = sum(data_list)

        l, r = 0, 0
        window_sum = 0
        ans = 0
        while r < len(data_list):

            window_sum += data_list[r]
            if (r - l + 1) == window_size:

                ans = max(ans, window_sum)

                window_sum -= data_list[l]

                l += 1
            r += 1

        return window_size - ans
                
        