from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


tree = TreeNode(1,TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))))
Solution().inorderTraversal(tree)
print("Hello from binary-tree-inorder-traversal!")
