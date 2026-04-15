from math import sqrt
from operator import itemgetter
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        new_sqrt:list[tuple[list, float]] = []
        for point in points:
            new_sqrt.append((point, sqrt(point[0]**2 +point[1]**2)))
        new_sqrt=sorted(new_sqrt, key=lambda el: el[1])
        return [list(el) for el, _ in new_sqrt[:k]]



print(Solution().kClosest(points = [[2,2],[2,2],[3,3],[2,-2],[1,1]], k = 4))

print("Hello from k-closest-points-to-origin!")
