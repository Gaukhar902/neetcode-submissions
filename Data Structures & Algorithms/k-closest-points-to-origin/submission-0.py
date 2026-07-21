class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a list to store (distance, point) and sort it
        res = []
        for p in points:
            # distance squared is sufficient for comparison (x^2 + y^2)
            dist = p[0]**2 + p[1]**2
            res.append((dist, p))
        
        res.sort(key=lambda x: x[0])
        return [p for dist, p in res[:k]]