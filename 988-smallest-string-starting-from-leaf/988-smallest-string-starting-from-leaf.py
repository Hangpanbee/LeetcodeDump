# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
     
        def traverse(root):
            if not root: return ""
            if not root.left and not root.right:
                return chr(root.val+97)
            currChr = chr(root.val+97)
            left = traverse(root.left)
            right = traverse(root.right)
      
            if left:
                left += currChr
            if right:
                right += currChr
    
            if not right or (left and left <= right):
                return left
            elif not left or (right and right <= left):
                return right

        self.ans = '{}'
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                self.ans = min(self.ans, chr(root.val + 97) + path)
            dfs(root.left, chr(root.val + 97) + path)
            dfs(root.right, chr(root.val + 97) + path)
        dfs(root, '')
        return self.ans
        #return traverse(root)