# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        #dfs
        self.dfs(root, [], targetSum)
        return self.ans
        
    def dfs(self, root, ansList, currSum):
        if root:
            ## the recursive stack gives the value integer the value not a pointer
            ansList.append(root.val)
           
            if root.left: self.dfs(root.left, ansList.copy(), currSum - root.val)
 
            if root.right: self.dfs(root.right, ansList.copy(), currSum - root.val)

            ## when pass down an accumulator, pay attention to the last value, bc it wont be updated yet
            if root.left == None and root.right == None:      
                if currSum == root.val: 
                    
                    self.ans.append(ansList)
                
            
            
        