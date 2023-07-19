class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        result = []

        def recursive(node: TreeNode, parent):
            if node is None:
                return  # close the loop
            graph[node.val] = [child.val for child in {parent, node.left, node.right} if child is not None]
            recursive(node.left, node)
            recursive(node.right, node)

        def recursive_graph(val, prev, current_distance):
            if current_distance == k:
                result.append(val)
                return
            current_distance += 1
            for node in graph[val]:
                if node != prev:
                    recursive_graph(node, val, current_distance)

        recursive(root, None)
        recursive_graph(target.val, None, 0)

        return result
