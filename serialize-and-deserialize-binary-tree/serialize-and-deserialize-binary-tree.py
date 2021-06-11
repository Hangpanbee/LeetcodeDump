# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def returnSerialize(root, ansStr):
            if not root: return "None,"
            ansStr =  str(root.val) + "," + returnSerialize(root.left, ansStr) + returnSerialize(root.right, ansStr)
            return ansStr
        return returnSerialize(root, "")[:-1]       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = data.split(",")
        # write a helper function
        def rDeserialize(root):
            if not root: return
            if root[0] == "None":  
                root.pop(0)
                return None
            Node = TreeNode(root.pop(0))
            Node.left = rDeserialize(root)
            Node.right = rDeserialize(root)
            return Node
        return rDeserialize(root)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))