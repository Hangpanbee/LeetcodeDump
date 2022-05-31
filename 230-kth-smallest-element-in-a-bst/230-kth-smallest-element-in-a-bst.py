# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        
        def inorder(root, smallerCount, kVal):
            if not root: return (smallerCount, kVal)
            
            leftCount, leftKval = inorder(root.left, smallerCount, kVal)
            
            currSmaller = 1 + leftCount
            foundK = kVal or leftKval
            #print(currSmaller )
            if currSmaller == k:
                foundK = root.val
            #print(foundK)
            right = inorder(root.right, currSmaller, foundK)
            
            #print(right)
            return right
        
        return inorder(root, 0, None)[1]