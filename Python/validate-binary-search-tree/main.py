from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_valid(self, node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return self.is_valid(node.left, min_val, node.val) and self.is_valid(node.right, node.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float('-inf'), float('inf'))
    
Solution().isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))))
        
print("Hello from validate-binary-search-tree!")
