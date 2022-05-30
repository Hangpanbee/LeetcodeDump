# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        lowestL = 0
        mapLevelToVals = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0))
        
        while q:
            currRoot, level = q.popleft()
            mapLevelToVals[level].append(currRoot.val)
            if currRoot.left:
                lowestL = level + 1
                q.append((currRoot.left, level+1))
            
            if currRoot.right:
                lowestL = level + 1
                q.append((currRoot.right, level+1))
        
        ans = []
        while lowestL >= 0:
            ans.append(mapLevelToVals[lowestL])
            lowestL -= 1
        
        return ans