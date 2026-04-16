

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_stack = None
        q_stack =None
        stack = []
        visited = set()
        while root or len(stack) > 0:
            if len(stack) > 0:
                root = stack.pop()
            while root:
                if root == p and not p_stack:
                    p_stack = stack.copy()
                    p_stack.append(root)
                if root == q and not q_stack:
                    q_stack = stack.copy()
                    q_stack.append(root)
                if not root.left and not root.right:
                    root = None
                    continue
                if root in visited and root.right in visited and root.left in visited:
                    root = None
                    continue
                stack.append(root)
                if not root.left in visited:
                    root = root.left
                    visited.add(root)   
                    continue
                if not root.right in visited:
                    root = root.right
                    visited.add(root)
                    continue
                visited.add(root)
        for i in range(min(len(p_stack), len(q_stack))+1):
            if len(p_stack) <= i or len(q_stack) <= i or p_stack[i] != q_stack[i]:
                return p_stack[i-1]
                


        return root

q = TreeNode(4)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))

Solution().lowestCommonAncestor(TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8))), p, q)
        

print("Hello from lowest-common-ancestor-of-a-binary-tree!")
