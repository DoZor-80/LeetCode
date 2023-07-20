class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        reverse_graph = {i: [] for i in range(length)}
        initial_safe_nodes = []
        connectivity_level = [0] * length

        for i in range(length):
            if graph[i]:
                for end_node in graph[i]:
                    reverse_graph[end_node].append(i)
                    connectivity_level[i] += 1
            else:
                initial_safe_nodes.append(i)

        is_safe = [False] * length

        for node in initial_safe_nodes:
            is_safe[node] = True

            for end_node in reverse_graph[node]:
                connectivity_level[end_node] -= 1
                if connectivity_level[end_node] == 0:
                    initial_safe_nodes.append(end_node)

        return [i for i in range(length) if is_safe[i]]
