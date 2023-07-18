class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(node, level):
            if node is None:
                return level
            level += 1
            if node.left is None and node.right is None:
                return level
            left = recursive(node.left, level) if node.left is not None else float('inf')
            right = recursive(node.right, level) if node.right is not None else float('inf')
            return min(left, right)

        return recursive(root, 0)
