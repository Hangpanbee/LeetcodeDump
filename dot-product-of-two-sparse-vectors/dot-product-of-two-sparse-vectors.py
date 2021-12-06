class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)
        self.nonZeroIndex = set()
        for i, v in enumerate(self.nums):
            if v != 0:
                self.nonZeroIndex.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vec_nonZeroIndex = vec.nonZeroIndex
        product = 0
        traverse = self.nonZeroIndex.intersection(vec_nonZeroIndex)
        
        for i in traverse:
            product += vec.nums[i] * self.nums[i]
        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)