# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        trees = {i: [] for i in range(n + 1)}
        trees[1] = [TreeNode()]

        for nodes_used in range(3, n + 1, 2):
            for i in range(1, nodes_used - 1, 2):
                j = nodes_used - 1 - i
                for left in trees[i]:
                    for right in trees[j]:
                        trees[nodes_used].append(TreeNode(0, left, right))
        return trees[n]
