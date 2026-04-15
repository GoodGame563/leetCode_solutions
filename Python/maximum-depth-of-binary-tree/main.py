from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right) 

Solution().maxDepth(TreeNode(3,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7))))

print("Hello from maximum-depth-of-binary-tree!")
