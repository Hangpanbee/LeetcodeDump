# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = collections.deque()
        q.append((root, 0))
        levelToVal = collections.defaultdict(list)
        while q:
            currRoot, currLvl = q.popleft()
            nextLevel = currLvl + 1

            levelToVal[nextLevel].append(currRoot.val)
     
            if currRoot.right:
                q.append((currRoot.right, nextLevel))
            if currRoot.left:
                q.append((currRoot.left, nextLevel))

                    
                   
        for k, v in levelToVal.items():
            if k%2==1: v.reverse()
        
        return levelToVal.values()
            
            