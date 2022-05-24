# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.treeSt = []
        curr = root
        while curr:
            self.treeSt.append(curr)
            curr = curr.left

    def next(self) -> int:
        curr = self.treeSt.pop()
        if curr.right:
            nxt = curr.right
            while nxt:
                self.treeSt.append(nxt)
                nxt = nxt.left

        return curr.val

    def hasNext(self) -> bool:
        return self.treeSt


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()