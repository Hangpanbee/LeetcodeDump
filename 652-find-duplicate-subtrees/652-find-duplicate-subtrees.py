# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        ans = []
        def helper(root, seen):
            if not root:
                return "*"
            #create some sort of hash
            hashed =  str(root.val)+"-" + helper(root.left, seen) + helper(root.right, seen)
            seen[hashed].append(root)
            if len(seen[hashed]) == 2:
                ans.append(root)
            return hashed

        seen = collections.defaultdict(list)
        helper(root, seen)
    

       
                    
        return ans
        
    