# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapColToNode = collections.defaultdict(list)
        mapColRowToNode = collections.defaultdict(list)
        self.minCol = 9999999999
        def dfs(root, r, c):
            
            if not root: return
            self.minCol = min(self.minCol, c)

            mapColRowToNode[(r, c)].append(root.val)
            
            #mapColToNode[c].append(root.val)
            left = dfs(root.left, r+1, c-1)
            right = dfs(root.right, r+1, c+1)
            
        dfs(root, 0, 0)
        
        sortedColRow = [*mapColRowToNode]
        sortedColRow.sort(key=lambda x: (x[1], x[0]))
        previousCol = -999999
        ans = []
        for row, col in sortedColRow:
            if col == previousCol:
                ans[-1].extend(sorted(mapColRowToNode[(row, col)]))
            else: 
                ans.append(sorted(mapColRowToNode[(row, col)]))
            previousCol = col
        
        #print(sortedColRow, mapColRowToNode)

        return ans