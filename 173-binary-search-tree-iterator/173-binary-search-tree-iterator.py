# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            self.tree.append(root)
            dfs(root.right)
        dfs(root)
        #print(self.tree)
        self.nextPointer = -1

    def next(self) -> int:
        self.nextPointer += 1
        return self.tree[self.nextPointer].val

    def hasNext(self) -> bool:
        return self.nextPointer < (len(self.tree)-1)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()