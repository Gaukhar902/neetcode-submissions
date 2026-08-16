class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for dest, src in prerequisites:
            adj[src].append(dest)
        
        visited = [0] * numCourses # 0: unvisited, 1: visiting, 2: visited
        
        def has_cycle(u):
            if visited[u] == 1: return True
            if visited[u] == 2: return False
            
            visited[u] = 1
            for v in adj[u]:
                if has_cycle(v): return True
            visited[u] = 2
            return False
        
        for i in range(numCourses):
            if has_cycle(i): return False
        return True