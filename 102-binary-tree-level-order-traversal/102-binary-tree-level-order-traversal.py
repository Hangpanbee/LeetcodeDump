# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        mapLevelToValsList = collections.defaultdict(list)
        q = collections.deque()
        q.append((root,0))
        
        
        while q:
            currNode, currLevel = q.popleft()
            mapLevelToValsList[currLevel].append(currNode.val)
            
            if currNode.left:
                q.append((currNode.left, currLevel+1))
            if currNode.right:
                q.append((currNode.right, currLevel+1))
        
        ans = []
        currLevel = 0
        while currLevel in mapLevelToValsList:
            ans.append(mapLevelToValsList[currLevel])
            currLevel+=1
            
        return ans
        
        