class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        reverse_graph = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            reverse_graph[prerequisite[1]].append(prerequisite[0])

        courses_without_prerequisites = []
        connectivity_level = []
        for key, value in graph.items():
            connectivity_level.append(len(value))
            if not value:
                courses_without_prerequisites.append(key)

        can_finish = [False] * numCourses
        for node in courses_without_prerequisites:
            can_finish[node] = True

            for end_node in reverse_graph[node]:
                connectivity_level[end_node] -= 1
                if connectivity_level[end_node] == 0:
                    courses_without_prerequisites.append(end_node)

        return True if False not in can_finish else False
