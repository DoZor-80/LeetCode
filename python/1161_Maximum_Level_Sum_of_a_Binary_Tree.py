from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = {}
        current_max = root.val
        result = 1

        def recursive(node: TreeNode, level: int, sums: dict) -> None:
            level += 1
            sums[level] = sums.get(level, 0) + node.val
            for child in node.left, node.right:
                if child is not None:
                    recursive(child, level, sums)

        recursive(root, 0, sums)
        for key, value in sums.items():
            if current_max < sums[key]:
                current_max = sums[key]
                result = key
        return result
