# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def helper(nums):
            if not nums: return None
            currMax, currMaxI = 0, 0
            for i, v in enumerate(nums):
                if v > currMax:
                    currMaxI, currMax = i, v
                    
            currNode = TreeNode(currMax)
            currNode.left = helper(nums[0:currMaxI])
            currNode.right = helper(nums[currMaxI+1:])
            
            
            return currNode
        
        
        return helper(nums)