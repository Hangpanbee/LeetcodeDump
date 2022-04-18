class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        def countArraysHaveSumLessOrEqual(targetSum, r, curSum, k):
            if curSum > targetSum: return 0
            if r == m: return 1  # found a valid array with sum <= targetSum
            ans = 0
            for c in range(n):
                cnt = countArraysHaveSumLessOrEqual(targetSum, r + 1, curSum + mat[r][c], k - ans)
                if cnt == 0: break  # prune, the array (which contains mat[r][c]) has sum > targetSum -> No need to process anymore
                ans += cnt
                if ans > k: break  # Important prune, since count > k -> No need to process anymore
            return ans

        left, right, ans = m, m * 5000, -1
        while left <= right:
            mid = left + (right - left) // 2
            cnt = countArraysHaveSumLessOrEqual(mid, 0, 0, k)
            if cnt >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans