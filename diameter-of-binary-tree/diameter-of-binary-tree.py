# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not using a global value solution
    def __init__(self):
        self.count = 0
    # each node try to find the max leg left and right
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root)[0]
       
        
        
    def helper(self, root):
        
        if root:
           
            # each function call returns the diameter of the current subtree and the longest leg
            leftDia, leftHeight = self.helper(root.left)
            rightDia, rightHeight = self.helper(root.right)
            print(leftDia, rightDia, root.val, leftHeight, rightHeight)
            
            # the diameter of each node is the longest left leg + longest right leg
            # so it is important to callback the height of each child
            currHeight = 1 + max(leftHeight, rightHeight)

            return max(leftDia, rightDia, leftHeight+rightHeight), currHeight
        
        # -1 bc the vertices is always num(Nodes)-1
        else: return 0,0