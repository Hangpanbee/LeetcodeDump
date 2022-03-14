class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.left_index = l
        self.right_index = r
        self.val = 0


class NumArray:

    def __init__(self, nums: List[int]):
        
        def construct_tree(nums, l, r):
            if l > r:
                return None
            
            if l == r:
                curr_node = Node(l, r)
                curr_node.val = nums[l]
                return curr_node, curr_node.val
            
            midPoint = l + (r-l)//2
            root = Node(l, r)
            
            root.left, left_val = construct_tree(nums, l, midPoint)
            root.right, right_val = construct_tree(nums, midPoint+1, r)
        
            root.val = left_val + right_val
            
            return root, root.val
        
        self.tree, total = construct_tree(nums, 0, len(nums)-1)
        #print(self.tree.left.val, self.tree.right.val)

    def update(self, index: int, val: int) -> None:
        root = self.tree
        @lru_cache(None)
        def traverse(root, index, val):
            if not root: return 0
            
            if root.left_index == index and root.right_index == index:
                #print(root.left_index, root.right_index)
                root.val = val
                return root.val
                
            midPoint = root.left_index + (root.right_index - root.left_index)//2
            
            if index <= midPoint:
                left = traverse(root.left, index, val)
            else:
                right = traverse(root.right, index, val)
            root.val = root.left.val + root.right.val
            return root.val
                
        traverse(root, index, val)
        #print(self.tree.left.val, self.tree.right.val)

    def sumRange(self, left: int, right: int) -> int:
        root = self.tree
        @lru_cache(None)
        def traverse(root, left, right):
            if not root: return 0
            if root.left_index == left and root.right_index == right:
                return root.val
            
            
            mid = root.left_index + (root.right_index - root.left_index)//2

            #left_val, right_val = 0, 0
            if right <= mid:
                return traverse(root.left, left, right)
            elif left >= (mid+1):
                return traverse(root.right, left, right)
            else:
                left_val = traverse(root.left, left, mid)
                right_val = traverse(root.right, mid+1, right)
                return left_val + right_val
            
        return traverse(root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)